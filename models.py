from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

# ── Tier limits ───────────────────────────────────────────────────
TIER_LIMITS = {
    "free":    {"charts": 1,  "ai_questions": 0,  "label": "Free"},
    "seeker":  {"charts": 5,  "ai_questions": 10, "label": "Seeker"},
    "scholar": {"charts": 20, "ai_questions": 50, "label": "Scholar"},
    "oracle":  {"charts": -1, "ai_questions": -1, "label": "Oracle"},  # -1 = unlimited
}


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id          = db.Column(db.Integer, primary_key=True)
    google_id   = db.Column(db.String(128), unique=True, nullable=False, index=True)
    email       = db.Column(db.String(256), unique=True, nullable=False)
    name        = db.Column(db.String(256), nullable=False)
    picture_url = db.Column(db.String(512))
    created_at  = db.Column(db.DateTime, default=datetime.utcnow)

    # Login tracking
    last_login_at = db.Column(db.DateTime, nullable=True)

    # AI usage tracking (resets monthly)
    ai_questions_used  = db.Column(db.Integer, default=0)
    ai_questions_reset = db.Column(db.DateTime, default=datetime.utcnow)

    charts = db.relationship(
        "BirthChart", back_populates="user",
        cascade="all, delete-orphan", lazy="dynamic"
    )
    subscription = db.relationship(
        "Subscription", back_populates="user",
        uselist=False, cascade="all, delete-orphan"
    )

    @property
    def plan_tier(self):
        """Return the user's current plan tier string."""
        if not self.subscription or self.subscription.status != "active":
            return "free"
        if self.subscription.current_period_end and self.subscription.current_period_end < datetime.utcnow():
            return "free"
        return self.subscription.plan_tier or "seeker"

    @property
    def is_paid(self):
        return self.plan_tier != "free"

    @property
    def tier_limits(self):
        return TIER_LIMITS.get(self.plan_tier, TIER_LIMITS["free"])

    def ai_quota_remaining(self):
        """Return remaining AI questions this month. -1 means unlimited."""
        limit = self.tier_limits["ai_questions"]
        if limit == -1:
            return -1
        # Reset monthly counter if needed
        now = datetime.utcnow()
        if self.ai_questions_reset is None or (
            now.year != self.ai_questions_reset.year or
            now.month != self.ai_questions_reset.month
        ):
            return limit  # Will be reset on next use
        return max(0, limit - (self.ai_questions_used or 0))

    def charts_limit(self):
        return self.tier_limits["charts"]


class BirthChart(db.Model):
    __tablename__ = "birth_charts"

    id           = db.Column(db.Integer, primary_key=True)
    user_id      = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)
    label        = db.Column(db.String(256))
    for_person   = db.Column(db.String(256))    # name of person this chart is for
    date         = db.Column(db.String(16))
    time         = db.Column(db.String(8))
    city         = db.Column(db.String(256))
    full_address = db.Column(db.String(512))
    gender       = db.Column(db.String(1))       # "M" or "F"
    placements_json = db.Column(db.Text)
    career_json     = db.Column(db.Text)
    romance_json    = db.Column(db.Text)
    created_at   = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", back_populates="charts")


class Subscription(db.Model):
    __tablename__ = "subscriptions"

    id                     = db.Column(db.Integer, primary_key=True)
    user_id                = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, unique=True)
    stripe_customer_id     = db.Column(db.String(128), index=True)
    stripe_subscription_id = db.Column(db.String(128), index=True)
    status                 = db.Column(db.String(32), default="none")   # active | cancelled | none
    plan_tier              = db.Column(db.String(16), default="seeker") # seeker | scholar | oracle
    current_period_end     = db.Column(db.DateTime)
    created_at             = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", back_populates="subscription")


class ChatMessage(db.Model):
    __tablename__ = "chat_messages"

    id         = db.Column(db.Integer, primary_key=True)
    user_id    = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)
    chart_id   = db.Column(db.Integer, db.ForeignKey("birth_charts.id"), nullable=True)
    role       = db.Column(db.String(16), nullable=False)   # "user" | "assistant"
    content    = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user  = db.relationship("User",       backref=db.backref("chat_messages", lazy="dynamic"))
    chart = db.relationship("BirthChart", backref=db.backref("chat_messages", lazy="dynamic"))


class JournalEntry(db.Model):
    __tablename__ = "journal_entries"

    id                   = db.Column(db.Integer, primary_key=True)
    user_id              = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)
    content              = db.Column(db.Text, nullable=False)
    entry_date           = db.Column(db.String(16))           # YYYY-MM-DD
    moon_sign            = db.Column(db.String(32))
    moon_nakshatra       = db.Column(db.String(64))
    active_transits_json = db.Column(db.Text)
    is_retrograde_period = db.Column(db.Boolean, default=False)
    created_at           = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", backref=db.backref("journal_entries", cascade="all, delete-orphan", lazy="dynamic"))
