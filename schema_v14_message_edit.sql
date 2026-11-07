-- v14: let people edit their own text messages (Edit option in the long-press menu)
-- Supabase -> SQL Editor -> paste -> Run   (safe to run many times)
drop policy if exists "messages edit own" on public.messages;
create policy "messages edit own" on public.messages for update to authenticated
  using ((select auth.uid()) = sender_id) with check ((select auth.uid()) = sender_id);
notify pgrst, 'reload schema';
