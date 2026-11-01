-- Social Hub v2 update: reels (video), reposts, sends, private accounts,
-- follow requests, suggested people, mobile number.
-- Run ONCE in Supabase Dashboard > SQL Editor (safe to re-run).
-- New Supabase project? Run schema.sql first, then this file.

-- ---------- columns ----------
alter table public.profiles add column if not exists is_private boolean not null default false;

alter table public.posts add column if not exists kind text not null default 'post';
alter table public.posts add column if not exists media_type text not null default 'image';
alter table public.posts drop constraint if exists posts_kind_check;
alter table public.posts add constraint posts_kind_check check (kind in ('post','reel'));
alter table public.posts drop constraint if exists posts_media_type_check;
alter table public.posts add constraint posts_media_type_check check (media_type in ('image','video'));

alter table public.follows add column if not exists status text not null default 'accepted';
alter table public.follows drop constraint if exists follows_status_check;
alter table public.follows add constraint follows_status_check check (status in ('pending','accepted'));

alter table public.messages add column if not exists post_id uuid references public.posts(id) on delete set null;

create index if not exists posts_kind_idx on public.posts (kind, created_at desc);
create index if not exists follows_status_idx on public.follows (following_id, status);

-- ---------- new tables ----------
create table if not exists public.user_private (
  id uuid primary key references public.profiles(id) on delete cascade,
  phone text check (phone is null or phone ~ '^\+?[0-9]{7,15}$'),
  updated_at timestamptz not null default now()
);
create table if not exists public.reposts (
  post_id uuid not null references public.posts(id) on delete cascade,
  user_id uuid not null references public.profiles(id) on delete cascade,
  created_at timestamptz not null default now(),
  primary key (post_id, user_id)
);
create table if not exists public.shares (
  id uuid primary key default gen_random_uuid(),
  post_id uuid not null references public.posts(id) on delete cascade,
  user_id uuid not null references public.profiles(id) on delete cascade,
  receiver_id uuid not null references public.profiles(id) on delete cascade,
  created_at timestamptz not null default now()
);
create index if not exists reposts_user_idx on public.reposts (user_id, created_at desc);
create index if not exists shares_post_idx on public.shares (post_id);

alter table public.user_private enable row level security;
alter table public.reposts enable row level security;
alter table public.shares enable row level security;

-- ---------- privacy helper ----------
-- true if the signed-in user may see owner's posts/stories/followers/following:
-- own account, public account, or an accepted follower of a private account.
create or replace function public.can_view(owner uuid)
returns boolean language sql stable security definer set search_path = '' as $$
  select owner = (select auth.uid())
      or not exists (select 1 from public.profiles p where p.id = owner and p.is_private)
      or exists (select 1 from public.follows f
                 where f.follower_id = (select auth.uid())
                   and f.following_id = owner and f.status = 'accepted');
$$;

-- ---------- posts / stories ----------
drop policy if exists "posts readable" on public.posts;
drop policy if exists "posts visible" on public.posts;
create policy "posts visible" on public.posts for select using (public.can_view(user_id));

drop policy if exists "stories readable until expiry" on public.stories;
drop policy if exists "stories visible" on public.stories;
create policy "stories visible" on public.stories for select
  using (expires_at > now() and public.can_view(user_id));

-- ---------- likes / comments (only on posts you can see) ----------
drop policy if exists "likes readable" on public.likes;
drop policy if exists "likes visible" on public.likes;
create policy "likes visible" on public.likes for select
  using (exists (select 1 from public.posts p where p.id = post_id));
drop policy if exists "likes insert own" on public.likes;
create policy "likes insert own" on public.likes for insert to authenticated
  with check ((select auth.uid()) = user_id and exists (select 1 from public.posts p where p.id = post_id));

drop policy if exists "comments readable" on public.comments;
drop policy if exists "comments visible" on public.comments;
create policy "comments visible" on public.comments for select
  using (exists (select 1 from public.posts p where p.id = post_id));
drop policy if exists "comments insert own" on public.comments;
create policy "comments insert own" on public.comments for insert to authenticated
  with check ((select auth.uid()) = user_id and exists (select 1 from public.posts p where p.id = post_id));

-- ---------- follows (+ requests for private accounts) ----------
drop policy if exists "follows readable" on public.follows;
drop policy if exists "follows insert own" on public.follows;
drop policy if exists "follows delete own" on public.follows;
drop policy if exists "follows visible" on public.follows;
drop policy if exists "follows accept" on public.follows;

create policy "follows visible" on public.follows for select using (
  (select auth.uid()) in (follower_id, following_id)
  or (status = 'accepted' and public.can_view(follower_id) and public.can_view(following_id)));
create policy "follows insert own" on public.follows for insert to authenticated with check (
  (select auth.uid()) = follower_id and (
    (status = 'pending' and exists (select 1 from public.profiles p where p.id = following_id and p.is_private))
    or (status = 'accepted' and not exists (select 1 from public.profiles p where p.id = following_id and p.is_private))));
create policy "follows accept" on public.follows for update to authenticated
  using ((select auth.uid()) = following_id)
  with check ((select auth.uid()) = following_id and status = 'accepted');
create policy "follows delete own" on public.follows for delete to authenticated
  using ((select auth.uid()) in (follower_id, following_id));

-- switching a private account to public accepts all waiting requests
create or replace function public.on_privacy_change()
returns trigger language plpgsql security definer set search_path = '' as $$
begin
  if old.is_private and not new.is_private then
    update public.follows set status = 'accepted' where following_id = new.id and status = 'pending';
  end if;
  return new;
end $$;
revoke execute on function public.on_privacy_change() from public, anon, authenticated;
drop trigger if exists on_profile_privacy_change on public.profiles;
create trigger on_profile_privacy_change after update of is_private on public.profiles
  for each row execute function public.on_privacy_change();

-- ---------- reposts / shares ----------
drop policy if exists "reposts visible" on public.reposts;
create policy "reposts visible" on public.reposts for select
  using (public.can_view(user_id) and exists (select 1 from public.posts p where p.id = post_id));
drop policy if exists "reposts insert own" on public.reposts;
create policy "reposts insert own" on public.reposts for insert to authenticated
  with check ((select auth.uid()) = user_id and exists (select 1 from public.posts p where p.id = post_id));
drop policy if exists "reposts delete own" on public.reposts;
create policy "reposts delete own" on public.reposts for delete to authenticated
  using ((select auth.uid()) = user_id);

drop policy if exists "shares visible" on public.shares;
create policy "shares visible" on public.shares for select
  using (exists (select 1 from public.posts p where p.id = post_id));
drop policy if exists "shares insert own" on public.shares;
create policy "shares insert own" on public.shares for insert to authenticated
  with check ((select auth.uid()) = user_id and exists (select 1 from public.posts p where p.id = post_id));

-- ---------- private phone number (only the owner can read/write) ----------
drop policy if exists "phone read own" on public.user_private;
create policy "phone read own" on public.user_private for select to authenticated using ((select auth.uid()) = id);
drop policy if exists "phone insert own" on public.user_private;
create policy "phone insert own" on public.user_private for insert to authenticated with check ((select auth.uid()) = id);
drop policy if exists "phone update own" on public.user_private;
create policy "phone update own" on public.user_private for update to authenticated
  using ((select auth.uid()) = id) with check ((select auth.uid()) = id);

-- ---------- RPCs ----------
-- posts/followers/following counts; null when the viewer may not see them
create or replace function public.profile_stats(uid uuid)
returns json language sql stable security definer set search_path = '' as $$
  select case when public.can_view(uid) then json_build_object(
    'posts',     (select count(*) from public.posts   where user_id = uid),
    'followers', (select count(*) from public.follows where following_id = uid and status = 'accepted'),
    'following', (select count(*) from public.follows where follower_id  = uid and status = 'accepted'))
  else null end;
$$;

-- save counts for a batch of posts (the list of who saved stays private)
create or replace function public.save_counts(ids uuid[])
returns table(post_id uuid, n bigint) language sql stable security definer set search_path = '' as $$
  select s.post_id, count(*)
  from public.saves s join public.posts p on p.id = s.post_id
  where s.post_id = any(ids) and public.can_view(p.user_id)
  group by s.post_id;
$$;

-- people followed by the people you follow (most mutuals first)
create or replace function public.suggested_users(lim int default 12)
returns table(id uuid, username text, full_name text, is_private boolean, via text, mutuals bigint)
language sql stable security definer set search_path = '' as $$
  with fr as (
    select following_id as friend from public.follows
    where follower_id = (select auth.uid()) and status = 'accepted'),
  cand as (
    select f.following_id as cid, count(*) as n, min(pf.username) as via
    from public.follows f
    join fr on fr.friend = f.follower_id
    join public.profiles pf on pf.id = f.follower_id
    where f.status = 'accepted'
      and f.following_id <> (select auth.uid())
      and not exists (select 1 from public.follows x
                      where x.follower_id = (select auth.uid()) and x.following_id = f.following_id)
    group by f.following_id)
  select p.id, p.username, p.full_name, p.is_private, c.via, c.n
  from cand c join public.profiles p on p.id = c.cid
  order by c.n desc, p.username
  limit lim;
$$;

notify pgrst, 'reload schema';
