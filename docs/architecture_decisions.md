---
name: Architecture Decisions — Krieshan AI
description: Critical technical decisions made during development. DO NOT reverse without understanding the reason.
type: project
---

## DO NOT CHANGE THESE — reasons documented below

### 1. `lazy="select"` on all SQLAlchemy relationships (not `lazy="dynamic"`)
**Why:** `lazy="dynamic"` is removed in SQLAlchemy 2.x (used by Flask-SQLAlchemy 3.1.1). Using it causes a crash on model load in the Railway production environment. All relationships in `models.py` use `lazy="select"`.

### 2. `joinedload(User.subscription)` in admin dashboard query
**Why:** Without eager loading, accessing `u.plan_tier` (which reads `u.subscription`) after the main query raises `DetachedInstanceError` in SQLAlchemy 2.x. The admin route must use `.options(joinedload(User.subscription))` on the User query.

### 3. `ProxyFix` middleware on the Flask app
**Why:** Railway terminates TLS and proxies to Flask over HTTP. Without `ProxyFix`, `url_for(..., _external=True)` generates `http://` URLs. Google OAuth requires `https://` redirect URIs, causing `redirect_uri_mismatch` (Error 400). The fix is in `app.py` right after `app = Flask(__name__)`.

### 4. Per-transaction DB migrations at startup
**Why:** PostgreSQL (unlike SQLite) aborts the entire transaction if any statement fails. All schema migrations must `commit()` and `rollback()` individually — not in a single batch. Each `ALTER TABLE` gets its own try/except/commit/rollback block.

### 5. `@login_manager.unauthorized_handler` returns JSON for API routes
**Why:** Flask-Login's default behavior is to redirect to the login page (HTML 302) when a protected route is hit without a session. This causes `JSON.parse()` to fail on the frontend with "unexpected token" errors. The custom handler returns JSON `{"error": "session_expired"}` for `/api/*` and `/chart` routes.

### 6. `session.permanent = True` set in `auth.py` callback
**Why:** Without this, the `PERMANENT_SESSION_LIFETIME = 30 days` config has no effect. Flask only applies the lifetime to permanent sessions. Set alongside `login_user(user, remember=True)` in the OAuth callback.

### 7. Direct Stripe payment links (not Checkout Sessions)
**Why:** The app uses `buy.stripe.com` direct payment links rather than server-side Stripe Checkout Session creation. This means `/payment-success` does NOT receive a `session_id`. Subscription activation happens via the `checkout.session.completed` webhook event using `client_reference_id` (the user's DB id) passed as a URL param on the payment link.

### 8. `ADMIN_PASSWORD` plain text env var (not bcrypt)
**Why:** The original bcrypt implementation required generating a hash via terminal command, which wasn't practical for a non-technical founder. Replaced with plain-text comparison against `ADMIN_PASSWORD` env var. Set this in Railway Variables.

### 9. `db.session.get(User, id)` not `User.query.get(id)`
**Why:** `Query.get()` is deprecated in SQLAlchemy 2.x. All primary-key lookups use `db.session.get(Model, id)`.

### 10. `BirthChart.query.filter_by(user_id=u.id)` in admin (not `u.charts`)
**Why:** Accessing `u.charts` via the ORM relationship was previously using `lazy="dynamic"` which caused crashes. Even after fixing to `lazy="select"`, the admin dashboard explicitly queries `BirthChart` directly to avoid any relationship loading issues.

## File structure notes
- `app.py` — all routes, middleware, admin panel, payment handling
- `auth.py` — Google OAuth blueprint (`auth_bp`), mounted at `/auth`
- `models.py` — User, BirthChart, Subscription, JournalEntry, ChatMessage
- `astrology.py` — all chart calculation logic (ephem-based)
- `interpretations.py` — all text content (dashas, nakshatras, stars, etc.)
- `characters.py` — character archetype logic
- `templates/` — all Jinja2 HTML templates
- `static/` — lion.svg logo, any other static assets
