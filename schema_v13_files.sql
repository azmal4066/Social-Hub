-- Social Hub v13: message options (Edit + Delete for you sync). Run ONCE in Supabase > SQL Editor. Safe to re-run.
-- Long-press menu works without this (Delete for you falls back to this device), but run it so
-- "Delete for you" syncs across devices and "Edit" is allowed.

create table if not exists public.message_hidden (
  user_id uuid not null references public.profiles(id) on delete cascade,
  message_id uuid not null references public.messages(id) on delete cascade,
  created_at timestamptz not null default now(),
  primary key (user_id, message_id));
alter table public.message_hidden enable row level security;
drop policy if exists "mh own" on public.message_hidden;
create policy "mh own" on public.message_hidden for all to authenticated
  using ((select auth.uid()) = user_id) with check ((select auth.uid()) = user_id);

-- sender can edit their own message text (edit flag is stored in messages.meta)
drop policy if exists "messages edit own" on public.messages;
create policy "messages edit own" on public.messages for update to authenticated
  using ((select auth.uid()) = sender_id) with check ((select auth.uid()) = sender_id);

notify pgrst, 'reload schema';
