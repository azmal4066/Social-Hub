-- Social Hub database schema (already applied to the Supabase project).
-- Run in Supabase Dashboard > SQL Editor only if you set up a NEW project.

create table public.profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  username text not null unique check (username ~ '^[a-z0-9._]{3,30}$'),
  full_name text,
  bio text default '',
  avatar_url text,
  created_at timestamptz not null default now()
);
create table public.posts (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references public.profiles(id) on delete cascade,
  image_url text not null,
  caption text default '',
  created_at timestamptz not null default now()
);
create table public.likes (
  post_id uuid not null references public.posts(id) on delete cascade,
  user_id uuid not null references public.profiles(id) on delete cascade,
  created_at timestamptz not null default now(),
  primary key (post_id, user_id)
);
create table public.comments (
  id uuid primary key default gen_random_uuid(),
  post_id uuid not null references public.posts(id) on delete cascade,
  user_id uuid not null references public.profiles(id) on delete cascade,
  body text not null check (char_length(body) between 1 and 500),
  created_at timestamptz not null default now()
);
create table public.follows (
  follower_id uuid not null references public.profiles(id) on delete cascade,
  following_id uuid not null references public.profiles(id) on delete cascade,
  created_at timestamptz not null default now(),
  primary key (follower_id, following_id),
  check (follower_id <> following_id)
);
create table public.saves (
  post_id uuid not null references public.posts(id) on delete cascade,
  user_id uuid not null references public.profiles(id) on delete cascade,
  primary key (post_id, user_id)
);
create table public.stories (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references public.profiles(id) on delete cascade,
  image_url text not null,
  created_at timestamptz not null default now(),
  expires_at timestamptz not null default (now() + interval '24 hours')
);
create table public.messages (
  id uuid primary key default gen_random_uuid(),
  sender_id uuid not null references public.profiles(id) on delete cascade,
  receiver_id uuid not null references public.profiles(id) on delete cascade,
  body text not null check (char_length(body) between 1 and 1000),
  created_at timestamptz not null default now(),
  read_at timestamptz,
  check (sender_id <> receiver_id)
);

create index on public.posts (user_id, created_at desc);
create index on public.likes (user_id);
create index on public.comments (post_id, created_at);
create index on public.follows (following_id);
create index on public.saves (user_id);
create index on public.stories (user_id, created_at desc);
create index on public.stories (expires_at);
create index on public.messages (sender_id, created_at desc);
create index on public.messages (receiver_id, created_at desc);

alter table public.profiles enable row level security;
alter table public.posts enable row level security;
alter table public.likes enable row level security;
alter table public.comments enable row level security;
alter table public.follows enable row level security;
alter table public.saves enable row level security;
alter table public.stories enable row level security;
alter table public.messages enable row level security;

create policy "profiles readable" on public.profiles for select using (true);
create policy "profiles update own" on public.profiles for update to authenticated using ((select auth.uid()) = id) with check ((select auth.uid()) = id);
create policy "posts readable" on public.posts for select using (true);
create policy "posts insert own" on public.posts for insert to authenticated with check ((select auth.uid()) = user_id);
create policy "posts delete own" on public.posts for delete to authenticated using ((select auth.uid()) = user_id);
create policy "likes readable" on public.likes for select using (true);
create policy "likes insert own" on public.likes for insert to authenticated with check ((select auth.uid()) = user_id);
create policy "likes delete own" on public.likes for delete to authenticated using ((select auth.uid()) = user_id);
create policy "comments readable" on public.comments for select using (true);
create policy "comments insert own" on public.comments for insert to authenticated with check ((select auth.uid()) = user_id);
create policy "comments delete own" on public.comments for delete to authenticated using ((select auth.uid()) = user_id);
create policy "follows readable" on public.follows for select using (true);
create policy "follows insert own" on public.follows for insert to authenticated with check ((select auth.uid()) = follower_id);
create policy "follows delete own" on public.follows for delete to authenticated using ((select auth.uid()) = follower_id);
create policy "saves read own" on public.saves for select to authenticated using ((select auth.uid()) = user_id);
create policy "saves insert own" on public.saves for insert to authenticated with check ((select auth.uid()) = user_id);
create policy "saves delete own" on public.saves for delete to authenticated using ((select auth.uid()) = user_id);
create policy "stories readable until expiry" on public.stories for select using (expires_at > now());
create policy "stories insert own" on public.stories for insert to authenticated with check ((select auth.uid()) = user_id);
create policy "stories delete own" on public.stories for delete to authenticated using ((select auth.uid()) = user_id);
create policy "messages read own" on public.messages for select to authenticated using ((select auth.uid()) = sender_id or (select auth.uid()) = receiver_id);
create policy "messages send as self" on public.messages for insert to authenticated with check ((select auth.uid()) = sender_id);
create policy "messages mark read" on public.messages for update to authenticated using ((select auth.uid()) = receiver_id) with check ((select auth.uid()) = receiver_id);

create or replace function public.handle_new_user()
returns trigger language plpgsql security definer set search_path = '' as $$
begin
  insert into public.profiles (id, username, full_name)
  values (new.id,
          lower(coalesce(new.raw_user_meta_data->>'username', 'user' || substr(new.id::text, 1, 8))),
          new.raw_user_meta_data->>'full_name');
  return new;
end $$;
revoke execute on function public.handle_new_user() from public, anon, authenticated;
create trigger on_auth_user_created after insert on auth.users
  for each row execute function public.handle_new_user();

alter publication supabase_realtime add table public.messages;

insert into storage.buckets (id, name, public) values ('posts', 'posts', true) on conflict do nothing;
create policy "posts images upload own folder" on storage.objects for insert to authenticated
  with check (bucket_id = 'posts' and (storage.foldername(name))[1] = (select auth.uid())::text);
create policy "posts images delete own" on storage.objects for delete to authenticated
  using (bucket_id = 'posts' and (storage.foldername(name))[1] = (select auth.uid())::text);
