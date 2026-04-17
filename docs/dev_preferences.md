---
name: Feedback & Preferences — Krieshan
description: How Krieshan likes to work, what to avoid, confirmed approaches
type: feedback
---

## Communication
- Keep responses short and direct. Lead with the action or answer.
- Don't explain what you're about to do — just do it.
- Don't summarize what was just done at the end of a response.

**Why:** Krieshan is non-technical and moves fast. Long explanations slow him down.

**How to apply:** Every response. Default to 1-3 sentences of context max, then code/action.

---

## Code changes
- Always push to `main` branch of `krieshansivabalan/krieshan-ai` — Railway auto-deploys from main.
- Don't create new files unless absolutely necessary.
- Don't add features beyond what was asked.
- Don't add comments, docstrings, or type annotations to code that wasn't changed.

**Why:** Keeps the codebase clean and deployments predictable.

---

## Admin page
- Admin is accessible at `/admin` — no login required to reach the login form, password-protected via `ADMIN_PASSWORD` env var.
- Admin should be visible to all users (linked in footer/bottom nav) but password-protected.
- Do not gate admin behind Google login or user tiers.

**Why:** Krieshan wants easy access to user data without having to be logged in as a specific Google account.

---

## Pricing
- Tiers: Free / Seeker $15/mo / Scholar $40/mo / Sage $99.98/mo
- Do not revert to $8/month anywhere in the codebase.
- "Oracle" was renamed to "Sage" — do not use "Oracle" in user-facing copy.

---

## Stripe
- Uses direct payment links (buy.stripe.com), not server-side Checkout Session creation.
- `client_reference_id` = user's DB id, passed as URL param on payment link.
- Webhook handles subscription activation via `checkout.session.completed` event.
- Payment-success route activates subscription optimistically (webhook may be delayed).

---

## Google OAuth
- Dev fallback: if `GOOGLE_CLIENT_ID` is not set, a "Dev User" (dev@localhost) is auto-created and logged in. This is intentional for local development only.
- In production (Railway), `GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET` must be set.
- Authorized redirect URI registered in Google Cloud Console: `https://krieshanai.up.railway.app/auth/callback`

---

## Logo
- The logo is `/static/lion.svg?v=2` — used consistently across all pages (login, index, privacy, terms).
- Do not replace with emoji or text characters.
