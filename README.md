# Social Hub

Instagram-style social app (dark theme) built with plain HTML/JS and Supabase,
wrapped in Streamlit so it can be deployed on Streamlit Community Cloud.

Features: sign up / log in, feed, photo posts, **reels (video upload)**, likes,
comments, **reposts**, **send posts/reels in DM**, saves (with public counts),
follow, **suggested people (followed by people you follow)**, stories (24h),
realtime direct messages, user search, edit profile, **private / public
accounts with follow requests**, **mobile number**, **change password**.

## IMPORTANT: update the database first (v2)
Open Supabase > SQL Editor, paste all of `schema_v2_update.sql` and run it once
(safe to re-run). Without it the new app cannot load posts.
New Supabase project? Run `schema.sql` first, then `schema_v2_update.sql`.

## Run locally
    pip install -r requirements.txt
    streamlit run app.py

## Deploy on Streamlit Community Cloud
1. Push this folder to a GitHub repository.
2. Go to https://share.streamlit.io and click **Create app**.
3. Pick the repository, branch `main`, and main file `app.py`. Deploy.
4. In Supabase: **Authentication > URL Configuration**, set **Site URL** to your
   Streamlit app URL (used in email confirmation links).
5. For quick testing, turn off **Confirm email** under Authentication > Providers > Email.

## Project layout
    app.py                 Streamlit wrapper
    static/index.html      The whole app (UI + Supabase client)
    schema.sql             Original database schema
    schema_v2_update.sql   v2 changes: reels, reposts, private accounts, RPCs
    .streamlit/config.toml Dark theme

## Notes
- The Supabase URL and publishable key in `static/index.html` are meant to be public.
  Row-level security protects the data. Never commit a `service_role` key.
- Google login is not included in the Streamlit build (Google blocks sign-in inside iframes).
- To use your own Supabase project, edit `SB_URL` and `SB_KEY` in `static/index.html`
  and run `schema.sql` + `schema_v2_update.sql` in the SQL Editor.
- Reels are videos up to 50 MB (Supabase free-plan upload limit). Photos go to Posts, videos to Reels.
- Private accounts: posts, reels, stories, followers and following are hidden by database
  rules (RLS), not just in the UI. Following a private account sends a request that the owner confirms
  in Settings > Follow requests. Switching to public accepts waiting requests.
- Media files live in a public storage bucket, so a direct file URL still opens if someone has it.
