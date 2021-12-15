DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS tokens;

CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT NOT NULL,
  email varchar UNIQUE NOT NULL,
  password TEXT NOT NULL,
  about TEXT
);

CREATE TABLE tokens (
  tokenId INTEGER PRIMARY KEY AUTOINCREMENT,
  token varchar,
  tokenExpiration DATETIME,
  userId INTEGER,
  FOREIGN KEY (userId) references users(id)
);
