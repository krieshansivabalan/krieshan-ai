import os
import json
import traceback
import datetime as dt
from datetime import datetime, timedelta

import stripe
import anthropic
from flask import Flask, render_template, request, jsonify, session, redirect, url_for, Response
from flask_login import LoginManager, login_required, current_user
from authlib.integrations.flask_client import OAuth

from models import db, User, BirthChart, Subscription, JournalEntry, ChatMessage, TIER_LIMITS
from auth import auth_bp, init_oauth
from astrology import get_chart, get_transits, get_today_moon_nakshatra, AYANAMSA_EXPLAINERS, get_navamsa_chart, get_dasamsa_chart
from characters import get_characters
from interpretations import (
    get_daily_horoscope, get_nakshatra_ritual, get_dasha_interpretation,
    ANTAR_DASHA_NOTES, calculate_kuta_score, get_fixed_star_interpretation,
    ARUDHA_INTERP, INDU_INTERP,
)

# ── App setup ─────────────────────────────────────────────────────
app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "sidereal-dev-secret-key-change-in-prod")

# Database
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL", "sqlite:///sidereal.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(hours=8)
db.init_app(app)

# Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message = ""

# OAuth
oauth = OAuth(app)
init_oauth(oauth)
app.register_blueprint(auth_bp)

# Stripe
stripe.api_key = os.environ.get("STRIPE_SECRET_KEY", "")
STRIPE_PUBLISHABLE_KEY = os.environ.get("STRIPE_PUBLISHABLE_KEY", "")
STRIPE_PRICE_ID = os.environ.get("STRIPE_PRICE_ID", "")
STRIPE_WEBHOOK_SECRET = os.environ.get("STRIPE_WEBHOOK_SECRET", "")

# Create all DB tables on first run (safe to call repeatedly)
with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Create tables on first run
with app.app_context():
    db.create_all()


# ── Auth pages ────────────────────────────────────────────────────
@app.route("/login")
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    return render_template("login.html")


# ── Main app ──────────────────────────────────────────────────────
@app.route("/")
@login_required
def index():
    return render_template(
        "index.html",
        stripe_publishable_key=STRIPE_PUBLISHABLE_KEY,
        user=current_user,
        ayanamsa_explainers=AYANAMSA_EXPLAINERS,
        arudha_interp=ARUDHA_INTERP,
        indu_interp=INDU_INTERP,
    )


@app.route("/dashboard")
@login_required
def dashboard():
    # Dashboard is admin-only — redirect to admin login if not authenticated
    if not _admin_session_valid():
        session.pop("admin_auth", None)
        session.pop("admin_auth_ts", None)
        return redirect(url_for("admin_login"))
    charts = current_user.charts.order_by(BirthChart.created_at.desc()).all()
    return render_template("dashboard.html", user=current_user, charts=charts)


@app.route("/synastry")
@login_required
def synastry():
    return render_template("synastry.html", user=current_user)


@app.route("/journal")
@login_required
def journal():
    return render_template("journal.html", user=current_user)


@app.route("/learn")
def learn():
    return render_template("learn.html", user=current_user if current_user.is_authenticated else None)


@app.route("/navamsa")
@login_required
def navamsa():
    return render_template("navamsa.html", user=current_user, ayanamsa_explainers=AYANAMSA_EXPLAINERS)


@app.route("/d10")
@login_required
def d10():
    return render_template("d10.html", user=current_user, ayanamsa_explainers=AYANAMSA_EXPLAINERS)


# ── Chart calculation ─────────────────────────────────────────────
@app.route("/chart", methods=["POST"])
@login_required
def chart():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data received."}), 400

        name           = (data.get("name") or "").strip()
        date           = (data.get("date") or "").strip()
        time           = (data.get("time") or "").strip()
        city           = (data.get("city") or "").strip()
        gender         = (data.get("gender") or "M").strip().upper()[:1]
        ayanamsa_system = (data.get("ayanamsa") or "lahiri").strip()

        if not date:
            return jsonify({"error": "Please enter a birth date."}), 400
        if not time:
            return jsonify({"error": "Please enter a birth time."}), 400
        if not city:
            return jsonify({"error": "Please enter a birth city."}), 400

        result = get_chart(name, date, time, city, ayanamsa_system=ayanamsa_system)

        # Store in session for transit calculations + AI chat
        session["natal_lat"]        = result["latitude"]
        session["natal_lon"]        = result["longitude"]
        session["natal_placements"] = _slim_placements(result["placements"])
        session["ayanamsa_system"]  = ayanamsa_system
        # Build a slim natal context string for AI chat (no chart_id yet)
        ctx_lines = [f"Name: {name or 'the person'}", f"Date: {date}", f"Time: {time}", f"City: {city}", ""]
        for pn, pd in result["placements"].items():
            ctx_lines.append(f"  {pn}: {pd.get('sign','')} {pd.get('degree',0):.1f}° House {pd.get('house','')} Nakshatra: {pd.get('nakshatra','')}")
        session["natal_context"] = "\n".join(ctx_lines)

        # Enrich dasha with interpretations
        if result.get("dasha"):
            dasha = result["dasha"]
            if dasha.get("current_maha"):
                dasha["current_maha"]["interpretation"] = get_dasha_interpretation(
                    dasha["current_maha"]["lord"]
                )
            if dasha.get("current_antar"):
                dasha["current_antar"]["note"] = ANTAR_DASHA_NOTES.get(
                    dasha["current_antar"]["lord"], ""
                )

        # Enrich fixed stars with per-planet interpretations
        for fs in result.get("fixed_stars", []):
            fs["planet_meaning"] = get_fixed_star_interpretation(fs["star"], fs["planet"])

        # Character archetypes
        characters = get_characters(
            result["sun_sign"], result["moon_sign"], result["rising_sign"], gender
        )

        # D9 Navamsa chart
        navamsa = get_navamsa_chart(result["placements"])

        # D10 Dasamsa chart
        dasamsa = get_dasamsa_chart(result["placements"])

        # Persist to database
        birth_chart = BirthChart(
            user_id=current_user.id,
            label=name or f"{city}, {date}",
            date=date,
            time=time,
            city=city,
            gender=gender,
            full_address=result.get("full_address", ""),
            placements_json=json.dumps(result.get("placements", {})),
            career_json=json.dumps(result.get("career", {})),
            romance_json=json.dumps(result.get("romance", {})),
        )
        db.session.add(birth_chart)
        db.session.commit()

        return jsonify({**result, "chart_id": birth_chart.id, "characters": characters, "navamsa": navamsa, "dasamsa": dasamsa})

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": f"Calculation error: {str(e)}"}), 500


@app.route("/api/navamsa", methods=["POST"])
@login_required
def api_navamsa():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data received."}), 400

        name            = (data.get("name") or "").strip()
        date            = (data.get("date") or "").strip()
        time_val        = (data.get("time") or "").strip()
        city            = (data.get("city") or "").strip()
        ayanamsa_system = (data.get("ayanamsa") or "lahiri").strip()

        if not date:
            return jsonify({"error": "Please enter a birth date."}), 400
        if not time_val:
            return jsonify({"error": "Please enter a birth time."}), 400
        if not city:
            return jsonify({"error": "Please enter a birth city."}), 400

        result = get_chart(name, date, time_val, city, ayanamsa_system=ayanamsa_system)
        navamsa = get_navamsa_chart(result["placements"])

        return jsonify({
            "name":            result["name"],
            "date":            result["date"],
            "time":            result["time"],
            "city":            result["city"],
            "full_address":    result["full_address"],
            "ayanamsa_label":  result["ayanamsa_label"],
            "sun_sign":        result["sun_sign"],
            "moon_sign":       result["moon_sign"],
            "rising_sign":     result["rising_sign"],
            "navamsa":         navamsa,
        })

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": f"Calculation error: {str(e)}"}), 500


@app.route("/api/d10", methods=["POST"])
@login_required
def api_d10():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data received."}), 400

        name            = (data.get("name") or "").strip()
        date            = (data.get("date") or "").strip()
        time_val        = (data.get("time") or "").strip()
        city            = (data.get("city") or "").strip()
        ayanamsa_system = (data.get("ayanamsa") or "lahiri").strip()

        if not date:
            return jsonify({"error": "Please enter a birth date."}), 400
        if not time_val:
            return jsonify({"error": "Please enter a birth time."}), 400
        if not city:
            return jsonify({"error": "Please enter a birth city."}), 400

        result  = get_chart(name, date, time_val, city, ayanamsa_system=ayanamsa_system)
        dasamsa = get_dasamsa_chart(result["placements"])

        return jsonify({
            "name":           result["name"],
            "date":           result["date"],
            "time":           result["time"],
            "city":           result["city"],
            "full_address":   result["full_address"],
            "ayanamsa_label": result["ayanamsa_label"],
            "sun_sign":       result["sun_sign"],
            "moon_sign":      result["moon_sign"],
            "rising_sign":    result["rising_sign"],
            "dasamsa":        dasamsa,
        })

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": f"Calculation error: {str(e)}"}), 500


def _slim_placements(placements):
    return {k: {"longitude": v["longitude"], "sign": v["sign"]}
            for k, v in placements.items()}


# ── Daily Horoscope ───────────────────────────────────────────────
@app.route("/api/daily-horoscope")
@login_required
def daily_horoscope():
    sun_sign    = request.args.get("sun")
    moon_sign   = request.args.get("moon")
    rising_sign = request.args.get("rising")

    day_seed = dt.date.today().timetuple().tm_yday
    result = {}
    for label, sign in [("sun", sun_sign), ("moon", moon_sign), ("rising", rising_sign)]:
        if sign:
            result[label] = {
                "sign":    sign,
                "reading": get_daily_horoscope(sign, day_seed),
            }

    # Also return today's Moon nakshatra
    try:
        moon_nak_data = get_today_moon_nakshatra()
        nak_name = moon_nak_data["nakshatra"]["name"]
        result["moon_nakshatra"] = {
            **moon_nak_data["nakshatra"],
            **get_nakshatra_ritual(nak_name),
            "sign": moon_nak_data["sign"],
        }
    except Exception:
        pass

    return jsonify(result)


# ── Tomorrow Moon ─────────────────────────────────────────────────
@app.route("/api/tomorrow-moon")
@login_required
def tomorrow_moon():
    """Return the Moon nakshatra for tomorrow — used for the 'return tomorrow' engagement hook."""
    try:
        moon_nak_data = get_today_moon_nakshatra(offset_days=1)
        nak  = moon_nak_data["nakshatra"]
        sign = moon_nak_data["sign"]
        themes = {
            "Ashwini": "swift beginnings and healing energy",
            "Bharani": "deep creative and transformative power",
            "Krittika": "sharp focus and purifying fire",
            "Rohini": "beauty, abundance, and sensory delight",
            "Mrigashira": "curious seeking and restless wonder",
            "Ardra": "emotional intensity and renewal through storms",
            "Punarvasu": "returning home to joy and optimism",
            "Pushya": "nourishment, luck, and spiritual guidance",
            "Ashlesha": "depth psychology and serpentine wisdom",
            "Magha": "ancestral power and royal authority",
            "Purva Phalguni": "rest, pleasure, and creative play",
            "Uttara Phalguni": "service, partnership, and steadfast giving",
            "Hasta": "skilled hands, healing, and precision",
            "Chitra": "art, beauty, and dazzling perception",
            "Swati": "independence, adaptability, and the wandering self",
            "Vishakha": "single-pointed ambition and triumph through perseverance",
            "Anuradha": "devotion, friendship, and steadfast loyalty",
            "Jyeshtha": "courage, protection, and leadership",
            "Mula": "deep roots, upheaval, and seeking ultimate truth",
            "Purva Ashadha": "invincibility, philosophy, and victorious momentum",
            "Uttara Ashadha": "lasting achievement and universal recognition",
            "Shravana": "deep listening, learning, and cosmic connectivity",
            "Dhanishtha": "music, rhythm, wealth, and group harmony",
            "Shatabhisha": "healing mysteries, solitude, and cosmic insight",
            "Purva Bhadrapada": "fierce transformation and otherworldly vision",
            "Uttara Bhadrapada": "calm depth, rain after storm, and deep compassion",
            "Revati": "safe passage, completion, and joyful endings",
        }
        theme = themes.get(nak["name"], "subtle cosmic shifts")
        return jsonify({"nakshatra": nak["name"], "sign": sign, "theme": theme})
    except Exception:
        return jsonify({"error": "Unavailable"}), 500


# ── Transits ──────────────────────────────────────────────────────
@app.route("/api/transits", methods=["GET"])
@login_required
def transits():

    natal_placements = session.get("natal_placements")
    if not natal_placements:
        return jsonify({"error": "Please generate your birth chart first."}), 400

    try:
        lat  = session.get("natal_lat", 0.0)
        lon  = session.get("natal_lon", 0.0)
        ayan = session.get("ayanamsa_system", "lahiri")
        result = get_transits(natal_placements, lat=lat, lon=lon, ayanamsa_system=ayan)

        # Enrich Moon nakshatra with ritual
        if result.get("moon_nakshatra"):
            nak_name = result["moon_nakshatra"]["name"]
            result["moon_nakshatra"].update(get_nakshatra_ritual(nak_name))

        return jsonify(result)
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": f"Transit calculation error: {str(e)}"}), 500


# ── Synastry API ──────────────────────────────────────────────────
@app.route("/api/synastry", methods=["POST"])
@login_required
def synastry_api():

    try:
        data = request.get_json()
        ayan = data.get("ayanamsa", "lahiri")

        # Calculate both charts
        chart_a = get_chart(
            data.get("name_a", "Person A"),
            data["date_a"], data["time_a"], data["city_a"],
            ayanamsa_system=ayan,
        )
        chart_b = get_chart(
            data.get("name_b", "Person B"),
            data["date_b"], data["time_b"], data["city_b"],
            ayanamsa_system=ayan,
        )

        # Kuta score from Moon nakshatras
        moon_nak_a = chart_a["placements"]["Moon"]["longitude"] // (360 / 27)
        moon_nak_b = chart_b["placements"]["Moon"]["longitude"] // (360 / 27)
        kuta = calculate_kuta_score(int(moon_nak_a), int(moon_nak_b))

        # Enrich kuta with dasha interpretations
        for chart, label in [(chart_a, "a"), (chart_b, "b")]:
            if chart.get("dasha") and chart["dasha"].get("current_maha"):
                chart["dasha"]["current_maha"]["interpretation"] = get_dasha_interpretation(
                    chart["dasha"]["current_maha"]["lord"]
                )

        return jsonify({
            "chart_a": chart_a,
            "chart_b": chart_b,
            "kuta":    kuta,
        })
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": f"Calculation error: {str(e)}"}), 500


# ── Journal API ───────────────────────────────────────────────────
@app.route("/api/journal", methods=["GET"])
@login_required
def get_journal():
    page = request.args.get("page", 1, type=int)
    entries = (current_user.journal_entries
               .order_by(JournalEntry.created_at.desc())
               .paginate(page=page, per_page=20, error_out=False))
    return jsonify({
        "entries": [{
            "id":              e.id,
            "content":         e.content,
            "entry_date":      e.entry_date,
            "moon_sign":       e.moon_sign,
            "moon_nakshatra":  e.moon_nakshatra,
            "is_retrograde":   e.is_retrograde_period,
            "created_at":      e.created_at.strftime("%B %d, %Y at %I:%M %p"),
        } for e in entries.items],
        "has_next": entries.has_next,
        "page":     page,
    })


@app.route("/api/journal", methods=["POST"])
@login_required
def create_journal():

    data = request.get_json()
    content = (data.get("content") or "").strip()
    if not content:
        return jsonify({"error": "Content cannot be empty."}), 400

    # Auto-stamp with today's Moon
    moon_sign = ""
    moon_nak  = ""
    try:
        moon_data = get_today_moon_nakshatra()
        moon_sign = moon_data["sign"]
        moon_nak  = moon_data["nakshatra"]["name"]
    except Exception:
        pass

    entry = JournalEntry(
        user_id=current_user.id,
        content=content,
        entry_date=dt.date.today().isoformat(),
        moon_sign=moon_sign,
        moon_nakshatra=moon_nak,
    )
    db.session.add(entry)
    db.session.commit()

    return jsonify({
        "id":             entry.id,
        "content":        entry.content,
        "entry_date":     entry.entry_date,
        "moon_sign":      entry.moon_sign,
        "moon_nakshatra": entry.moon_nakshatra,
        "created_at":     entry.created_at.strftime("%B %d, %Y at %I:%M %p"),
    })


@app.route("/api/journal/<int:entry_id>", methods=["DELETE"])
@login_required
def delete_journal(entry_id):
    entry = JournalEntry.query.filter_by(id=entry_id, user_id=current_user.id).first()
    if not entry:
        return jsonify({"error": "Not found"}), 404
    db.session.delete(entry)
    db.session.commit()
    return jsonify({"ok": True})


# ── Payment / Tier ────────────────────────────────────────────────
@app.route("/api/check-paid")
@login_required
def check_paid():
    tier    = current_user.plan_tier
    limits  = TIER_LIMITS.get(tier, TIER_LIMITS["free"])
    ai_rem  = current_user.ai_quota_remaining()
    session["paid"] = tier != "free"
    return jsonify({
        "paid":            tier != "free",
        "tier":            tier,
        "tier_label":      limits["label"],
        "ai_remaining":    ai_rem,
        "charts_limit":    limits["charts"],
        "charts_used":     current_user.charts.count(),
    })


@app.route("/create-checkout-session", methods=["POST"])
@login_required
def create_checkout_session():
    if not stripe.api_key or not STRIPE_PRICE_ID:
        _upsert_subscription(
            user=current_user,
            customer_id=None,
            subscription_id=None,
            status="active",
            period_end=None,
            dev_mode=True,
        )
        session["paid"] = True
        return jsonify({"dev_mode": True, "paid": True})

    try:
        customer_id = None
        if current_user.subscription and current_user.subscription.stripe_customer_id:
            customer_id = current_user.subscription.stripe_customer_id
        else:
            customer = stripe.Customer.create(
                email=current_user.email,
                metadata={"user_id": current_user.id},
            )
            customer_id = customer.id

        checkout_session = stripe.checkout.Session.create(
            customer=customer_id,
            payment_method_types=["card"],
            line_items=[{"price": STRIPE_PRICE_ID, "quantity": 1}],
            mode="subscription",
            success_url=request.host_url + "payment-success?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=request.host_url + "payment-cancel",
        )
        return jsonify({"checkout_url": checkout_session.url})
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


@app.route("/payment-success")
@login_required
def payment_success():
    session_id = request.args.get("session_id")
    if session_id and stripe.api_key:
        try:
            checkout_session = stripe.checkout.Session.retrieve(
                session_id, expand=["subscription"]
            )
            if checkout_session.payment_status in ("paid", "no_payment_required"):
                stripe_sub = checkout_session.subscription
                _upsert_subscription(
                    user=current_user,
                    customer_id=checkout_session.customer,
                    subscription_id=stripe_sub.id if stripe_sub else None,
                    status="active",
                    period_end=stripe_sub.current_period_end if stripe_sub else None,
                )
                session["paid"] = True
        except Exception:
            traceback.print_exc()
    else:
        session["paid"] = True

    return redirect(url_for("index") + "?paid=true")


@app.route("/payment-cancel")
def payment_cancel():
    return redirect(url_for("index") + "?cancelled=true")


@app.route("/stripe-webhook", methods=["POST"])
def stripe_webhook():
    payload = request.get_data(as_text=True)
    sig_header = request.headers.get("Stripe-Signature")

    if not STRIPE_WEBHOOK_SECRET:
        return jsonify({"ok": True})

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, STRIPE_WEBHOOK_SECRET)
    except Exception:
        return jsonify({"error": "Invalid signature"}), 400

    event_type = event["type"]
    if event_type in ("customer.subscription.updated", "customer.subscription.deleted"):
        sub_obj = event["data"]["object"]
        force_status = "cancelled" if event_type == "customer.subscription.deleted" else None
        _handle_subscription_event(sub_obj, force_status=force_status)

    return jsonify({"ok": True})


def _upsert_subscription(user, customer_id, subscription_id, status, period_end, dev_mode=False, plan_tier=None):
    sub = user.subscription
    if not sub:
        sub = Subscription(user_id=user.id)
        db.session.add(sub)
    if customer_id:
        sub.stripe_customer_id = customer_id
    if subscription_id:
        sub.stripe_subscription_id = subscription_id
    sub.status = status
    if plan_tier:
        sub.plan_tier = plan_tier
    elif not sub.plan_tier:
        sub.plan_tier = "seeker"
    if dev_mode:
        sub.current_period_end = datetime(2125, 1, 1)
    elif period_end:
        sub.current_period_end = datetime.utcfromtimestamp(period_end)
    db.session.commit()


def _handle_subscription_event(stripe_sub, force_status=None):
    customer_id = stripe_sub.get("customer")
    sub = Subscription.query.filter_by(stripe_customer_id=customer_id).first()
    if not sub:
        return
    raw_status = force_status or stripe_sub.get("status", "none")
    sub.status = "active" if raw_status == "active" else "cancelled"
    period_end = stripe_sub.get("current_period_end")
    if period_end:
        sub.current_period_end = datetime.utcfromtimestamp(period_end)
    db.session.commit()


# ── Saved charts API ──────────────────────────────────────────────
@app.route("/api/charts")
@login_required
def get_charts():
    charts = current_user.charts.order_by(BirthChart.created_at.desc()).all()
    return jsonify([{
        "id":           c.id,
        "label":        c.label,
        "date":         c.date,
        "time":         c.time,
        "city":         c.city,
        "full_address": c.full_address,
        "created_at":   c.created_at.strftime("%B %d, %Y"),
    } for c in charts])


@app.route("/api/charts/<int:chart_id>", methods=["DELETE"])
@login_required
def delete_chart(chart_id):
    chart = BirthChart.query.filter_by(id=chart_id, user_id=current_user.id).first()
    if not chart:
        return jsonify({"error": "Not found"}), 404
    db.session.delete(chart)
    db.session.commit()
    return jsonify({"ok": True})


@app.route("/api/charts/<int:chart_id>/load", methods=["POST"])
@login_required
def load_chart(chart_id):
    """Re-calculate and return a saved chart's full reading."""
    chart = BirthChart.query.filter_by(id=chart_id, user_id=current_user.id).first()
    if not chart:
        return jsonify({"error": "Chart not found"}), 404
    try:
        ayanamsa_system = (request.get_json() or {}).get("ayanamsa", "lahiri")
        result = get_chart(chart.for_person or chart.label or "", chart.date, chart.time,
                           chart.city, ayanamsa_system=ayanamsa_system)
        if result.get("dasha"):
            dasha = result["dasha"]
            if dasha.get("current_maha"):
                dasha["current_maha"]["interpretation"] = get_dasha_interpretation(dasha["current_maha"]["lord"])
            if dasha.get("current_antar"):
                dasha["current_antar"]["note"] = ANTAR_DASHA_NOTES.get(dasha["current_antar"]["lord"], "")
        for fs in result.get("fixed_stars", []):
            fs["planet_meaning"] = get_fixed_star_interpretation(fs["star"], fs["planet"])
        gender = chart.gender or "M"
        characters = get_characters(result["sun_sign"], result["moon_sign"], result["rising_sign"], gender)
        navamsa  = get_navamsa_chart(result["placements"])
        dasamsa  = get_dasamsa_chart(result["placements"])
        return jsonify({**result, "chart_id": chart.id, "characters": characters,
                        "navamsa": navamsa, "dasamsa": dasamsa})
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


# ── AI Chart Chat ─────────────────────────────────────────────────
_anthropic = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY", ""))

def _build_chart_context(chart_id, user):
    """Build a rich text context from a saved chart for AI prompting."""
    chart = BirthChart.query.filter_by(id=chart_id, user_id=user.id).first()
    if not chart:
        return None, None
    try:
        placements = json.loads(chart.placements_json or "{}")
    except Exception:
        placements = {}

    lines = [
        f"Name: {chart.for_person or chart.label or 'the person'}",
        f"Date of Birth: {chart.date}",
        f"Time of Birth: {chart.time}",
        f"City: {chart.city}",
        "",
        "PLANETARY PLACEMENTS (Sidereal/Vedic):",
    ]
    for pname, pdata in placements.items():
        sign    = pdata.get("sign", "")
        degree  = pdata.get("degree", 0)
        house   = pdata.get("house", "")
        nak     = pdata.get("nakshatra", "")
        retro   = " (R)" if pdata.get("retrograde") else ""
        lines.append(f"  {pname}: {sign} {degree:.1f}°{retro}  House {house}  Nakshatra: {nak}")

    # Add D9 and D10 quick summary
    try:
        nav = get_navamsa_chart(placements)
        das = get_dasamsa_chart(placements)
        lines += [
            "",
            f"D9 NAVAMSA — Marriage & Soul Chart:",
            f"  D9 Lagna: {nav.get('d9_lagna_sign')}  |  Venus D9: {nav.get('d9_venus_sign')}  |  7th House D9: {nav.get('d9_7th_sign')}  |  Darakaraka: {nav.get('darakaraka')}",
            "",
            f"D10 DASAMSA — Career Chart:",
            f"  D10 Lagna: {das.get('d10_lagna_sign')}  |  10th House: {das.get('d10_10th_sign')}  |  Amatyakaraka: {das.get('amatyakaraka')}  |  Saturn D10: {das.get('d10_saturn_sign')}",
        ]
    except Exception:
        pass

    return "\n".join(lines), chart


@app.route("/api/chat", methods=["POST"])
@login_required
def chart_chat():
    data     = request.get_json() or {}
    question = (data.get("question") or "").strip()
    chart_id = data.get("chart_id")

    if not question:
        return jsonify({"error": "Please enter a question."}), 400

    # ── Tier gate ─────────────────────────────────────────────────
    tier   = current_user.plan_tier
    if tier == "free":
        return jsonify({"error": "upgrade", "tier": "free",
                        "message": "AI Chart Chat is available on Seeker plan and above. Upgrade to unlock unlimited cosmic insight."}), 403

    # ── Monthly quota ─────────────────────────────────────────────
    now   = datetime.utcnow()
    limit = TIER_LIMITS[tier]["ai_questions"]   # -1 = unlimited
    if limit != -1:
        # Reset monthly counter if new month
        if (current_user.ai_questions_reset is None or
                now.year  != current_user.ai_questions_reset.year or
                now.month != current_user.ai_questions_reset.month):
            current_user.ai_questions_used  = 0
            current_user.ai_questions_reset = now
            db.session.commit()
        if (current_user.ai_questions_used or 0) >= limit:
            return jsonify({"error": "quota",
                            "message": f"You've used all {limit} AI questions for this month. Upgrade your plan or wait until next month."}), 429

    # ── Build context ─────────────────────────────────────────────
    if chart_id:
        chart_context, chart_obj = _build_chart_context(chart_id, current_user)
    else:
        chart_context = session.get("natal_context", "")
        chart_obj     = None

    if not chart_context:
        return jsonify({"error": "Please calculate a birth chart first before asking questions."}), 400

    # ── Prior conversation (last 6 messages for context) ──────────
    prior_msgs = []
    if chart_obj:
        history = (ChatMessage.query
                   .filter_by(user_id=current_user.id, chart_id=chart_obj.id)
                   .order_by(ChatMessage.created_at.desc())
                   .limit(6).all())
        for msg in reversed(history):
            prior_msgs.append({"role": msg.role, "content": msg.content})

    system_prompt = f"""You are Krieshan AI — a deeply knowledgeable Vedic astrologer and guide. You specialise in sidereal astrology, Jyotish, divisional charts (D9 Navamsa, D10 Dasamsa), Vimshottari dasha, nakshatras, and karaka theory.

You are speaking with {current_user.name}. Their birth chart data is below:

{chart_context}

Guidelines:
- Speak in warm, personal second-person ("you", "your")
- Give specific, chart-grounded answers — reference actual placements, signs, houses, and nakshatras
- Be insightful and precise, not generic
- Keep answers to 2–4 paragraphs unless asked for more
- Do not make up placements not in the chart data
- When relevant, connect D1, D9, and D10 insights
- You may suggest timing based on dasha periods if relevant
- Never refuse to engage with astrological questions about this chart"""

    messages = prior_msgs + [{"role": "user", "content": question}]

    try:
        response = _anthropic.messages.create(
            model="claude-3-5-haiku-20241022",
            max_tokens=1024,
            system=system_prompt,
            messages=messages,
        )
        answer = response.content[0].text
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": f"AI error: {str(e)}"}), 500

    # ── Persist messages & update usage counter ───────────────────
    try:
        if chart_obj:
            db.session.add(ChatMessage(user_id=current_user.id, chart_id=chart_obj.id, role="user",      content=question))
            db.session.add(ChatMessage(user_id=current_user.id, chart_id=chart_obj.id, role="assistant", content=answer))
        if limit != -1:
            current_user.ai_questions_used = (current_user.ai_questions_used or 0) + 1
        db.session.commit()
    except Exception:
        traceback.print_exc()

    remaining = current_user.ai_quota_remaining()
    return jsonify({"answer": answer, "remaining": remaining})


@app.route("/api/chat/history")
@login_required
def chat_history():
    chart_id = request.args.get("chart_id", type=int)
    q = ChatMessage.query.filter_by(user_id=current_user.id)
    if chart_id:
        q = q.filter_by(chart_id=chart_id)
    msgs = q.order_by(ChatMessage.created_at.asc()).limit(50).all()
    return jsonify([{"role": m.role, "content": m.content,
                     "created_at": m.created_at.strftime("%H:%M")} for m in msgs])


# ── PDF / Print Report ────────────────────────────────────────────
@app.route("/chart/<int:chart_id>/report")
@login_required
def chart_report(chart_id):
    """Render a print-optimised report page for a saved chart."""
    chart = BirthChart.query.filter_by(id=chart_id, user_id=current_user.id).first_or_404()
    try:
        placements = json.loads(chart.placements_json or "{}")
        result     = get_chart(chart.for_person or chart.label or "", chart.date,
                               chart.time, chart.city)
        navamsa    = get_navamsa_chart(result["placements"])
        dasamsa    = get_dasamsa_chart(result["placements"])
    except Exception:
        traceback.print_exc()
        placements, result, navamsa, dasamsa = {}, {}, {}, {}
    return render_template("chart_report.html",
                           chart=chart, result=result,
                           navamsa=navamsa, dasamsa=dasamsa,
                           user=current_user)


@app.route("/api/account", methods=["DELETE"])
@login_required
def delete_account():
    from flask_login import logout_user
    user = current_user._get_current_object()
    logout_user()
    session.clear()
    db.session.delete(user)
    db.session.commit()
    return jsonify({"ok": True})


# ── Admin Panel ───────────────────────────────────────────────────
_ADMIN_PASSWORD  = "Witstypeai2026!"
_ADMIN_SESSION_HOURS = 8   # session expires after 8 hours

def _admin_session_valid():
    """Return True only if admin_auth is set AND was granted within the last 8 hours."""
    if not session.get("admin_auth"):
        return False
    granted_at = session.get("admin_auth_ts")
    if not granted_at:
        return False
    try:
        delta = datetime.utcnow() - datetime.fromisoformat(granted_at)
        return delta.total_seconds() < _ADMIN_SESSION_HOURS * 3600
    except Exception:
        return False

def admin_required(f):
    from functools import wraps
    @wraps(f)
    def decorated(*args, **kwargs):
        if not _admin_session_valid():
            session.pop("admin_auth", None)
            session.pop("admin_auth_ts", None)
            return redirect(url_for("admin_login"))
        return f(*args, **kwargs)
    return decorated

@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    # If already authenticated with a valid session, skip straight to dashboard
    if _admin_session_valid():
        return redirect(url_for("admin_dashboard"))
    error = None
    if request.method == "POST":
        if request.form.get("password") == _ADMIN_PASSWORD:
            session["admin_auth"]    = True
            session["admin_auth_ts"] = datetime.utcnow().isoformat()
            session.permanent        = True
            return redirect(url_for("admin_dashboard"))
        error = "Incorrect password."
    return render_template("admin_login.html", error=error)

@app.route("/admin/logout")
def admin_logout():
    session.pop("admin_auth", None)
    session.pop("admin_auth_ts", None)
    return redirect(url_for("admin_login"))

@app.route("/admin")
@admin_required
def admin_dashboard():
    users = User.query.order_by(User.created_at.desc()).all()
    user_data = []
    for u in users:
        charts = u.charts.order_by(BirthChart.created_at.desc()).all()
        user_data.append({"user": u, "charts": charts})
    return render_template("admin_dashboard.html", user_data=user_data, total=len(users))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5050))
    debug = os.environ.get("FLASK_ENV", "development") == "development"
    app.run(debug=debug, host="0.0.0.0", port=port)
