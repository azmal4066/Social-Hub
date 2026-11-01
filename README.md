# Social Hub

Instagram-style social app (dark theme) built with plain HTML/JS and Supabase,
wrapped in Streamlit so it can be deployed on Streamlit Community Cloud.

Features: sign up / log in, feed, photo posts, likes, comments, saves,
follow, stories (24h), realtime direct messages, user search, edit profile.

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
    supabase/schema.sql    Database schema, RLS policies, storage rules
    .streamlit/config.toml Dark theme

## Notes
- The Supabase URL and publishable key in `static/index.html` are meant to be public.
  Row-level security protects the data. Never commit a `service_role` key.
- Google login is not included in the Streamlit build (Google blocks sign-in inside iframes).
- To use your own Supabase project, edit `SB_URL` and `SB_KEY` in `static/index.html`
  and run `supabase/schema.sql` in the SQL Editor.
