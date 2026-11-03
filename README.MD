-- v9: Instagram-style notes (short text + optional song, visible 24h)
create table if not exists public.notes (
  user_id    uuid primary key references public.profiles(id) on delete cascade,
  content    text not null default '' check (char_length(content) <= 60),
  music      jsonb,
  created_at timestamptz not null default now(),
  expires_at timestamptz not null default (now() + interval '24 hours')
);
alter table public.notes enable row level security;

-- you see your own note + notes of people you follow (accepted)
drop policy if exists "notes read" on public.notes;
create policy "notes read" on public.notes for select to authenticated using (
  (select auth.uid()) = user_id
  or exists (select 1 from public.follows f
             where f.follower_id = (select auth.uid())
               and f.following_id = notes.user_id
               and f.status = 'accepted')
);
drop policy if exists "notes insert own" on public.notes;
create policy "notes insert own" on public.notes for insert to authenticated with check ((select auth.uid()) = user_id);
drop policy if exists "notes update own" on public.notes;
create policy "notes update own" on public.notes for update to authenticated using ((select auth.uid()) = user_id) with check ((select auth.uid()) = user_id);
drop policy if exists "notes delete own" on public.notes;
create policy "notes delete own" on public.notes for delete to authenticated using ((select auth.uid()) = user_id);
