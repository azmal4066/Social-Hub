# Social Hub

## Supabase (project: social-hub) - already applied
Run in order if you set up a new project: schema.sql, schema_v4_chat.sql, schema_v5_groups.sql,
schema_v8_music.sql, schema_v9_notes.sql, schema_v10_note_reactions.sql,
schema_v11_profile.sql  (NEW - needed for pronouns/links/banners/gender/AI label/professional/grid order)

## Full songs
app.py -> `YOUTUBE_API_KEY = ""`  (Google Cloud -> enable YouTube Data API v3 -> create API key).
Without a key only the 30s iTunes previews work.

## Run
pip install -r requirements.txt && streamlit run app.py
(.streamlit/config.toml = dark theme - keep this folder next to app.py)

## What's new
- Notes moved to the Chats page top; tap a note to like / react (emoji) / reply. Owner sees who reacted.
- Music picker: full song, drag the strip to pick the part, choose any seconds (up to 90).
- Story sticker styles: Rectangle, Square, Circle, Music only, Lyrics.
- Sidebar on the right.

## v11 changes
- Chats page: Instagram-style DM list (Messages / Requests, time ago, unread dot), notes tray, new note viewer (reply box + like + emoji reactions).
- Edit profile is now a full page: photo/avatar, name, username, pronouns, bio, links, banners, gender, reorder grid, AI label, professional account.
- Share profile: gradient QR card with COLOR, Share profile, Copy link, Download, and scan.
- Dark theme everywhere (Streamlit theme + app UI). Settings -> Notifications: push on/off + test, pause (1h/8h/24h), messages, groups, calls, sound, vibration, message preview, call ringtone (saved per user on the device).
