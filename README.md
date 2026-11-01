# Social Hub

Instagram-style social app (dark theme) built with plain HTML/JS and Supabase,
wrapped in Streamlit so it can be deployed on Streamlit Community Cloud.

Features: sign up / log in, feed, photo posts, **reels (video upload)**, likes,
comments, reposts, send posts/reels in DM, saves, follow, suggested people,
stories (24h), realtime DMs, user search, edit profile, **private / public
accounts with follow requests**, mobile number, change password.

## Database setup (run in Supabase > SQL Editor, in this order)
1. `schema.sql`            (new Supabase project only)
2. `schema_v2_update.sql`  (reels, private accounts, RPCs)
3. `schema_v3_fix.sql`     (**NEW** - sign-up fix + login-only visibility)

Existing project? Just run `schema_v3_fix.sql` once (safe to re-run).

## What v3 changed
- **"Database error saving new user" fixed.** The sign-up trigger now cleans the
  username and adds a number if it is taken. The app also checks the username
  *before* sign-up and shows "Username already taken".
- **Reels / posts / stories visibility**
  - Public account: every *logged-in* user sees its posts and reels
    (Reels tab shows everyone's reels; Friends tab = people you follow).
  - Private account: only the owner and accepted followers.
  - Logged-out visitors see nothing.
- If a feed fails to load, the real error message is now shown instead of "No reels yet".

## Run locally
    pip install -r requirements.txt
    streamlit run app.py

## Deploy on Streamlit Community Cloud
1. Push this folder to a GitHub repository.
2. share.streamlit.io > Create app > main file `app.py`.
3. Supabase > Authentication > URL Configuration: set Site URL to your app URL.
4. For quick testing, turn off **Confirm email** (Authentication > Providers > Email).

## Project layout
    app.py                 Streamlit wrapper (the UI is embedded inside it)
    static/index.html      Same UI as a standalone copy (keep in sync with app.py)
    schema.sql / schema_v2_update.sql / schema_v3_fix.sql
    .streamlit/config.toml Dark theme

## Notes
- Supabase URL + publishable key in the HTML are meant to be public; RLS protects data.
  Never commit a `service_role` key.
- Media files live in a public storage bucket, so someone who already has a direct
  file URL can still open it (the URL is not shown to people who can't see the post).
- Reels are videos up to 50 MB (Supabase free-plan limit).
