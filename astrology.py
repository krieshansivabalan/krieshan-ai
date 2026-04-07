import ephem
import math
from datetime import datetime, timezone, timedelta
import pytz
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from interpretations import (
    SIGN_SYMBOLS, PLANET_SYMBOLS, PLANET_MEANINGS,
    SIGNS, get_interpretation, get_career_reading, get_romance_reading,
    get_transit_interpretation, get_nakshatra_info,
    YOGA_DATA, get_aspect_interpretation,
    SPOUSE_SIGN_QUALITIES, VENUS_SIGN_LOVE, SEVENTH_LORD_IN_HOUSE,
)

# ─── Ayanamsa Systems ──────────────────────────────────────────────────────────

J2000 = 2451545.0


def get_lahiri_ayanamsa(jd):
    years = (jd - J2000) / 365.25
    return (23.8531 + years * 0.013969) % 360


def get_fagan_bradley_ayanamsa(jd):
    """Fagan-Bradley (Western Sidereal) — ~0.9° larger than Lahiri."""
    years = (jd - J2000) / 365.25
    return (24.7163 + years * 0.013969) % 360


def get_krishnamurti_ayanamsa(jd):
    """Krishnamurti Paddhati — very close to Lahiri, slightly different epoch."""
    years = (jd - J2000) / 365.25
    return (23.8534 + years * 0.013969) % 360


def get_true_chitrapaksha_ayanamsa(jd):
    """True Chitrapaksha — keeps Spica (Chitra) exactly at 180°."""
    years = (jd - J2000) / 365.25
    return (23.8590 + years * 0.013969) % 360


AYANAMSA_FUNCTIONS = {
    "lahiri":            get_lahiri_ayanamsa,
    "fagan_bradley":     get_fagan_bradley_ayanamsa,
    "krishnamurti":      get_krishnamurti_ayanamsa,
    "true_chitrapaksha": get_true_chitrapaksha_ayanamsa,
}

AYANAMSA_LABELS = {
    "lahiri":            "Lahiri (IAU Official)",
    "fagan_bradley":     "Fagan-Bradley (Western Sidereal)",
    "krishnamurti":      "Krishnamurti (KP System)",
    "true_chitrapaksha": "True Chitrapaksha (Spica at 180°)",
}

AYANAMSA_EXPLAINERS = {
    "lahiri": (
        "The official Indian government standard, adopted in 1955. Defined by the Sun's position "
        "on the vernal equinox of 285 CE. Most Vedic and Western sidereal astrologers use this. "
        "Best choice if you are new to sidereal astrology."
    ),
    "fagan_bradley": (
        "Developed by Cyril Fagan and Donald Bradley in the 1950s. About 0.9° larger than Lahiri, "
        "placing it slightly earlier in the zodiac. Popular among Western sidereal astrologers who "
        "follow the Babylonian zodiac tradition."
    ),
    "krishnamurti": (
        "Refined by K.S. Krishnamurti for his Krishnamurti Paddhati (KP) system. Nearly identical "
        "to Lahiri but uses a slightly different reference epoch. Preferred by KP practitioners for "
        "precise event timing."
    ),
    "true_chitrapaksha": (
        "Mathematically fixes the star Spica (Chitra) at exactly 180° sidereal longitude. Because "
        "Spica moves slightly, this ayanamsa changes dynamically rather than using a fixed drift rate. "
        "Favored by astrologers who want the zodiac anchored to an actual fixed star."
    ),
}


def compute_ayanamsa(jd, system="lahiri"):
    fn = AYANAMSA_FUNCTIONS.get(system, get_lahiri_ayanamsa)
    return fn(jd)


# ─── Core Helpers ──────────────────────────────────────────────────────────────

def geocode_city(city):
    geolocator = Nominatim(user_agent="sidereal_astrology_v1", timeout=10)
    location = geolocator.geocode(city)
    if not location:
        raise ValueError(f"Could not find location: '{city}'. Try a more specific city name.")
    return location.latitude, location.longitude, location.address


def get_timezone(lat, lon):
    tf = TimezoneFinder()
    tz_str = tf.timezone_at(lat=lat, lng=lon)
    return tz_str or "UTC"


def local_to_utc(date_str, time_str, timezone_str):
    tz = pytz.timezone(timezone_str)
    naive = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
    local = tz.localize(naive, is_dst=None)
    return local.astimezone(pytz.utc)


def tropical_to_sidereal(longitude, ayanamsa):
    return (longitude - ayanamsa) % 360


def longitude_to_sign_and_degree(longitude):
    sign_index = int(longitude / 30) % 12
    degree = longitude % 30
    return SIGNS[sign_index], degree


def get_current_obliquity(jd):
    T = (jd - J2000) / 36525.0
    return 23.439291111 - 0.013004167 * T - 1.638889e-7 * T**2 + 5.036111e-7 * T**3


def calculate_ascendant(ramc_degrees, latitude_deg, obliquity_deg):
    ramc = math.radians(ramc_degrees)
    lat  = math.radians(latitude_deg)
    obl  = math.radians(obliquity_deg)
    y = math.cos(ramc)
    x = -(math.sin(ramc) * math.cos(obl) + math.tan(lat) * math.sin(obl))
    return math.degrees(math.atan2(y, x)) % 360


def calculate_mc(ramc_degrees, obliquity_deg):
    ramc = math.radians(ramc_degrees)
    obl  = math.radians(obliquity_deg)
    return math.degrees(math.atan2(math.sin(ramc), math.cos(ramc) * math.cos(obl))) % 360


def get_whole_sign_house(planet_lon, asc_lon):
    asc_sign_start = int(asc_lon / 30) * 30
    return int((planet_lon - asc_sign_start + 360) % 360 / 30) + 1


def get_ecliptic_longitude(body, observer):
    body.compute(observer)
    ecl = ephem.Ecliptic(body, epoch=observer.date)
    return math.degrees(ecl.lon) % 360


def get_lunar_nodes(jd, ayanamsa):
    T = (jd - J2000) / 36525.0
    omega = (125.0445479
             - 1934.1362608 * T
             + 0.0020754 * T**2
             + T**3 / 467441.0
             - T**4 / 60616000.0) % 360
    rahu_tropical = omega % 360
    ketu_tropical = (omega + 180.0) % 360
    return tropical_to_sidereal(rahu_tropical, ayanamsa), tropical_to_sidereal(ketu_tropical, ayanamsa)


def get_nakshatra(longitude):
    nak_span  = 360.0 / 27.0
    pada_span = nak_span / 4.0
    idx = int(longitude / nak_span) % 27
    pos_in_nak = longitude % nak_span
    pada = int(pos_in_nak / pada_span) + 1
    info = get_nakshatra_info(idx)
    return {
        "index":  idx,
        "name":   info["name"],
        "lord":   info["lord"],
        "symbol": info["symbol"],
        "pada":   pada,
        "pos_in_nak": pos_in_nak,
    }


# ─── Fixed Stars ───────────────────────────────────────────────────────────────

# J2000.0 tropical longitudes in degrees; proper motion ~50.3 arcsec/year = 0.013972 deg/yr
FIXED_STARS = {
    "Algol":      {"lon_j2000": 55.17,  "meaning": "Intense power, transformation, and overcoming adversity"},
    "Aldebaran":  {"lon_j2000": 69.78,  "meaning": "Courage, authority, and worldly success"},
    "Regulus":    {"lon_j2000": 149.83, "meaning": "Royalty, ambition, and sudden rise or fall"},
    "Spica":      {"lon_j2000": 203.83, "meaning": "Gifts, brilliance, and spiritual blessings"},
    "Antares":    {"lon_j2000": 249.77, "meaning": "Passion, intensity, and warrior spirit"},
    "Vega":       {"lon_j2000": 285.32, "meaning": "Charisma, artistic gifts, and magnetism"},
    "Fomalhaut":  {"lon_j2000": 333.87, "meaning": "Vision, idealism, and spiritual aspiration"},
    "Achernar":   {"lon_j2000": 345.32, "meaning": "Success after trials, purification, endings"},
}


def check_fixed_star_conjunctions(placements, jd, ayanamsa, orb=1.0):
    """
    Return list of {planet, star, orb_deg, meaning} for planets within `orb`
    degrees of a major fixed star (sidereal positions compared).
    """
    years_from_j2000 = (jd - J2000) / 365.25
    proper_motion = years_from_j2000 * 0.013972

    results = []
    for star_name, star_data in FIXED_STARS.items():
        star_trop = (star_data["lon_j2000"] + proper_motion) % 360
        star_sid  = tropical_to_sidereal(star_trop, ayanamsa)

        for planet_name, pl in placements.items():
            if planet_name in ("Midheaven",):
                continue
            diff = abs(pl["longitude"] - star_sid)
            if diff > 180:
                diff = 360 - diff
            if diff <= orb:
                results.append({
                    "planet":  planet_name,
                    "symbol":  pl.get("symbol", ""),
                    "star":    star_name,
                    "orb":     round(diff, 2),
                    "meaning": star_data["meaning"],
                })

    results.sort(key=lambda x: x["orb"])
    return results


# ─── Vimshottari Dasha ─────────────────────────────────────────────────────────

DASHA_ORDER = ["Ketu", "Venus", "Sun", "Moon", "Mars", "Rahu", "Jupiter", "Saturn", "Mercury"]
DASHA_YEARS = {"Ketu": 7, "Venus": 20, "Sun": 6, "Moon": 10, "Mars": 7, "Rahu": 18, "Jupiter": 16, "Saturn": 19, "Mercury": 17}
DASHA_TOTAL = 120  # years

# Nakshatra index → dasha lord (repeats every 9 nakshatras)
NAK_LORD_ORDER = ["Ketu", "Venus", "Sun", "Moon", "Mars", "Rahu", "Jupiter", "Saturn", "Mercury"]


def get_vimshottari_dasha(moon_sid_lon, birth_jd):
    """
    Calculate Vimshottari Dasha timeline from sidereal Moon longitude and birth Julian Date.
    Returns: current_maha, current_antar, plus timeline array.
    """
    nak_span  = 360.0 / 27.0
    nak_index = int(moon_sid_lon / nak_span) % 27
    pos_in_nak = moon_sid_lon % nak_span

    first_lord = NAK_LORD_ORDER[nak_index % 9]
    first_dasha_years = DASHA_YEARS[first_lord]
    # How much of the first dasha has already elapsed at birth
    elapsed_fraction  = pos_in_nak / nak_span
    first_balance_yrs = first_dasha_years * (1.0 - elapsed_fraction)

    # Build Maha Dasha timeline starting from birth
    start_lord_idx = DASHA_ORDER.index(first_lord)
    timeline = []
    jd = birth_jd

    for i in range(9):
        lord = DASHA_ORDER[(start_lord_idx + i) % 9]
        if i == 0:
            years = first_balance_yrs
        else:
            years = DASHA_YEARS[lord]
        days  = years * 365.25
        end_jd = jd + days
        timeline.append({
            "lord":    lord,
            "years":   round(years, 2),
            "start_jd": round(jd, 2),
            "end_jd":   round(end_jd, 2),
            "start_date": _jd_to_date_str(jd),
            "end_date":   _jd_to_date_str(end_jd),
        })
        jd = end_jd

    # Extend two more full cycles so we have future coverage
    for cycle in range(1, 3):
        for i in range(9):
            lord = DASHA_ORDER[(start_lord_idx + 1 + i) % 9] if cycle == 1 else DASHA_ORDER[i]
            years = DASHA_YEARS[lord]
            days  = years * 365.25
            end_jd = jd + days
            timeline.append({
                "lord":    lord,
                "years":   round(years, 2),
                "start_jd": round(jd, 2),
                "end_jd":   round(end_jd, 2),
                "start_date": _jd_to_date_str(jd),
                "end_date":   _jd_to_date_str(end_jd),
            })
            jd = end_jd

    # Find current Maha Dasha
    now_jd = ephem.julian_date(datetime.now(timezone.utc).strftime("%Y/%m/%d %H:%M:%S"))
    current_maha = None
    for period in timeline:
        if period["start_jd"] <= now_jd < period["end_jd"]:
            current_maha = period
            break

    # Build Antar Dasha (sub-periods) within current Maha
    current_antar = None
    antar_timeline = []
    if current_maha:
        maha_lord = current_maha["lord"]
        maha_start_jd = current_maha["start_jd"]
        maha_years = current_maha["years"]
        antar_start_idx = DASHA_ORDER.index(maha_lord)
        jd2 = maha_start_jd
        for i in range(9):
            antar_lord = DASHA_ORDER[(antar_start_idx + i) % 9]
            antar_fraction = DASHA_YEARS[antar_lord] / DASHA_TOTAL
            antar_years = maha_years * antar_fraction
            antar_end_jd = jd2 + antar_years * 365.25
            entry = {
                "lord":       antar_lord,
                "years":      round(antar_years, 2),
                "start_date": _jd_to_date_str(jd2),
                "end_date":   _jd_to_date_str(antar_end_jd),
            }
            antar_timeline.append(entry)
            if jd2 <= now_jd < antar_end_jd:
                current_antar = entry
            jd2 = antar_end_jd

    return {
        "current_maha":    current_maha,
        "current_antar":   current_antar,
        "antar_timeline":  antar_timeline,
        "maha_timeline":   timeline[:18],  # show enough for display
    }


def _jd_to_date_str(jd):
    try:
        d = ephem.Date(jd - 2415020.0)  # ephem uses Dublin JD
        dt = d.datetime()
        return dt.strftime("%b %Y")
    except Exception:
        return ""


# ─── Placement Builder ─────────────────────────────────────────────────────────

def _build_placement(planet_name, sid_lon, degree, sign, trop_lon=None):
    nak = get_nakshatra(sid_lon)
    p = {
        "longitude":       round(sid_lon, 4),
        "sign":            sign,
        "degree":          round(degree, 2),
        "symbol":          PLANET_SYMBOLS.get(planet_name, ""),
        "sign_symbol":     SIGN_SYMBOLS.get(sign, ""),
        "meaning":         PLANET_MEANINGS.get(planet_name, ""),
        "interpretation":  get_interpretation(planet_name, sign),
        "nakshatra":       nak["name"],
        "nakshatra_lord":  nak["lord"],
        "nakshatra_pada":  nak["pada"],
        "nakshatra_symbol": nak["symbol"],
    }
    if trop_lon is not None:
        t_sign, t_degree = longitude_to_sign_and_degree(trop_lon % 360)
        p["tropical_sign"]   = t_sign
        p["tropical_degree"] = round(t_degree, 2)
        p["tropical_sign_symbol"] = SIGN_SYMBOLS.get(t_sign, "")
    return p


# ─── Main Chart Calculation ────────────────────────────────────────────────────

def get_chart(name, date_str, time_str, city, ayanamsa_system="lahiri"):
    lat, lon, full_address = geocode_city(city)
    tz_str = get_timezone(lat, lon)
    utc_dt = local_to_utc(date_str, time_str, tz_str)

    observer = ephem.Observer()
    observer.lat       = str(lat)
    observer.lon       = str(lon)
    observer.elevation = 0
    observer.pressure  = 0
    observer.date      = utc_dt.strftime("%Y/%m/%d %H:%M:%S")

    jd        = ephem.julian_date(observer.date)
    ayanamsa  = compute_ayanamsa(jd, ayanamsa_system)
    obliquity = get_current_obliquity(jd)

    planet_classes = [
        ("Sun",     ephem.Sun),
        ("Moon",    ephem.Moon),
        ("Mercury", ephem.Mercury),
        ("Venus",   ephem.Venus),
        ("Mars",    ephem.Mars),
        ("Jupiter", ephem.Jupiter),
        ("Saturn",  ephem.Saturn),
        ("Uranus",  ephem.Uranus),
        ("Neptune", ephem.Neptune),
    ]

    placements = {}
    for planet_name, planet_class in planet_classes:
        body     = planet_class()
        trop_lon = get_ecliptic_longitude(body, observer)
        sid_lon  = tropical_to_sidereal(trop_lon, ayanamsa)
        sign, degree = longitude_to_sign_and_degree(sid_lon)
        placements[planet_name] = _build_placement(planet_name, sid_lon, degree, sign, trop_lon)

    # Rahu & Ketu
    rahu_sid, ketu_sid = get_lunar_nodes(jd, ayanamsa)
    rahu_sign, rahu_deg = longitude_to_sign_and_degree(rahu_sid)
    ketu_sign, ketu_deg = longitude_to_sign_and_degree(ketu_sid)
    placements["Rahu"] = _build_placement("Rahu", rahu_sid, rahu_deg, rahu_sign)
    placements["Ketu"] = _build_placement("Ketu", ketu_sid, ketu_deg, ketu_sign)

    # Ascendant
    ramc_degrees = math.degrees(float(observer.sidereal_time()))
    asc_tropical  = calculate_ascendant(ramc_degrees, lat, obliquity)
    asc_sidereal  = tropical_to_sidereal(asc_tropical, ayanamsa)
    asc_sign, asc_degree = longitude_to_sign_and_degree(asc_sidereal)
    placements["Ascendant"] = _build_placement("Ascendant", asc_sidereal, asc_degree, asc_sign, asc_tropical)
    placements["Ascendant"]["house"] = 1

    # Midheaven (MC)
    mc_tropical = calculate_mc(ramc_degrees, obliquity)
    mc_sidereal = tropical_to_sidereal(mc_tropical, ayanamsa)
    mc_sign, mc_degree = longitude_to_sign_and_degree(mc_sidereal)
    placements["Midheaven"] = _build_placement("Midheaven", mc_sidereal, mc_degree, mc_sign, mc_tropical)
    placements["Midheaven"]["symbol"]  = "MC"
    placements["Midheaven"]["meaning"] = "Career, vocation & public legacy"

    # Whole-sign houses
    asc_lon = placements["Ascendant"]["longitude"]
    for key, pl in placements.items():
        if key != "Ascendant":
            pl["house"] = get_whole_sign_house(pl["longitude"], asc_lon)

    # Derived readings
    career  = get_career_reading(placements)
    romance = get_romance_reading(placements)

    # Dasha system from Moon
    moon_sid = placements["Moon"]["longitude"]
    dasha = get_vimshottari_dasha(moon_sid, jd)

    # Fixed star conjunctions
    fixed_stars = check_fixed_star_conjunctions(placements, jd, ayanamsa)

    # Yoga detection
    yogas = calculate_yogas(placements)

    # Planetary aspects (Graha Drishti)
    aspects = calculate_aspects(placements)

    # Spouse / partner profile
    spouse_profile = calculate_spouse_profile(placements)

    # Special lagnas
    arudha_lagna = calculate_arudha_lagna(placements)
    indu_lagna   = calculate_indu_lagna(placements)

    local_dt = utc_dt.astimezone(pytz.timezone(tz_str))
    return {
        "name":            name or "The Seeker",
        "date":            date_str,
        "time":            time_str,
        "city":            city,
        "full_address":    full_address,
        "latitude":        round(lat, 4),
        "longitude":       round(lon, 4),
        "timezone":        tz_str,
        "local_datetime":  local_dt.strftime("%B %d, %Y at %I:%M %p %Z"),
        "ayanamsa":        round(ayanamsa, 4),
        "ayanamsa_system": ayanamsa_system,
        "ayanamsa_label":  AYANAMSA_LABELS.get(ayanamsa_system, "Lahiri"),
        "placements":      placements,
        "sun_sign":        placements["Sun"]["sign"],
        "moon_sign":       placements["Moon"]["sign"],
        "rising_sign":     placements["Ascendant"]["sign"],
        "mc_sign":         placements["Midheaven"]["sign"],
        "career":          career,
        "romance":         romance,
        "dasha":           dasha,
        "fixed_stars":     fixed_stars,
        "yogas":           yogas,
        "aspects":         aspects,
        "spouse_profile":  spouse_profile,
        "arudha_lagna":    arudha_lagna,
        "indu_lagna":      indu_lagna,
        "ayanamsa_explainers": AYANAMSA_EXPLAINERS,
    }


# ─── Transit Calculation ───────────────────────────────────────────────────────

def get_transits(natal_placements, lat=0.0, lon=0.0, ayanamsa_system="lahiri"):
    now_utc = datetime.now(timezone.utc)

    observer = ephem.Observer()
    observer.lat       = str(lat)
    observer.lon       = str(lon)
    observer.elevation = 0
    observer.pressure  = 0
    observer.date      = now_utc.strftime("%Y/%m/%d %H:%M:%S")

    jd       = ephem.julian_date(observer.date)
    ayanamsa = compute_ayanamsa(jd, ayanamsa_system)
    asc_lon  = natal_placements["Ascendant"]["longitude"]

    planet_classes = [
        ("Sun",     ephem.Sun),
        ("Moon",    ephem.Moon),
        ("Mercury", ephem.Mercury),
        ("Venus",   ephem.Venus),
        ("Mars",    ephem.Mars),
        ("Jupiter", ephem.Jupiter),
        ("Saturn",  ephem.Saturn),
    ]

    transits = {}
    for planet_name, planet_class in planet_classes:
        body     = planet_class()
        trop_lon = get_ecliptic_longitude(body, observer)
        sid_lon  = tropical_to_sidereal(trop_lon, ayanamsa)
        sign, degree = longitude_to_sign_and_degree(sid_lon)
        house = get_whole_sign_house(sid_lon, asc_lon)
        nak   = get_nakshatra(sid_lon)
        transits[planet_name] = {
            "longitude":       round(sid_lon, 4),
            "sign":            sign,
            "sign_symbol":     SIGN_SYMBOLS.get(sign, ""),
            "degree":          round(degree, 2),
            "house":           house,
            "nakshatra":       nak["name"],
            "nakshatra_pada":  nak["pada"],
            "symbol":          PLANET_SYMBOLS.get(planet_name, ""),
            "interpretation":  get_transit_interpretation(planet_name, house),
        }

    # Rahu / Ketu
    rahu_sid, ketu_sid = get_lunar_nodes(jd, ayanamsa)
    for node_name, sid_lon in [("Rahu", rahu_sid), ("Ketu", ketu_sid)]:
        sign, degree = longitude_to_sign_and_degree(sid_lon)
        house = get_whole_sign_house(sid_lon, asc_lon)
        nak   = get_nakshatra(sid_lon)
        transits[node_name] = {
            "longitude":       round(sid_lon, 4),
            "sign":            sign,
            "sign_symbol":     SIGN_SYMBOLS.get(sign, ""),
            "degree":          round(degree, 2),
            "house":           house,
            "nakshatra":       nak["name"],
            "nakshatra_pada":  nak["pada"],
            "symbol":          PLANET_SYMBOLS.get(node_name, ""),
            "interpretation":  get_transit_interpretation(node_name, house),
        }

    # Today's Moon nakshatra for the tracker
    moon_nak = get_nakshatra(transits["Moon"]["longitude"])

    daily_keys   = ["Moon", "Sun"]
    monthly_keys = ["Mercury", "Venus", "Mars"]
    yearly_keys  = ["Jupiter", "Saturn", "Rahu", "Ketu"]

    return {
        "date":        now_utc.strftime("%B %d, %Y"),
        "transits":    transits,
        "daily":       {k: transits[k] for k in daily_keys   if k in transits},
        "monthly":     {k: transits[k] for k in monthly_keys if k in transits},
        "yearly":      {k: transits[k] for k in yearly_keys  if k in transits},
        "moon_nakshatra": moon_nak,
    }


def get_today_moon_nakshatra(offset_days=0):
    """Standalone: returns today's (or tomorrow's) Moon nakshatra for the daily tracker."""
    import datetime as _dt
    now_utc = datetime.now(timezone.utc) + _dt.timedelta(days=offset_days)
    observer = ephem.Observer()
    observer.lat = "0"; observer.lon = "0"
    observer.elevation = 0; observer.pressure = 0
    observer.date = now_utc.strftime("%Y/%m/%d %H:%M:%S")
    jd = ephem.julian_date(observer.date)
    ayanamsa = get_lahiri_ayanamsa(jd)
    moon = ephem.Moon()
    trop_lon = get_ecliptic_longitude(moon, observer)
    sid_lon  = tropical_to_sidereal(trop_lon, ayanamsa)
    nak = get_nakshatra(sid_lon)
    sign, _ = longitude_to_sign_and_degree(sid_lon)
    return {"nakshatra": nak, "sign": sign, "longitude": round(sid_lon, 4)}


# ─── Yoga Detection ────────────────────────────────────────────────────────────

# Vedic sign rulerships
_SIGN_LORDS = {
    "Aries": "Mars",    "Taurus": "Venus",   "Gemini": "Mercury",
    "Cancer": "Moon",   "Leo": "Sun",        "Virgo": "Mercury",
    "Libra": "Venus",   "Scorpio": "Mars",   "Sagittarius": "Jupiter",
    "Capricorn": "Saturn", "Aquarius": "Saturn", "Pisces": "Jupiter",
}
_KENDRA  = {1, 4, 7, 10}
_TRIKONA = {1, 5, 9}


def calculate_yogas(placements):
    """
    Detect Vedic yogas from whole-sign house placements.
    Returns list of dicts with full yoga data + detected metadata.
    """
    sign_idx = {s: i for i, s in enumerate(SIGNS)}

    def planet_sign(name):
        return placements[name]["sign"] if name in placements else None

    def planet_house(name):
        return placements[name].get("house", 0) if name in placements else 0

    def house_lord(n):
        """Return the planet ruling whole-sign house n from the Ascendant."""
        asc_sign = placements["Ascendant"]["sign"]
        idx = (sign_idx.get(asc_sign, 0) + n - 1) % 12
        return _SIGN_LORDS[SIGNS[idx]]

    found_names = []

    def add(name):
        if name not in found_names and name in YOGA_DATA:
            found_names.append(name)

    # ── Pancha Mahapurusha Yogas ──────────────────────────────────────────────
    MAHAPURUSHA = {
        "Mars":    {"own": {"Aries", "Scorpio"},          "exalt": {"Capricorn"}, "yoga": "Ruchaka Yoga"},
        "Mercury": {"own": {"Gemini", "Virgo"},           "exalt": {"Virgo"},     "yoga": "Bhadra Yoga"},
        "Jupiter": {"own": {"Sagittarius", "Pisces"},     "exalt": {"Cancer"},    "yoga": "Hamsa Yoga"},
        "Venus":   {"own": {"Taurus", "Libra"},           "exalt": {"Pisces"},    "yoga": "Malavya Yoga"},
        "Saturn":  {"own": {"Capricorn", "Aquarius"},     "exalt": {"Libra"},     "yoga": "Sasa Yoga"},
    }
    for planet, data in MAHAPURUSHA.items():
        s = planet_sign(planet)
        h = planet_house(planet)
        if s and h in _KENDRA and (s in data["own"] or s in data["exalt"]):
            add(data["yoga"])

    # ── Gaja Kesari Yoga (Jupiter in kendra from Moon) ────────────────────────
    moon_h = planet_house("Moon")
    jup_h  = planet_house("Jupiter")
    if moon_h and jup_h and (jup_h - moon_h) % 12 in {0, 3, 6, 9}:
        add("Gaja Kesari Yoga")

    # ── Budha Aditya Yoga (Sun + Mercury same sign) ───────────────────────────
    if planet_sign("Sun") and planet_sign("Sun") == planet_sign("Mercury"):
        add("Budha Aditya Yoga")

    # ── Chandra Mangala Yoga (Moon + Mars conjunct in same sign) ─────────────
    if planet_sign("Moon") and planet_sign("Moon") == planet_sign("Mars"):
        add("Chandra Mangala Yoga")

    # ── Vesi Yoga (a planet other than Moon in 2nd from Sun) ─────────────────
    sun_h = planet_house("Sun")
    if sun_h:
        second_sun = sun_h % 12 + 1
        for p in placements:
            if p not in ("Sun", "Moon", "Ascendant", "Midheaven") and planet_house(p) == second_sun:
                add("Vesi Yoga")
                break

    # ── Kemadruma Yoga (no planet in 2nd or 12th from Moon) ──────────────────
    if moon_h:
        adj1 = moon_h % 12 + 1
        adj2 = (moon_h - 2) % 12 + 1
        neighbors = False
        for p in placements:
            if p in ("Ascendant", "Midheaven", "Rahu", "Ketu"):
                continue
            if planet_house(p) in {adj1, adj2, moon_h} and p != "Moon":
                neighbors = True
                break
        if not neighbors:
            add("Kemadruma Yoga")

    # ── Parivartana Yoga (mutual sign exchange between two planets) ───────────
    planets_for_ex = [p for p in placements if p not in ("Ascendant", "Midheaven", "Rahu", "Ketu")]
    for p1 in planets_for_ex:
        s1 = planet_sign(p1)
        if not s1:
            continue
        lord1 = _SIGN_LORDS.get(s1)
        if not lord1 or lord1 == p1:
            continue
        s2 = planet_sign(lord1)
        if s2 and _SIGN_LORDS.get(s2) == p1:
            add("Parivartana Yoga")
            break

    # ── Neecha Bhanga Raja Yoga (debilitated planet, debilitation cancelled) ──
    DEBILITATED = {
        "Sun": "Libra",  "Moon": "Scorpio", "Mars": "Cancer",
        "Mercury": "Pisces", "Jupiter": "Capricorn", "Venus": "Virgo", "Saturn": "Aries",
    }
    DEBI_CANCEL_LORD = {
        "Sun": "Venus", "Moon": "Mars", "Mars": "Moon",
        "Mercury": "Jupiter", "Jupiter": "Saturn", "Venus": "Mercury", "Saturn": "Mars",
    }
    for planet, debi_sign in DEBILITATED.items():
        if planet_sign(planet) == debi_sign:
            cancel = DEBI_CANCEL_LORD.get(planet)
            if cancel and planet_house(cancel) in _KENDRA:
                add("Neecha Bhanga Raja Yoga")
                break

    # ── Dharma Karma Adhipati Yoga (9th + 10th lords conjunct/exchange) ───────
    l9  = house_lord(9)
    l10 = house_lord(10)
    if l9 != l10:
        if planet_sign(l9) == planet_sign(l10):   # conjunct
            add("Dharma Karma Adhipati Yoga")
        elif planet_house(l9) == planet_house(l10):  # same house
            add("Dharma Karma Adhipati Yoga")
        elif _SIGN_LORDS.get(planet_sign(l9)) == l10 and _SIGN_LORDS.get(planet_sign(l10)) == l9:  # exchange
            add("Dharma Karma Adhipati Yoga")

    # ── Viparita Raja Yoga (lords of 6/8/12 in each other's dusthana houses) ──
    l6  = house_lord(6)
    l8  = house_lord(8)
    l12 = house_lord(12)
    dusthana = {6, 8, 12}
    vip_count = sum(1 for el in (l6, l8, l12) if planet_house(el) in dusthana)
    if vip_count >= 2:
        add("Viparita Raja Yoga")

    # ── Adhi Yoga (2+ of Jupiter/Venus/Mercury in 6th, 7th, 8th from Moon) ───
    if moon_h:
        houses_678 = {(moon_h + i - 1) % 12 + 1 for i in (5, 6, 7)}
        benefics_there = [p for p in ("Jupiter", "Venus", "Mercury") if planet_house(p) in houses_678]
        if len(benefics_there) >= 2:
            add("Adhi Yoga")

    # ── Amala Yoga (only benefics in 10th from Lagna) ────────────────────────
    tenth_occupants = [p for p in placements
                       if p not in ("Ascendant", "Midheaven") and planet_house(p) == 10]
    benefic_set = {"Jupiter", "Venus", "Mercury", "Moon"}
    if tenth_occupants and all(p in benefic_set for p in tenth_occupants):
        add("Amala Yoga")

    # ── Shubha Kartari Yoga (benefics in 2nd AND 12th from Lagna) ────────────
    has_2nd_benefic  = any(p in benefic_set and planet_house(p) == 2  for p in placements)
    has_12th_benefic = any(p in benefic_set and planet_house(p) == 12 for p in placements)
    if has_2nd_benefic and has_12th_benefic:
        add("Shubha Kartari Yoga")

    # ── Kesari Yoga (Jupiter in kendra from Lagna) ────────────────────────────
    if planet_house("Jupiter") in _KENDRA:
        add("Kesari Yoga")

    # ── Saraswati Yoga (Jupiter+Venus+Mercury all in kendra/trikona/2nd, Jupiter strong) ──
    good_h = _KENDRA | _TRIKONA | {2}
    jup_strong = planet_sign("Jupiter") in {"Sagittarius", "Pisces", "Cancer"}
    if (planet_house("Jupiter") in good_h and planet_house("Venus") in good_h
            and planet_house("Mercury") in good_h and jup_strong):
        add("Saraswati Yoga")

    # ── Sunapha Yoga (planet other than Sun in 2nd from Moon) ────────────────
    if moon_h:
        second_from_moon = moon_h % 12 + 1
        for p in placements:
            if p not in ("Sun", "Moon", "Ascendant", "Midheaven") and planet_house(p) == second_from_moon:
                add("Sunapha Yoga")
                break

    # ── Anapha Yoga (planet other than Sun in 12th from Moon) ────────────────
    if moon_h:
        twelfth_from_moon = (moon_h - 2) % 12 + 1
        for p in placements:
            if p not in ("Sun", "Moon", "Ascendant", "Midheaven") and planet_house(p) == twelfth_from_moon:
                add("Anapha Yoga")
                break

    # ── Durudhara Yoga (planets both 2nd AND 12th from Moon) ─────────────────
    if moon_h:
        h2  = moon_h % 12 + 1
        h12 = (moon_h - 2) % 12 + 1
        non_luminary = [p for p in placements if p not in ("Sun", "Moon", "Ascendant", "Midheaven")]
        has_2nd  = any(planet_house(p) == h2  for p in non_luminary)
        has_12th = any(planet_house(p) == h12 for p in non_luminary)
        if has_2nd and has_12th:
            add("Durudhara Yoga")

    # ── Vasumati Yoga (Jupiter+Venus+Mercury all in upachaya from Moon/Lagna) ─
    upachaya = {3, 6, 10, 11}
    benefics_up_moon  = moon_h and all((planet_house(p) - moon_h) % 12 + 1 in upachaya for p in ("Jupiter", "Venus", "Mercury"))
    benefics_up_lagna = all(planet_house(p) in upachaya for p in ("Jupiter", "Venus", "Mercury"))
    if benefics_up_moon or benefics_up_lagna:
        add("Vasumati Yoga")

    # ── Lakshmi Yoga (9th lord in own/exalt sign AND in kendra/trikona) ───────
    l9 = house_lord(9)
    l9_sign = planet_sign(l9)
    _OWN_SIGNS = {
        "Sun": {"Leo"}, "Moon": {"Cancer"}, "Mars": {"Aries", "Scorpio"},
        "Mercury": {"Gemini", "Virgo"}, "Jupiter": {"Sagittarius", "Pisces"},
        "Venus": {"Taurus", "Libra"}, "Saturn": {"Capricorn", "Aquarius"},
    }
    _EXALT_SIGNS = {
        "Sun": "Aries", "Moon": "Taurus", "Mars": "Capricorn",
        "Mercury": "Virgo", "Jupiter": "Cancer", "Venus": "Pisces", "Saturn": "Libra",
    }
    l9_strong = (l9_sign in _OWN_SIGNS.get(l9, set()) or l9_sign == _EXALT_SIGNS.get(l9))
    if l9_strong and planet_house(l9) in (_KENDRA | _TRIKONA):
        add("Lakshmi Yoga")

    # ── Guru Mangala Yoga (Jupiter and Mars conjunct or mutual 7th) ───────────
    jup_h2 = planet_house("Jupiter")
    mar_h  = planet_house("Mars")
    if jup_h2 and mar_h:
        if jup_h2 == mar_h or abs(jup_h2 - mar_h) == 6:
            add("Guru Mangala Yoga")

    # ── Shakata Yoga (Jupiter in 6/8/12 from Moon) ────────────────────────────
    if moon_h and jup_h:
        offset_from_moon = (jup_h - moon_h) % 12
        if offset_from_moon in {5, 7, 11}:   # 6th=5, 8th=7, 12th=11 (0-indexed diff)
            add("Shakata Yoga")

    # ── Chamara Yoga (Asc lord exalted + conjunct Jupiter, or Jupiter in Asc/7th) ──
    asc_lord = _SIGN_LORDS.get(placements.get("Ascendant", {}).get("sign", ""), "")
    asc_lord_exalted = asc_lord and planet_sign(asc_lord) == _EXALT_SIGNS.get(asc_lord)
    asc_lord_with_jup = asc_lord and planet_sign(asc_lord) == planet_sign("Jupiter")
    jup_in_1_or_7 = planet_house("Jupiter") in {1, 7}
    if (asc_lord_exalted and asc_lord_with_jup) or jup_in_1_or_7:
        add("Chamara Yoga")

    # ── Kahala Yoga (4th lord + 9th lord in mutual kendra + Asc lord strong) ──
    l4  = house_lord(4)
    l9b = house_lord(9)
    if l4 != l9b:
        diff_kah = abs(planet_house(l4) - planet_house(l9b))
        mutual_kendra = diff_kah in {0, 3, 6, 9}
        asc_l = house_lord(1)
        asc_strong = planet_house(asc_l) in (_KENDRA | _TRIKONA)
        if mutual_kendra and asc_strong:
            add("Kahala Yoga")

    # ── Nipuna Yoga (Mercury exalted or own sign, aspects/conjoins Ascendant) ──
    merc_sign = planet_sign("Mercury")
    merc_strong = merc_sign in {"Gemini", "Virgo"}
    merc_h = planet_house("Mercury")
    merc_near_asc = merc_h in {1, 7}   # conjunct or 7th aspect to Lagna
    if merc_strong and merc_near_asc:
        add("Nipuna Yoga")

    # ── Pushkala Yoga (Moon in friendly/own sign, lord in kendra, Asc lord strong) ──
    _FRIENDLY = {
        "Moon": {"Cancer", "Taurus", "Pisces", "Sagittarius"},
    }
    moon_sign = planet_sign("Moon")
    moon_friendly = moon_sign in _FRIENDLY["Moon"]
    moon_lord = _SIGN_LORDS.get(moon_sign, "")
    moon_lord_kendra = moon_lord and planet_house(moon_lord) in _KENDRA
    asc_l2 = house_lord(1)
    asc_strong2 = planet_house(asc_l2) in (_KENDRA | _TRIKONA)
    if moon_friendly and moon_lord_kendra and asc_strong2:
        add("Pushkala Yoga")

    # Build output with full YOGA_DATA content
    result = []
    for name in found_names:
        entry = {"name": name}
        entry.update(YOGA_DATA[name])
        result.append(entry)

    return result


# ─── Graha Drishti (Aspect) Calculation ────────────────────────────────────────

# Special aspect offsets (house-distance from occupying house)
_ASPECT_OFFSETS = {
    "Sun":     [7],
    "Moon":    [7],
    "Mercury": [7],
    "Venus":   [7],
    "Mars":    [4, 7, 8],
    "Jupiter": [5, 7, 9],
    "Saturn":  [3, 7, 10],
    "Rahu":    [5, 7, 9],
    "Ketu":    [5, 7, 9],
}

# Approximate strength of each aspect by house-offset
_ASPECT_STRENGTH = {3: 0.25, 4: 0.75, 5: 0.5, 7: 1.0, 8: 0.75, 9: 0.75, 10: 0.75}

# Nature of planets
_PLANET_NATURE = {
    "Sun": "neutral", "Moon": "benefic", "Mercury": "neutral",
    "Venus": "benefic", "Jupiter": "benefic",
    "Mars": "malefic", "Saturn": "malefic",
    "Rahu": "malefic", "Ketu": "spiritual",
}


def calculate_aspects(placements):
    """
    Compute Graha Drishti (Vedic planetary aspects) using whole-sign houses.
    Returns list of aspect dicts with interpretation and strength.
    """
    # Build house → [planet_names] map
    house_planets = {}
    for p, data in placements.items():
        if p in ("Ascendant", "Midheaven"):
            continue
        h = data.get("house", 0)
        if h:
            house_planets.setdefault(h, []).append(p)

    aspects = []
    seen = set()  # avoid duplicates from bidirectional interpretations

    for from_planet, offsets in _ASPECT_OFFSETS.items():
        if from_planet not in placements:
            continue
        from_h = placements[from_planet].get("house", 0)
        if not from_h:
            continue

        for offset in offsets:
            target_h = (from_h + offset - 2) % 12 + 1
            for to_planet in house_planets.get(target_h, []):
                if to_planet == from_planet:
                    continue
                key = tuple(sorted([from_planet, to_planet]))
                # Allow same pair at different offsets/aspects
                full_key = (from_planet, to_planet, offset)
                if full_key in seen:
                    continue
                seen.add(full_key)

                strength = _ASPECT_STRENGTH.get(offset, 0.5)
                aspect_label = {
                    7: "7th Aspect (Opposition)",
                    4: "4th Aspect (Square)",
                    8: "8th Aspect (Trine)",
                    5: "5th Aspect (Trine)",
                    9: "9th Aspect (Trine)",
                    3: "3rd Aspect (Sextile)",
                    10: "10th Aspect (Square)",
                }.get(offset, f"{offset}th Aspect")

                interp = get_aspect_interpretation(from_planet, to_planet, offset)
                nature_from = _PLANET_NATURE.get(from_planet, "neutral")
                nature_to   = _PLANET_NATURE.get(to_planet, "neutral")

                aspects.append({
                    "from_planet":    from_planet,
                    "from_symbol":    placements[from_planet].get("symbol", ""),
                    "from_house":     from_h,
                    "from_sign":      placements[from_planet].get("sign", ""),
                    "to_planet":      to_planet,
                    "to_symbol":      placements[to_planet].get("symbol", ""),
                    "to_house":       target_h,
                    "to_sign":        placements[to_planet].get("sign", ""),
                    "aspect_offset":  offset,
                    "aspect_label":   aspect_label,
                    "strength":       strength,
                    "nature_from":    nature_from,
                    "nature_to":      nature_to,
                    "interpretation": interp,
                })

    # Sort by strength descending then alphabetically
    aspects.sort(key=lambda a: (-a["strength"], a["from_planet"]))
    return aspects

# ─── Spouse / Partner Profile ──────────────────────────────────────────────────

def calculate_spouse_profile(placements):
    """
    Derive the ideal spouse/partner profile from Vedic chart indicators:
      • 7th house (sign on cusp, occupants)
      • 7th house lord (planet, placement, dignity)
      • Venus (natural karaka of love)
      • Jupiter (karaka for husband in female charts)
      • Darakaraka (Jaimini — planet at lowest degree)
    Returns a structured dict for front-end rendering.
    """
    sign_idx = {s: i for i, s in enumerate(SIGNS)}

    def p_sign(name):
        return placements.get(name, {}).get("sign")

    def p_house(name):
        return placements.get(name, {}).get("house", 0)

    def p_deg(name):
        return placements.get(name, {}).get("degree", 0)

    # ── 7th house sign ────────────────────────────────────────────────────────
    asc_sign = placements.get("Ascendant", {}).get("sign", "Aries")
    asc_idx   = sign_idx.get(asc_sign, 0)
    seventh_sign = SIGNS[(asc_idx + 6) % 12]

    # ── 7th house lord ────────────────────────────────────────────────────────
    seventh_lord = _SIGN_LORDS.get(seventh_sign, "Venus")
    sl_sign  = p_sign(seventh_lord)
    sl_house = p_house(seventh_lord)

    # Dignity of 7th lord
    exalt = {"Sun": "Aries", "Moon": "Taurus", "Mars": "Capricorn",
             "Mercury": "Virgo", "Jupiter": "Cancer", "Venus": "Pisces", "Saturn": "Libra"}
    debi  = {"Sun": "Libra", "Moon": "Scorpio", "Mars": "Cancer",
             "Mercury": "Pisces", "Jupiter": "Capricorn", "Venus": "Virgo", "Saturn": "Aries"}
    own   = {"Sun": {"Leo"}, "Moon": {"Cancer"}, "Mars": {"Aries", "Scorpio"},
             "Mercury": {"Gemini", "Virgo"}, "Jupiter": {"Sagittarius", "Pisces"},
             "Venus": {"Taurus", "Libra"}, "Saturn": {"Capricorn", "Aquarius"}}
    if sl_sign == exalt.get(seventh_lord):
        sl_dignity = "exalted"
    elif sl_sign == debi.get(seventh_lord):
        sl_dignity = "debilitated"
    elif sl_sign in own.get(seventh_lord, set()):
        sl_dignity = "own sign"
    else:
        sl_dignity = "neutral"

    # ── Planets in 7th house ──────────────────────────────────────────────────
    seventh_occupants = [p for p, d in placements.items()
                         if p not in ("Ascendant", "Midheaven") and d.get("house") == 7]

    # ── Venus placement ───────────────────────────────────────────────────────
    venus_sign  = p_sign("Venus") or "Libra"
    venus_house = p_house("Venus")
    venus_nak   = placements.get("Venus", {}).get("nakshatra", "")

    # ── Darakaraka (Jaimini: planet at lowest degree, excl. Rahu/Ketu) ────────
    eligible = {p: p_deg(p) for p in ("Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn")
                if p in placements}
    darakaraka = min(eligible, key=eligible.get) if eligible else "Venus"
    dk_sign  = p_sign(darakaraka) or "Unknown"
    dk_house = p_house(darakaraka)

    # ── Pull interpretations ──────────────────────────────────────────────────
    qualities   = SPOUSE_SIGN_QUALITIES.get(seventh_sign, {})
    lord_in_h   = SEVENTH_LORD_IN_HOUSE.get(sl_house, "")
    venus_love  = VENUS_SIGN_LOVE.get(venus_sign, "")

    # ── Influencing planets on 7th: any planet aspecting house 7 ─────────────
    influencers = []
    for p, offsets in _ASPECT_OFFSETS.items():
        if p not in placements:
            continue
        ph = p_house(p)
        if not ph:
            continue
        for off in offsets:
            tgt = (ph + off - 2) % 12 + 1
            if tgt == 7 and p not in seventh_occupants:
                influencers.append(p)
                break

    # ── Strength summary ──────────────────────────────────────────────────────
    strength_score = 0
    if sl_dignity == "exalted":       strength_score = 3
    elif sl_dignity == "own sign":    strength_score = 2
    elif sl_dignity == "neutral":     strength_score = 1
    elif sl_dignity == "debilitated": strength_score = 0

    benefic_inf = [p for p in influencers if _PLANET_NATURE.get(p) == "benefic"]
    malefic_inf = [p for p in influencers if _PLANET_NATURE.get(p) == "malefic"]
    strength_score += len(benefic_inf) - len(malefic_inf)
    if sl_house in _KENDRA | _TRIKONA:
        strength_score += 1

    if strength_score >= 4:    strength_label = "Very Strong"
    elif strength_score >= 2:  strength_label = "Strong"
    elif strength_score >= 0:  strength_label = "Moderate"
    else:                      strength_label = "Challenged"

    return {
        "seventh_sign":       seventh_sign,
        "seventh_lord":       seventh_lord,
        "seventh_lord_sign":  sl_sign,
        "seventh_lord_house": sl_house,
        "seventh_lord_dignity": sl_dignity,
        "seventh_occupants":  seventh_occupants,
        "venus_sign":         venus_sign,
        "venus_house":        venus_house,
        "venus_nakshatra":    venus_nak,
        "darakaraka":         darakaraka,
        "darakaraka_sign":    dk_sign,
        "darakaraka_house":   dk_house,
        "partner_personality":  qualities.get("personality", ""),
        "partner_traits":       qualities.get("traits", []),
        "partner_appearance":   qualities.get("appearance", ""),
        "partner_meeting":      qualities.get("meeting", ""),
        "partner_challenges":   qualities.get("challenges", ""),
        "lord_placement_meaning": lord_in_h,
        "venus_love_style":    venus_love,
        "influencers":         influencers,
        "benefic_influences":  benefic_inf,
        "malefic_influences":  malefic_inf,
        "relationship_strength": strength_label,
    }


# ─── Arudha Lagna ──────────────────────────────────────────────────────────────

def calculate_arudha_lagna(placements):
    """
    Arudha Lagna (AL / Pada Lagna) — the sign that reflects how the world
    perceives you and the material manifestation of your personality.

    Algorithm (classical Parashari):
      1. Find the Ascendant sign and its lord.
      2. Count how many signs the lord is FROM the Ascendant (call it N).
      3. Count N signs FROM the lord. That gives the raw AL sign.
      4. Special rules:
           - If raw AL == Ascendant sign  → shift to the 10th from Ascendant.
           - If raw AL == 7th from Ascendant → shift to the 4th from Ascendant.
    """
    sign_idx = {s: i for i, s in enumerate(SIGNS)}

    asc_sign  = placements.get("Ascendant", {}).get("sign", "Aries")
    asc_idx   = sign_idx.get(asc_sign, 0)

    lord_name = _SIGN_LORDS.get(asc_sign, "Mars")
    lord_data = placements.get(lord_name, {})
    lord_sign = lord_data.get("sign", asc_sign)
    lord_idx  = sign_idx.get(lord_sign, asc_idx)

    # Number of signs from Ascendant to lord (1-based, so same sign = 1)
    n = (lord_idx - asc_idx) % 12 + 1

    # Raw AL: count n signs from the lord
    raw_al_idx = (lord_idx + n - 1) % 12
    raw_al_sign = SIGNS[raw_al_idx]

    # Correction rule 1 – AL falls in lagna sign
    if raw_al_idx == asc_idx:
        al_idx  = (asc_idx + 9) % 12       # 10th from lagna
    # Correction rule 2 – AL falls in 7th from lagna
    elif raw_al_idx == (asc_idx + 6) % 12:
        al_idx  = (asc_idx + 3) % 12       # 4th from lagna
    else:
        al_idx  = raw_al_idx

    al_sign  = SIGNS[al_idx]
    al_house = (al_idx - asc_idx) % 12 + 1  # house number from lagna

    lord_house = placements.get(lord_name, {}).get("house", 0)

    return {
        "sign":       al_sign,
        "house":      al_house,
        "lord":       lord_name,
        "lord_sign":  lord_sign,
        "lord_house": lord_house,
    }


# ─── Indu Lagna ────────────────────────────────────────────────────────────────

# Classical Indu Lagna planet-values (Saptarishi / Parashari tradition)
_INDU_VALUES = {
    "Sun": 30, "Moon": 16, "Mars": 6, "Mercury": 8,
    "Jupiter": 10, "Venus": 12, "Saturn": 1,
    "Rahu": 0,  "Ketu": 0,
}

def calculate_indu_lagna(placements):
    """
    Indu Lagna — the special prosperity / wealth lagna.

    Algorithm:
      1. Find the lord of the 9th house from the Ascendant; note its Indu value.
      2. Find the lord of the 9th house from the Moon; note its Indu value.
      3. Sum = value1 + value2.
      4. Remainder = Sum % 12  (use 12 if remainder == 0).
      5. Count 'remainder' signs from the Moon sign. That is the Indu Lagna.
    """
    sign_idx = {s: i for i, s in enumerate(SIGNS)}

    asc_sign  = placements.get("Ascendant", {}).get("sign", "Aries")
    moon_sign = placements.get("Moon",      {}).get("sign", "Aries")

    asc_idx   = sign_idx.get(asc_sign,  0)
    moon_idx  = sign_idx.get(moon_sign, 0)

    # 9th sign from Ascendant & from Moon (0-based offset = 8)
    ninth_from_asc  = SIGNS[(asc_idx  + 8) % 12]
    ninth_from_moon = SIGNS[(moon_idx + 8) % 12]

    lord_asc  = _SIGN_LORDS.get(ninth_from_asc,  "Jupiter")
    lord_moon = _SIGN_LORDS.get(ninth_from_moon, "Jupiter")

    val1 = _INDU_VALUES.get(lord_asc,  0)
    val2 = _INDU_VALUES.get(lord_moon, 0)

    total     = val1 + val2
    remainder = total % 12 or 12       # 0 → 12

    il_idx  = (moon_idx + remainder - 1) % 12
    il_sign = SIGNS[il_idx]
    il_house = (il_idx - asc_idx) % 12 + 1  # house from lagna

    return {
        "sign":            il_sign,
        "house":           il_house,
        "ninth_lord_asc":  lord_asc,
        "ninth_lord_moon": lord_moon,
        "val_asc":         val1,
        "val_moon":        val2,
        "total":           total,
        "remainder":       remainder,
    }


# ─── D9 Navamsa Chart ──────────────────────────────────────────────────────────

# Navamsa starting sign by D1 sign index (0=Aries … 11=Pisces)
_NAV_START = {
    0: 0,   # Aries      → Aries
    1: 9,   # Taurus     → Capricorn
    2: 6,   # Gemini     → Libra
    3: 3,   # Cancer     → Cancer
    4: 0,   # Leo        → Aries
    5: 9,   # Virgo      → Capricorn
    6: 6,   # Libra      → Libra
    7: 3,   # Scorpio    → Cancer
    8: 0,   # Sagittarius→ Aries
    9: 9,   # Capricorn  → Capricorn
    10: 6,  # Aquarius   → Libra
    11: 3,  # Pisces     → Cancer
}

_NAV_SPAN = 30.0 / 9.0   # 3°20' per navamsa


def longitude_to_navamsa(longitude):
    """Return (d9_sign, d9_degree, d9_sign_index) for a sidereal longitude."""
    sign_idx    = int(longitude / 30) % 12
    pos_in_sign = longitude % 30
    nav_num     = int(pos_in_sign / _NAV_SPAN)       # 0–8
    nav_start   = _NAV_START[sign_idx]
    d9_idx      = (nav_start + nav_num) % 12
    d9_sign     = SIGNS[d9_idx]
    # Project position within this navamsa to a 0–30° scale
    pos_in_nav  = pos_in_sign % _NAV_SPAN
    d9_degree   = round((pos_in_nav / _NAV_SPAN) * 30, 2)
    return d9_sign, d9_degree, d9_idx


def get_chara_karakas(placements):
    """
    Jaimini Chara Karakas ranked by descending degree within sign.
    Returns dict: AK→planet, AmK→planet … DK→planet (7 karakas).
    """
    seven = ["Sun", "Moon", "Mercury", "Venus", "Mars", "Jupiter", "Saturn"]
    ranked = sorted(
        [(p, placements[p].get("degree", 0)) for p in seven if p in placements],
        key=lambda x: x[1],
        reverse=True,
    )
    labels = ["AK", "AmK", "BK", "MK", "PiK", "PuK", "DK"]
    return {labels[i]: planet for i, (planet, _) in enumerate(ranked) if i < len(labels)}


def get_navamsa_chart(placements):
    """
    Calculate the D9 Navamsa chart from a set of sidereal D1 placements.
    Returns a dict of navamsa placements keyed by planet name.
    """
    from interpretations import (
        NAVAMSA_LAGNA_INTERP, NAVAMSA_VENUS_INTERP, NAVAMSA_7TH_SIGN_INTERP, DARAKARAKA_INTERP,
        NAVAMSA_MOON_INTERP, NAVAMSA_MARS_INTERP, NAVAMSA_JUPITER_INTERP,
        VARGOTTAMA_INTERP, D9_ELEMENT_INTERP,
    )

    navamsa = {}
    for planet_name, pl in placements.items():
        lon         = pl["longitude"]
        d9_sign, d9_degree, d9_idx = longitude_to_navamsa(lon)
        # Use pseudo-longitude for nakshatra within D9
        d9_pseudo_lon = d9_idx * 30 + d9_degree
        nak = get_nakshatra(d9_pseudo_lon)
        navamsa[planet_name] = {
            "planet":         planet_name,
            "symbol":         pl.get("symbol", PLANET_SYMBOLS.get(planet_name, "")),
            "d1_sign":        pl.get("sign", ""),
            "d1_degree":      round(pl.get("degree", 0), 2),
            "d1_sign_symbol": pl.get("sign_symbol", SIGN_SYMBOLS.get(pl.get("sign", ""), "")),
            "d9_sign":        d9_sign,
            "d9_degree":      d9_degree,
            "d9_sign_symbol": SIGN_SYMBOLS.get(d9_sign, ""),
            "d9_sign_idx":    d9_idx,
            "nakshatra":      nak["name"],
            "nakshatra_lord": nak["lord"],
            "nakshatra_pada": nak["pada"],
        }

    # D9 houses (whole sign from D9 Ascendant)
    if "Ascendant" in navamsa:
        d9_asc_idx = navamsa["Ascendant"]["d9_sign_idx"]
        for nav_pl in navamsa.values():
            nav_pl["d9_house"] = (nav_pl["d9_sign_idx"] - d9_asc_idx) % 12 + 1

    # ── Marriage indicators ──────────────────────────────────────────────────
    d9_lagna_sign = navamsa.get("Ascendant", {}).get("d9_sign", "Aries")
    d9_lagna_idx  = navamsa.get("Ascendant", {}).get("d9_sign_idx", 0)

    # 7th from D9 lagna
    d9_7th_sign = SIGNS[(d9_lagna_idx + 6) % 12]

    # Venus in D9
    d9_venus_sign = navamsa.get("Venus", {}).get("d9_sign", "")

    # Chara karakas
    karakas = get_chara_karakas(placements)
    dk_planet = karakas.get("DK", "Venus")
    ak_planet = karakas.get("AK", "Sun")

    dk_d9_sign = navamsa.get(dk_planet, {}).get("d9_sign", "")
    ak_d9_sign = navamsa.get(ak_planet, {}).get("d9_sign", "")

    # 7th lord of D9
    d9_7th_lord = _SIGN_LORDS.get(d9_7th_sign, "Venus")
    d9_7th_lord_sign = navamsa.get(d9_7th_lord, {}).get("d9_sign", "")
    d9_7th_lord_house = navamsa.get(d9_7th_lord, {}).get("d9_house", 0)

    # ── Vargottama: planets where D1 sign == D9 sign ─────────────────────────
    _SIGN_ELEMENTS = {
        "Aries": "Fire", "Leo": "Fire", "Sagittarius": "Fire",
        "Taurus": "Earth", "Virgo": "Earth", "Capricorn": "Earth",
        "Gemini": "Air", "Libra": "Air", "Aquarius": "Air",
        "Cancer": "Water", "Scorpio": "Water", "Pisces": "Water",
    }
    vargottama_planets = []
    for pname, pdata in navamsa.items():
        if pdata["d1_sign"] == pdata["d9_sign"]:
            vargottama_planets.append({
                "planet":  pname,
                "symbol":  pdata.get("symbol", ""),
                "sign":    pdata["d9_sign"],
                "interp":  VARGOTTAMA_INTERP.get(pname, f"{pname} is Vargottama — its qualities are amplified and pure across both charts."),
            })

    # ── D9 Elemental Balance ─────────────────────────────────────────────────
    element_counts = {"Fire": 0, "Earth": 0, "Air": 0, "Water": 0}
    for pdata in navamsa.values():
        el = _SIGN_ELEMENTS.get(pdata["d9_sign"])
        if el:
            element_counts[el] += 1
    max_count = max(element_counts.values()) if element_counts else 0
    dominant_elements = [el for el, cnt in element_counts.items() if cnt == max_count]
    if len(dominant_elements) == 1:
        dominant_element = dominant_elements[0]
        element_interp = D9_ELEMENT_INTERP.get(dominant_element, "")
    else:
        dominant_element = "Balanced"
        element_interp = D9_ELEMENT_INTERP.get("Balanced", "")

    # ── Moon / Mars / Jupiter in D9 ─────────────────────────────────────────
    d9_moon_sign    = navamsa.get("Moon",    {}).get("d9_sign", "")
    d9_mars_sign    = navamsa.get("Mars",    {}).get("d9_sign", "")
    d9_jupiter_sign = navamsa.get("Jupiter", {}).get("d9_sign", "")

    return {
        "placements":        navamsa,
        "d9_lagna_sign":     d9_lagna_sign,
        "d9_7th_sign":       d9_7th_sign,
        "d9_7th_lord":       d9_7th_lord,
        "d9_7th_lord_sign":  d9_7th_lord_sign,
        "d9_7th_lord_house": d9_7th_lord_house,
        "d9_venus_sign":     d9_venus_sign,
        "darakaraka":        dk_planet,
        "darakaraka_d9_sign": dk_d9_sign,
        "atmakaraka":        ak_planet,
        "atmakaraka_d9_sign": ak_d9_sign,
        "karakas":           karakas,
        # Interpretations
        "lagna_interp":      NAVAMSA_LAGNA_INTERP.get(d9_lagna_sign, ""),
        "venus_interp":      NAVAMSA_VENUS_INTERP.get(d9_venus_sign, ""),
        "seventh_interp":    NAVAMSA_7TH_SIGN_INTERP.get(d9_7th_sign, ""),
        "dk_interp":         DARAKARAKA_INTERP.get(dk_planet, ""),
        # Deeper personality insights
        "vargottama_planets":  vargottama_planets,
        "element_counts":      element_counts,
        "dominant_element":    dominant_element,
        "element_interp":      element_interp,
        "d9_moon_sign":        d9_moon_sign,
        "moon_interp":         NAVAMSA_MOON_INTERP.get(d9_moon_sign, ""),
        "d9_mars_sign":        d9_mars_sign,
        "mars_interp":         NAVAMSA_MARS_INTERP.get(d9_mars_sign, ""),
        "d9_jupiter_sign":     d9_jupiter_sign,
        "jupiter_interp":      NAVAMSA_JUPITER_INTERP.get(d9_jupiter_sign, ""),
    }
