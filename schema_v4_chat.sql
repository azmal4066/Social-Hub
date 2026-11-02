-- Social Hub v4: chat upgrade (themes, calls log, media, voice, disappearing, mute, nicknames, block, report)
-- Run ONCE in Supabase > SQL Editor (after schema.sql, schema_v2_update.sql, schema_v3_fix.sql). Safe to re-run.

-- 1. richer messages
alter table public.messages add column if not exists kind text not null default 'text';
alter table public.messages add column if not exists media_url text;
alter table public.messages add column if not exists meta jsonb;
alter table public.messages add column if not exists expires_at timestamptz;
alter table public.messages drop constraint if exists messages_body_check;
alter table public.messages drop constraint if exists messages_body_len;
alter table public.messages add constraint messages_body_len check (char_length(body) <= 1000);

-- 2. shared chat settings (theme, disappearing timer, nicknames); user_a < user_b
create table if not exists public.chat_settings (
  user_a uuid not null references public.profiles(id) on delete cascade,
  user_b uuid not null references public.profiles(id) on delete cascade,
  theme text not null default '',
  disappear int not null default 0,
  nick_a text, nick_b text,
  primary key (user_a, user_b), check (user_a < user_b));
alter table public.chat_settings enable row level security;
drop policy if exists "cs read" on public.chat_settings;
drop policy if exists "cs insert" on public.chat_settings;
drop policy if exists "cs update" on public.chat_settings;
create policy "cs read" on public.chat_settings for select to authenticated using ((select auth.uid()) in (user_a, user_b));
create policy "cs insert" on public.chat_settings for insert to authenticated with check ((select auth.uid()) in (user_a, user_b));
create policy "cs update" on public.chat_settings for update to authenticated using ((select auth.uid()) in (user_a, user_b)) with check ((select auth.uid()) in (user_a, user_b));

-- 3. per-user chat prefs (mute, delete-chat-for-me)
create table if not exists public.chat_prefs (
  user_id uuid not null references public.profiles(id) on delete cascade,
  peer_id uuid not null references public.profiles(id) on delete cascade,
  muted boolean not null default false,
  cleared_at timestamptz,
  primary key (user_id, peer_id));
alter table public.chat_prefs enable row level security;
drop policy if exists "cp own" on public.chat_prefs;
create policy "cp own" on public.chat_prefs for all to authenticated using ((select auth.uid()) = user_id) with check ((select auth.uid()) = user_id);

-- 4. blocks + reports
create table if not exists public.blocks (
  blocker_id uuid not null references public.profiles(id) on delete cascade,
  blocked_id uuid not null references public.profiles(id) on delete cascade,
  created_at timestamptz not null default now(),
  primary key (blocker_id, blocked_id), check (blocker_id <> blocked_id));
alter table public.blocks enable row level security;
drop policy if exists "blocks read" on public.blocks;
drop policy if exists "blocks insert" on public.blocks;
drop policy if exists "blocks delete" on public.blocks;
create policy "blocks read" on public.blocks for select to authenticated using ((select auth.uid()) in (blocker_id, blocked_id));
create policy "blocks insert" on public.blocks for insert to authenticated with check ((select auth.uid()) = blocker_id);
create policy "blocks delete" on public.blocks for delete to authenticated using ((select auth.uid()) = blocker_id);

create table if not exists public.reports (
  id uuid primary key default gen_random_uuid(),
  reporter_id uuid not null references public.profiles(id) on delete cascade,
  reported_id uuid not null references public.profiles(id) on delete cascade,
  reason text, created_at timestamptz not null default now());
alter table public.reports enable row level security;
drop policy if exists "reports insert" on public.reports;
create policy "reports insert" on public.reports for insert to authenticated with check ((select auth.uid()) = reporter_id);

-- 5. message policies: hide expired, no sending to people who blocked you, allow unsend
drop policy if exists "messages read own" on public.messages;
create policy "messages read own" on public.messages for select to authenticated
  using (((select auth.uid()) = sender_id or (select auth.uid()) = receiver_id) and (expires_at is null or expires_at > now()));
drop policy if exists "messages send as self" on public.messages;
create policy "messages send as self" on public.messages for insert to authenticated
  with check ((select auth.uid()) = sender_id
    and not exists (select 1 from public.blocks b where (b.blocker_id = receiver_id and b.blocked_id = sender_id) or (b.blocker_id = sender_id and b.blocked_id = receiver_id)));
drop policy if exists "messages unsend own" on public.messages;
create policy "messages unsend own" on public.messages for delete to authenticated using ((select auth.uid()) = sender_id);

-- 6. realtime for theme sync
do $$ begin
  begin alter publication supabase_realtime add table public.chat_settings; exception when duplicate_object then null; end;
end $$;

notify pgrst, 'reload schema';
