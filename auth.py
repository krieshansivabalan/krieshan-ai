import os
from datetime import datetime
from flask import Blueprint, redirect, url_for, session, request
from flask_login import login_user, logout_user, login_required, current_user
from models import db, User

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

# Set by init_oauth() called from app.py
_oauth = None


def init_oauth(oauth):
    global _oauth
    _oauth = oauth
    _oauth.register(
        name="google",
        client_id=os.environ.get("GOOGLE_CLIENT_ID", ""),
        client_secret=os.environ.get("GOOGLE_CLIENT_SECRET", ""),
        server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
        client_kwargs={"scope": "openid email profile"},
    )


@auth_bp.route("/google")
def login_google():
    # If no Google credentials configured, create a dev user and log straight in
    if not os.environ.get("GOOGLE_CLIENT_ID"):
        dev_user = User.query.filter_by(email="dev@localhost").first()
        if not dev_user:
            dev_user = User(
                google_id="dev-local",
                email="dev@localhost",
                name="Dev User",
                picture_url="",
            )
            db.session.add(dev_user)
            db.session.commit()
        dev_user.last_login_at = datetime.utcnow()
        db.session.commit()
        login_user(dev_user, remember=True)
        return redirect(url_for("index"))  # /app

    redirect_uri = url_for("auth.callback", _external=True)
    return _oauth.google.authorize_redirect(redirect_uri)


@auth_bp.route("/callback")
def callback():
    token = _oauth.google.authorize_access_token()
    userinfo = token.get("userinfo")
    if not userinfo:
        userinfo = _oauth.google.userinfo()

    google_id = userinfo["sub"]
    email = userinfo["email"]
    name = userinfo.get("name", email.split("@")[0])
    picture = userinfo.get("picture", "")

    # Upsert: find by google_id, fall back to email
    user = User.query.filter_by(google_id=google_id).first()
    if not user:
        user = User.query.filter_by(email=email).first()
        if user:
            user.google_id = google_id
        else:
            user = User(google_id=google_id, email=email, name=name)
            db.session.add(user)

    user.name = name
    user.picture_url = picture
    user.last_login_at = datetime.utcnow()
    db.session.commit()

    session.permanent = True
    login_user(user, remember=True)
    # Keep session["paid"] in sync so transit route works without extra DB hit
    session["paid"] = user.is_paid

    next_url = session.pop("next", None)
    return redirect(next_url or url_for("index"))  # /app


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    session.clear()
    return redirect(url_for("landing"))
