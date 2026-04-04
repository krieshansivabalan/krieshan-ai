from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    google_id = db.Column(db.String(128), unique=True, nullable=False, index=True)
    email = db.Column(db.String(256), unique=True, nullable=False)
    name = db.Column(db.String(256), nullable=False)
    picture_url = db.Column(db.String(512))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    charts = db.relationship(
        "BirthChart", back_populates="user",
        cascade="all, delete-orphan", lazy="dynamic"
    )
    subscription = db.relationship(
        "Subscription", back_populates="user",
        uselist=False, cascade="all, delete-orphan"
    )

    @property
    def is_paid(self):
        if not self.subscription:
            return False
        return (
            self.subscription.status == "active"
            and self.subscription.current_period_end is not None
            and self.subscription.current_period_end > datetime.utcnow()
        )


class BirthChart(db.Model):
    __tablename__ = "birth_charts"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)
    label = db.Column(db.String(256))
    date = db.Column(db.String(16))
    time = db.Column(db.String(8))
    city = db.Column(db.String(256))
    full_address = db.Column(db.String(512))
    gender = db.Column(db.String(1))           # "M" or "F"
    placements_json = db.Column(db.Text)
    career_json = db.Column(db.Text)
    romance_json = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", back_populates="charts")


class Subscription(db.Model):
    __tablename__ = "subscriptions"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, unique=True)
    stripe_customer_id = db.Column(db.String(128), index=True)
    stripe_subscription_id = db.Column(db.String(128), index=True)
    status = db.Column(db.String(32), default="none")  # "active" | "cancelled" | "none"
    current_period_end = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", back_populates="subscription")


class JournalEntry(db.Model):
    __tablename__ = "journal_entries"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)
    content = db.Column(db.Text, nullable=False)
    entry_date = db.Column(db.String(16))           # YYYY-MM-DD
    moon_sign = db.Column(db.String(32))
    moon_nakshatra = db.Column(db.String(64))
    active_transits_json = db.Column(db.Text)        # JSON summary string
    is_retrograde_period = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", backref=db.backref("journal_entries", cascade="all, delete-orphan", lazy="dynamic"))
