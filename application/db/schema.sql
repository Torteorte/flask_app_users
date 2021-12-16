DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS tokens;

CREATE TABLE users (
  id varchar PRIMARY KEY,
  username varchar NOT NULL,
  email varchar UNIQUE NOT NULL,
  password varchar NOT NULL,
  about varchar
);

CREATE TABLE tokens (
  tokenId INTEGER PRIMARY KEY AUTOINCREMENT,
  token varchar NOT NULL,
  tokenExpiration DATETIME NOT NULL,
  userId varchar NOT NULL,
  FOREIGN KEY (userId) references users(id)
);
