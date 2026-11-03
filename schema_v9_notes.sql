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
5. `schema_v5_groups.sql`  (group chats + reactions)
6. `schema_v8_music.sql`   (music column + delete policies)
7. `schema_v9_notes.sql`   (**NEW** - notes table)

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

## v7 update (no new SQL needed)
Replace `app.py` and `static/index.html` (same UI).

- **Sidebar**: floating, icon-only rounded panel on the left (Home, Reels, Messages, Search, Profile) with a close arrow at the bottom. To show text labels again, delete the line `#nav button span:not(.dot){display:none}` in the v7 CSS block.
- **Chat**: message bubbles and stickers are smaller (font 13.5px).
- **Reels sound**: audio is ON by default; a single tap on a reel toggles sound off/on (and the choice is kept while scrolling). If the browser blocks sound autoplay, the first tap anywhere turns it on.
- **Reels order**: up to 300 new + old reels are loaded and shuffled every time the Reels tab opens.
- **Faster realtime**: your own messages appear instantly (optimistic send); direct messages also use a Supabase broadcast "ping" so the other person gets them quicker than waiting for database change events; connection is re-checked every 15 s.
- **Faster calls**: the call invite channel connects while the mic/camera permission is being asked, invites are re-sent at 0.7 s intervals first, and ICE candidates are pre-gathered.
- **Reactions**: 316 reactions (6 quick + 310 more, scrollable) in the message sheet.
- **Stickers**: new "Trending" section with 50 stickers above the full list.


## v8 update (run `schema_v8_music.sql` once)
Replace `app.py` and `static/index.html`.

- **New post / reel / story composer** (the `+` button on Home and Profile): Instagram-style screen with
  Templates, Effects, Music, Collage tiles (with icons), a camera tile, a Gallery tile and *Recents*.
  Tap **Select** to pick many photos (numbered) for a collage.
- **50 templates** (10 layouts x 5 palettes) and **50 trending effects** (Lofi dusk, Cinematic, Golden hour, VHS, Y2K, Neon night, Light leak ...), drawn on canvas.
- **8 collage layouts**.
- **Music**: search a song, pick it, choose the start point with the slider and a 5/10/15/30 s clip. It plays on posts, reels and stories (tap the green chip).
  Spotify: set `SPOTIFY_CLIENT_ID` and `APP_URL` in `app.py` and add `APP_URL` as a Redirect URI in the Spotify dashboard, then tap *Connect Spotify*.
  Spotify no longer returns preview URLs for most tracks, so those are matched to the 30 s iTunes preview automatically. Without a Client ID, the iTunes search is used.
- **Delete**: trash icon on your own posts, reels (Delete button) and stories (top right of the story viewer). Storage file is removed too.
- **Chat fix**: a single message / photo no longer stretches into a huge bubble; chat photos are capped at 220 px.
- Browsers cannot list the phone gallery. *Recents* shows photos you picked earlier in the session; the Gallery tile opens the phone picker.


## v9 update (run `schema_v9_notes.sql` once)
Replace `app.py` and `static/index.html`.

- **Notes**: a bubble above your avatar in the Home stories row. Tap it to write a note (max 60 chars)
  and/or add a song (Spotify or iTunes search). Notes last 24 h; pick the clip start (slider) and length (5/10/15/30 s). You see your own note and notes of people
  you follow; tap theirs to read it, hear the song and Reply (opens the chat). Delete from the same sheet.

## Spotify setup
1. https://developer.spotify.com/dashboard > Create app. Add Redirect URI = your Streamlit URL (exactly, e.g. `https://yourapp.streamlit.app`).
2. Copy the Client ID into `SPOTIFY_CLIENT_ID` and put the same URL in `APP_URL` at the top of `app.py`.
3. Spotify apps in Development mode only work for users added under *User Management* (max 25).
4. In the app tap *Connect Spotify* in the music search. The login lasts about 1 hour, then connect again.
