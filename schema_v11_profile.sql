-- v11: extra profile fields
alter table public.profiles
  add column if not exists pronouns text default '',
  add column if not exists links jsonb not null default '[]'::jsonb,
  add column if not exists banners jsonb not null default '[]'::jsonb,
  add column if not exists gender text default '',
  add column if not exists ai_profile boolean not null default false,
  add column if not exists is_professional boolean not null default false,
  add column if not exists category text default '',
  add column if not exists grid_order jsonb not null default '[]'::jsonb;
notify pgrst, 'reload schema';
