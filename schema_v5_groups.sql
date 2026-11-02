-- Social Hub v5: group chats + message reactions. Run ONCE after schema_v4_chat.sql. Safe to re-run.
create table if not exists public.groups (
  id uuid primary key default gen_random_uuid(),
  name text not null check (char_length(name) between 1 and 50),
  created_by uuid not null references public.profiles(id) on delete cascade,
  theme text not null default '',
  disappear int not null default 0,
  created_at timestamptz not null default now());
create table if not exists public.group_members (
  group_id uuid not null references public.groups(id) on delete cascade,
  user_id uuid not null references public.profiles(id) on delete cascade,
  muted boolean not null default false,
  joined_at timestamptz not null default now(),
  primary key (group_id, user_id));
create index if not exists gm_user on public.group_members(user_id);

create or replace function public.is_group_member(gid uuid)
returns boolean language sql stable security definer set search_path = '' as $$
  select exists (select 1 from public.group_members m where m.group_id = gid and m.user_id = (select auth.uid()));
$$;
create or replace function public.is_group_owner(gid uuid)
returns boolean language sql stable security definer set search_path = '' as $$
  select exists (select 1 from public.groups g where g.id = gid and g.created_by = (select auth.uid()));
$$;

alter table public.groups enable row level security;
alter table public.group_members enable row level security;
drop policy if exists "groups read" on public.groups;
drop policy if exists "groups insert" on public.groups;
drop policy if exists "groups update" on public.groups;
create policy "groups read" on public.groups for select to authenticated using (public.is_group_member(id) or created_by = (select auth.uid()));
create policy "groups insert" on public.groups for insert to authenticated with check (created_by = (select auth.uid()));
create policy "groups update" on public.groups for update to authenticated using (public.is_group_member(id)) with check (public.is_group_member(id));
drop policy if exists "gm read" on public.group_members;
drop policy if exists "gm insert" on public.group_members;
drop policy if exists "gm update" on public.group_members;
drop policy if exists "gm delete" on public.group_members;
create policy "gm read" on public.group_members for select to authenticated using (public.is_group_member(group_id));
create policy "gm insert" on public.group_members for insert to authenticated with check (public.is_group_owner(group_id) or public.is_group_member(group_id));
create policy "gm update" on public.group_members for update to authenticated using (user_id = (select auth.uid())) with check (user_id = (select auth.uid()));
create policy "gm delete" on public.group_members for delete to authenticated using (user_id = (select auth.uid()) or public.is_group_owner(group_id));

-- messages: DM (receiver_id) or group (group_id)
alter table public.messages alter column receiver_id drop not null;
alter table public.messages add column if not exists group_id uuid references public.groups(id) on delete cascade;
alter table public.messages drop constraint if exists messages_target_chk;
alter table public.messages add constraint messages_target_chk check (num_nonnulls(receiver_id, group_id) = 1);
create index if not exists messages_group on public.messages(group_id, created_at);

drop policy if exists "messages read own" on public.messages;
create policy "messages read own" on public.messages for select to authenticated
  using ((expires_at is null or expires_at > now()) and (
    (select auth.uid()) = sender_id or (select auth.uid()) = receiver_id
    or (group_id is not null and public.is_group_member(group_id))));
drop policy if exists "messages send as self" on public.messages;
create policy "messages send as self" on public.messages for insert to authenticated
  with check ((select auth.uid()) = sender_id and (
    (group_id is null and not exists (select 1 from public.blocks b where (b.blocker_id = receiver_id and b.blocked_id = sender_id) or (b.blocker_id = sender_id and b.blocked_id = receiver_id)))
    or (group_id is not null and public.is_group_member(group_id))));

-- reactions
create table if not exists public.message_reactions (
  message_id uuid not null references public.messages(id) on delete cascade,
  user_id uuid not null references public.profiles(id) on delete cascade,
  emoji text not null check (char_length(emoji) between 1 and 16),
  primary key (message_id, user_id));
alter table public.message_reactions enable row level security;
drop policy if exists "mr read" on public.message_reactions;
drop policy if exists "mr insert" on public.message_reactions;
drop policy if exists "mr update" on public.message_reactions;
drop policy if exists "mr delete" on public.message_reactions;
create policy "mr read" on public.message_reactions for select to authenticated using (exists (select 1 from public.messages m where m.id = message_id));
create policy "mr insert" on public.message_reactions for insert to authenticated with check (user_id = (select auth.uid()) and exists (select 1 from public.messages m where m.id = message_id));
create policy "mr update" on public.message_reactions for update to authenticated using (user_id = (select auth.uid())) with check (user_id = (select auth.uid()));
create policy "mr delete" on public.message_reactions for delete to authenticated using (user_id = (select auth.uid()));

do $$ begin
  begin alter publication supabase_realtime add table public.groups; exception when duplicate_object then null; end;
  begin alter publication supabase_realtime add table public.group_members; exception when duplicate_object then null; end;
  begin alter publication supabase_realtime add table public.message_reactions; exception when duplicate_object then null; end;
end $$;
notify pgrst, 'reload schema';
