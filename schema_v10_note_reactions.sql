-- v10: likes / emoji reactions on notes (one reaction per person per note)
create table if not exists public.note_reactions (
  note_user  uuid not null references public.profiles(id) on delete cascade,
  user_id    uuid not null references public.profiles(id) on delete cascade,
  emoji      text not null check (char_length(emoji) between 1 and 16),
  created_at timestamptz not null default now(),
  primary key (note_user, user_id)
);
alter table public.note_reactions enable row level security;
grant select, insert, update, delete on public.note_reactions to authenticated;

drop policy if exists "nr read" on public.note_reactions;
create policy "nr read" on public.note_reactions for select to authenticated
  using (user_id = (select auth.uid()) or note_user = (select auth.uid()));
drop policy if exists "nr insert" on public.note_reactions;
create policy "nr insert" on public.note_reactions for insert to authenticated with check (user_id = (select auth.uid()));
drop policy if exists "nr update" on public.note_reactions;
create policy "nr update" on public.note_reactions for update to authenticated
  using (user_id = (select auth.uid())) with check (user_id = (select auth.uid()));
drop policy if exists "nr delete" on public.note_reactions;
create policy "nr delete" on public.note_reactions for delete to authenticated
  using (user_id = (select auth.uid()) or note_user = (select auth.uid()));

notify pgrst, 'reload schema';
