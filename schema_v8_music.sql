-- music column for posts / reels / stories (safe to run many times)
alter table public.posts   add column if not exists music jsonb;
alter table public.stories add column if not exists music jsonb;
notify pgrst, 'reload schema';
