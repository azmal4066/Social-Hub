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

## v17 changes - PHOTO STUDIO (no new SQL needed)
Open it from the **sidebar** (new wand icon, above Profile). Pick a photo, edit with any of these, then tap **Share** -> Post / Story (or "Add music first" to continue in the normal composer).
- **Background**: Remove background (auto) / AI person cut-out (MediaPipe, loads from CDN) -> Sensitivity / edge softness / grow-shrink sliders, Keep/Erase brush, replace with colour, gradient, scene, blur, your own photo, optional shadow.
- **Object**: paint over something, tap Remove (in-browser inpainting - best for small objects).
- **Enhance**: Auto enhance + strength, brightness, contrast, saturation, warmth.
- **Retouch**: skin smoothing + glow (skin-tone masked, keeps edges sharp).
- **Flare**: Sun / Anamorphic / Rainbow lens flare with position, size, colour.
- **HDR** + clarity, **Sharpen**, **Vignette** (dark/light).
- **Filters**: 31 colour looks + import your own `.cube` LUT file.
- **Gradient**: 16 gradient overlays with blend modes, opacity, angle.
- **Frames**: 12 borders (Polaroid, Film, Neon, Stamp, Arch...).
- **Templates / Effects**: the same 150 + 150 as the composer.
- **Stickers**: emoji, label stickers and 15 overlays (light leak, bokeh, rain, snow, dust...).
- **Text**: 16 Google fonts + upload your own font, 12 text effects (neon, 3D, glitch, gold...). Drag to move, sliders to resize / rotate.
- Format chips: Original / 4:5 Post / 9:16 Story. The ↶ button undoes background / object edits.
- Everything runs in the browser (nothing extra to install). Background/object tools are lightweight algorithms, not a cloud AI model.
