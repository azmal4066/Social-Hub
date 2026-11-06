-- v12: story likes (so story likes can show up on the Notifications page)
-- Supabase -> SQL Editor -> paste -> Run   (safe to run many times)
create table if not exists public.story_likes (
  story_id   uuid not null,
  user_id    uuid not null references public.profiles(id) on delete cascade,
  owner_id   uuid not null references public.profiles(id) on delete cascade,
  story_url  text,
  created_at timestamptz not null default now(),
  primary key (story_id, user_id)
);
create index if not exists story_likes_owner on public.story_likes (owner_id, created_at desc);
alter table public.story_likes enable row level security;
grant select, insert, delete on public.story_likes to authenticated;

drop policy if exists "sl read" on public.story_likes;
create policy "sl read" on public.story_likes for select to authenticated
  using (user_id = (select auth.uid()) or owner_id = (select auth.uid()));
drop policy if exists "sl insert" on public.story_likes;
create policy "sl insert" on public.story_likes for insert to authenticated
  with check (user_id = (select auth.uid()) and user_id <> owner_id);
drop policy if exists "sl delete" on public.story_likes;
create policy "sl delete" on public.story_likes for delete to authenticated
  using (user_id = (select auth.uid()) or owner_id = (select auth.uid()));

notify pgrst, 'reload schema';
