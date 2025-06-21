CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  cpf TEXT NOT NULL UNIQUE,
  password TEXT NOT NULL
);

INSERT INTO users (name, cpf, password) VALUES ('Admin', '12345678900', 'admin123');

CREATE TABLE IF NOT EXISTS topic (
  id SERIAL PRIMARY KEY,
  creator_id INTEGER REFERENCES users(id),
  name TEXT NOT NULL,
  open BOOLEAN DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS voting_session (
  id SERIAL PRIMARY KEY,
  topic_id INTEGER REFERENCES topic(id),
  user_id INTEGER REFERENCES users(id),
  vote BOOLEAN NOT NULL,
  UNIQUE(user_id, topic_id) 
);
