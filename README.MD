# Social Hub

## Supabase (project: social-hub) - already applied
Run in order if you set up a new project: schema.sql, schema_v4_chat.sql, schema_v5_groups.sql,
schema_v8_music.sql, schema_v9_notes.sql, schema_v10_note_reactions.sql,
schema_v11_profile.sql, schema_v12_notifications.sql  (v12 = NEW - story likes for the Notifications page)

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

## v12 fixes
- Share profile QR card now opens full screen (CSS class clash with chat shared-post `.shr` fixed -> `.shq`).
- Story/post composer: preview no longer pushes Templates / Effects / Music panel off screen.
- Music autoplay: tapping a note, opening a post/reel (scroll into view) or story starts the song immediately (shared audio element unlocked on first touch, YouTube player preloaded, blocked play retries on next touch). Song stops when the post scrolls away / note closes.

## v13 changes
- Music: any song picked from iTunes/Spotify results is auto-upgraded to the FULL YouTube song (matched by title + length), then drag the strip to pick your part (up to 90 s). If YouTube blocks a song, it falls back to the 30s preview.
- YouTube quota saver: searches cached 12 h; `YOUTUBE_API_KEY` can hold several keys separated by commas (auto-rotates when one hits its daily quota).
- +100 latest 3D templates (Float, Fan, Skew, Flip, Glass, Neon, Pop, Tower, Coin, Grid x 10 palettes) -> 150 total.
- +100 3D effects (Anaglyph, Extrude, Tilt L/R, Mirror Floor, Tilt-Shift, Bevel, Pop-Out, Ghost Trail, Wall Fold x 10 grades) -> 150 total.

## v14 changes
- **Notifications page**: heart icon at the top right of Home (red dot when something new). Shows post / reel likes, comments, reposts, story likes, note likes + emoji reactions, follows, follow requests (Confirm / Delete right there), accepted requests, posts sent to you, missed calls and group adds - grouped Today / Yesterday / Last 7 days / Last 30 days. Tap a thumbnail to open the post, tap a name to open the profile.
- **Story likes**: heart button on other people's stories (needs `schema_v12_notifications.sql` - run it once in Supabase SQL Editor).
- **Music fix**: the post / reel song now stops as soon as you switch to another section (Home / Reels / Messages / Search / Profile).
- **Composer**: Templates, Effects and Collage layouts now show as a vertical scrolling grid (4 per row) instead of a sideways strip.
- **Reels UI**: glass action pill (like / comment / repost / send / save), glass header pills, bigger avatar ring, Follow pill, caption, music pill ("Original audio" when the reel has no song).
- **Coloured likes**: every reel like (double tap or heart) gets a different colour - red, rose, dark blue, orange, violet, green, white - kept per reel on the device.

## v15 changes
- **Run once:** `schema_v13_message_options.sql` in Supabase SQL Editor (Edit + synced "Delete for you").
- **Long-press a message** (or right-click on desktop) -> neon menu: quick reactions (+ full emoji list), Reply, Copy, Forward, Edit (your text messages), Save / open (photos, videos, files), Message info, Delete for you, Unsend (your messages), Report (other people's messages). Double-tap a message = heart. Tap no longer opens the old sheet.
- Reply quotes, "edited" and "Forwarded" labels are stored in `messages.meta` (no extra columns needed).
- **Curved + neon chat UI:** curved header and composer with glowing edges, gradient neon bubbles (yours) and glass neon bubbles (theirs), pop-in animation, glowing sheets and theme tiles.
- **+50 chat themes** (Theme sheet now has Classic / Nature / Love): 25 nature scenes (mountains, forests, ocean, beach, aurora, dunes, night sky, blossom) and 25 love scenes (heart bokeh, petals, couples, balloons, fairy lights, love sky, neon hearts). They are drawn as built-in SVG art, so no image hosting is needed.
- **+50 templates** (10 styles x 5 palettes): Glitter Frame, Y2K Window, Scrapbook, Heart Frame, Spotlight, Magazine, Ticket Stub, Lock Screen, Bubble Cluster, Viewfinder -> 200 total.
- **+50 effects** (10 effects x 5 colours): Glitter, Sparkle, Love Bokeh, Prism, VHS Glitch, Snowfall, Rain, Confetti, Dream Glow, Holo Foil -> 200 total.
