-- Le DROP des tables est commenté car les tables ont ete crees, si on fait flask init-db sa va effacer les tables, on perds tout.
-- Il faut decommenter les DROPS si on veux creer  ou recreer les tables .
--DROP VIEW IF EXISTS matches_with_team_names;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS genre;
DROP TABLE IF EXISTS banques;
DROP TABLE IF EXISTS comptes;
DROP TABLE IF EXISTS mpayement;
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS libelle;
DROP TABLE IF EXISTS mouvements;


CREATE TABLE users(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nom TEXT NOT NULL,
  pernom TEXT NOT NULL,
  genre_id TEXT UNIQUE NOT NULL,
  email TEXT UNIQUE NOT NULL,
  password_hash TEXT NOT NULL,
  admin INTEGER NOT NULL 
);

CREATE TABLE genre(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL
);

CREATE TABLE banques(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nom TEXT NOT NULL
);

CREATE TABLE comptes(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  numero INTEGER UNIQUE NOT NULL,
  banque_id INTEGER  NOT NULL,
  description TEXT NOT NULL,
  mdepart INTEGER NOT NULL
);

CREATE TABLE mpayement(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nom TEXT UNIQUE NOT NULL,
  n_ref TEXT NULL
);

CREATE TABLE categories(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL
);

CREATE TABLE mouvements(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  date TIMESTAMP NOT NULL,
  libelle TEXT NOT NULL,
  compte_id INTEGER NOT NULL,
  mpayement_id INTEGER NOT NULL,
  FOREIGN KEY(compte_id) REFERENCES comptes(id) ON DELETE CASCADE
  FOREIGN KEY(mpayement_id) REFERENCES mpayement(id) ON DELETE CASCADE
);

--CREATE VIEW matches_with_team_names(id, date, score0, score1, team0, team1, team0_name, team1_name)
--AS SELECT matches.id, date, score0, score1, team0, team1, teams0.name, teams1.name from matches
--          INNER JOIN teams as teams0 ON teams0.id = team0
--          INNER JOIN teams as teams1 ON teams1.id = team1;
