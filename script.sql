CREATE TABLE admins (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  country TEXT NOT NULL,
  gender TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  password_hash TEXT NOT NULL
);


CREATE TABLE providers (
  id SERIAL PRIMARY KEY,
  company_name TEXT NOT NULL,
  contact_person TEXT,
  email TEXT,
  type TEXT,
  nit TEXT,
  phone TEXT,
  city TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

