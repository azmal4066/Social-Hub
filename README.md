# Social Hub

## Supabase (project: social-hub) - already applied
Run in order if you set up a new project: schema.sql, schema_v4_chat.sql, schema_v5_groups.sql,
schema_v8_music.sql, schema_v9_notes.sql, schema_v10_note_reactions.sql

## Full songs
app.py -> `YOUTUBE_API_KEY = ""`  (Google Cloud -> enable YouTube Data API v3 -> create API key).
Without a key only the 30s iTunes previews work.

## Run
pip install -r requirements.txt && streamlit run app.py
(.streamlit/config.toml = dark theme)

## What's new
- Notes moved to the Chats page top; tap a note to like / react (emoji) / reply. Owner sees who reacted.
- Music picker: full song, drag the strip to pick the part, choose any seconds (up to 90).
- Story sticker styles: Rectangle, Square, Circle, Music only, Lyrics.
- Sidebar on the right.
