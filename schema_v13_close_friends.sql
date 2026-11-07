-- v13: Close Friends + story audience
-- Supabase -> SQL Editor -> paste -> Run   (safe to run many times)
create table if not exists public.close_friends (
  owner_id  uuid not null references public.profiles(id) on delete cascade,
  friend_id uuid not null references public.profiles(id) on delete cascade,
  created_at timestamptz not null default now(),
  primary key (owner_id, friend_id),
  check (owner_id <> friend_id)
);
alter table public.close_friends enable row level security;
grant select, insert, delete on public.close_friends to authenticated;
drop policy if exists "cf read" on public.close_friends;
create policy "cf read" on public.close_friends for select to authenticated
  using (owner_id = (select auth.uid()) or friend_id = (select auth.uid()));
drop policy if exists "cf insert" on public.close_friends;
create policy "cf insert" on public.close_friends for insert to authenticated
  with check (owner_id = (select auth.uid()));
drop policy if exists "cf delete" on public.close_friends;
create policy "cf delete" on public.close_friends for delete to authenticated
  using (owner_id = (select auth.uid()));

alter table public.stories add column if not exists audience text not null default 'all' check (audience in ('all','close'));

drop policy if exists "stories readable until expiry" on public.stories;
create policy "stories readable until expiry" on public.stories for select
  using (
    expires_at > now()
    and (
      audience = 'all'
      or user_id = (select auth.uid())
      or exists (select 1 from public.close_friends c
                 where c.owner_id = stories.user_id and c.friend_id = (select auth.uid()))
    )
  );
notify pgrst, 'reload schema';
