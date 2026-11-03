-- v8: music on posts / reels / stories + make sure owners can delete their own rows
alter table public.posts   add column if not exists music jsonb;
alter table public.stories add column if not exists music jsonb;

drop policy if exists "posts delete own" on public.posts;
create policy "posts delete own" on public.posts for delete to authenticated using ((select auth.uid()) = user_id);
drop policy if exists "stories delete own" on public.stories;
create policy "stories delete own" on public.stories for delete to authenticated using ((select auth.uid()) = user_id);
