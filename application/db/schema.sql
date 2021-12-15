DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS tokens;

CREATE TABLE users (
  id varchar PRIMARY KEY,
  username TEXT NOT NULL,
  email varchar UNIQUE NOT NULL,
  password TEXT NOT NULL,
  about TEXT
);

CREATE TABLE tokens (
  tokenId INTEGER PRIMARY KEY AUTOINCREMENT,
  token varchar,
  tokenExpiration DATETIME,
  userId varchar,
  FOREIGN KEY (userId) references users(id)
);
