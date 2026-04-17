---
name: Project — Krieshan AI
description: Full overview of the Krieshan AI sidereal astrology app — stack, deployment, features, status
type: project
---

## What it is
A Vedic sidereal astrology SaaS web app. Users enter birth details and get a full birth chart (D1, D9 Navamsa, D10 Dasamsa), nakshatra readings, Vimshottari Dasha timing, transits, soul profile, character archetypes, synastry, an astro journal, and AI chart chat.

## Stack
- **Backend:** Python/Flask, SQLAlchemy, PostgreSQL (via Railway)
- **Auth:** Google OAuth via Authlib (`/auth/google` → `/auth/callback`)
- **Payments:** Stripe — direct payment links (buy.stripe.com), webhook at `/stripe-webhook`
- **AI:** Anthropic SDK (claude-sonnet model) for `/api/chat`
- **Deployment:** Railway (auto-deploys on push to `main` branch of `krieshansivabalan/krieshan-ai`)
- **Local path:** `/Users/krieshansivabalan/sidereal_astrology/`

## Pricing tiers
- Free — basic chart only
- Seeker $15/mo — daily transits, Dasha, Soul Profile, D9/D10, PDF
- Scholar $40/mo — everything + synastry, journal, fixed stars, AI chat
- Sage $99.98/mo — unlimited everything, early features

## Key routes
- `/` → landing page (login.html) — all users
- `/app` → main chart calculator (index.html) — login required
- `/admin` → admin dashboard, password protected via `ADMIN_PASSWORD` env var
- `/admin/login` → admin login form
- `/payment-success?tier=X` → post-Stripe redirect, activates subscription optimistically
- `/stripe-webhook` → CSRF-exempt, handles `checkout.session.completed` + subscription events
- `/auth/google` → starts Google OAuth
- `/auth/callback` → OAuth callback, creates/updates user, sets `session.permanent = True`

## Environment variables (set in Railway)
- `FLASK_SECRET_KEY` — required, hard-fails if missing in production
- `DATABASE_URL` — PostgreSQL connection string (set by Railway automatically)
- `GOOGLE_CLIENT_ID` / `GOOGLE_CLIENT_SECRET` — Google OAuth
- `STRIPE_SECRET_KEY` — live mode (`sk_live_...`)
- `STRIPE_WEBHOOK_SECRET` — from Stripe live webhook dashboard
- `ADMIN_PASSWORD` — plain text admin password (no hashing)
- `ANTHROPIC_API_KEY` — for AI chart chat

## Current status (April 2026)
- Live and launch-ready
- Google OAuth working
- Stripe live mode active
- Admin dashboard working
- All major features built and deployed
- AI Chart Chat built but hidden in UI (needs to be enabled)
- Custom domain `krieshanai.com` not yet pointed to Railway

## Remaining tasks (priority order)
1. Enable AI Chart Chat in the UI (Seeker+ tier)
2. Welcome email on signup (SendGrid)
3. Add Google Analytics
4. New user onboarding prompt on /app
5. Weekly transit alert emails
6. Remove "coming soon" labels from landing page
7. Account deletion button in UI (backend route `/api/account DELETE` already exists)
8. Replace placeholder testimonials with real user quotes
