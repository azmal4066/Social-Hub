-- Social Hub v3 fix
--  1. Sign-up "Database error saving new user" fix
--  2. Content (posts / reels / stories) only for LOGGED-IN users
--     - public account  -> every logged-in user can see it
--     - private account -> only the owner + accepted followers
-- Run ONCE in Supabase Dashboard > SQL Editor (after schema.sql + schema_v2_update.sql).
-- Safe to re-run.

-- ---------- 1. sign-up trigger (never fails on a taken / odd username) ----------
create or replace function public.handle_new_user()
returns trigger language plpgsql security definer set search_path = '' as $$
declare
  base  text;
  uname text;
  n     int := 0;
begin
  base := lower(coalesce(new.raw_user_meta_data->>'username', ''));
  base := regexp_replace(base, '[^a-z0-9._]', '', 'g');
  if char_length(base) < 3 then
    base := 'user' || substr(replace(new.id::text, '-', ''), 1, 8);
  end if;
  base  := left(base, 30);
  uname := base;
  while exists (select 1 from public.profiles p where p.username = uname) loop
    n := n + 1;
    uname := left(base, 30 - char_length(n::text)) || n::text;
  end loop;

  insert into public.profiles (id, username, full_name)
  values (new.id, uname, new.raw_user_meta_data->>'full_name')
  on conflict (id) do nothing;
  return new;
end $$;

revoke execute on function public.handle_new_user() from public, anon, authenticated;

drop trigger if exists on_auth_user_created on auth.users;
create trigger on_auth_user_created after insert on auth.users
  for each row execute function public.handle_new_user();

-- repair: any auth user that has no profile yet gets one
insert into public.profiles (id, username)
select u.id, 'user' || substr(replace(u.id::text, '-', ''), 1, 8)
from auth.users u
where not exists (select 1 from public.profiles p where p.id = u.id)
on conflict do nothing;

-- ---------- 2. visibility rule: must be logged in ----------
create or replace function public.can_view(owner uuid)
returns boolean language sql stable security definer set search_path = '' as $$
  select (select auth.uid()) is not null and (
        owner = (select auth.uid())
     or not exists (select 1 from public.profiles p where p.id = owner and p.is_private)
     or exists (select 1 from public.follows f
                where f.follower_id = (select auth.uid())
                  and f.following_id = owner and f.status = 'accepted'));
$$;

-- posts & reels (same table) and stories use can_view(); recreate to be sure
drop policy if exists "posts visible" on public.posts;
create policy "posts visible" on public.posts for select to authenticated
  using (public.can_view(user_id));

drop policy if exists "stories visible" on public.stories;
create policy "stories visible" on public.stories for select to authenticated
  using (expires_at > now() and public.can_view(user_id));

notify pgrst, 'reload schema';
