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
3. `schema_v3_fix.sql`     (sign-up fix + login-only visibility)
4. `schema_v4_chat.sql`    (chat upgrade: themes, calls, media, mute, block ...)
5. `schema_v5_groups.sql`  (**NEW** - group chats + reactions)

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
- Reels: app allows up to 500 MB (resumable upload). Supabase **free plan caps every file at 50 MB**; for bigger reels use the Pro plan and raise Settings > Storage > Upload file size limit.


## v4 chat upgrade
Instagram-style chat: tap the name for the details page (Profile / Search / Mute / Options, Theme with 20 themes + upload, Disappearing messages, Privacy & safety, Nicknames, Shared media), voice + video calls (WebRTC over Supabase Realtime, STUN only - add a TURN server in `ICE` for strict mobile networks), photo/video/voice/sticker/location/file messages, unsend, seen, block, report. Group chats (create, rename, add people, leave, mute) and message reactions (tap a message / double-tap for a heart) are included. Run `schema_v5_groups.sql` after v4 (already applied on your Supabase project).
`schema_v2_update.sql` was not in the upload - keep your existing copy next to the others.

## v6 update (navigation + notifications + calls)
No new SQL needed. Replace `app.py` (and `static/index.html`, which is the same UI).

- **Back button**: the phone/browser back button now goes back one screen inside the app
  (info -> chat -> chats -> previous screen). On the first screen it shows
  "Press back again to exit"; a second press within 2 seconds leaves the app.
  Back also closes open sheets, stories and the side menu first.
- **Chat section is full screen**: the chat list, a conversation, chat info and group screens hide the
  menu. The back arrow (top-left of the chat list) returns to the previous screen.
- **Side menu**: the 5 bottom options (Home, Reels, Messages, Search, Profile) are now a left sidebar.
  Tap the small handle on the left edge, or swipe right from the left edge. Tap outside / swipe left to close.
- **Notifications**: new message, voice call and video call alerts - in-app banner, sound, vibration,
  and a system notification (while the app is open or in a background tab, where the browser allows it).
  Incoming calls ring until answered or declined.
- **Calls fixed**: the app no longer re-initialises (and drops its realtime channels) every time the tab regains
  focus; the invite is re-sent every 2.5 s while ringing; reconnects on resume; TURN relay added to `ICE`
  (free public relay - replace with your own TURN for production).
- Limitation: browsers cannot ring or notify a phone that is locked or has the app fully closed without
  Web Push + a service worker, which Streamlit hosting cannot serve. For that, host `static/index.html` as a standalone PWA.
