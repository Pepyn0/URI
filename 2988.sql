--- URI Online Judge SQL
--- By Edivânia Pontes
--- Problem 2988

create table teams(
  id INTEGER PRIMARY KEY,
  name VARCHAR (50)
);

create table matches(
  id INTEGER PRIMARY KEY,
  team_1 INTEGER REFERENCES teams (id),
  team_2 INTEGER REFERENCES teams (id),
  team_1_goals INTEGER,
  team_2_goals INTEGER
);

INSERT INTO teams(id, name)
VALUES 
       (1, 'CEARA'),
       (2, 'FORTALEZA'),
       (3, 'GUARANY DE SOBRAL'),
       (4, 'FLORESTA');

INSERT INTO matches(id, team_1, team_2, team_1_goals, team_2_goals)
VALUES 
       (1, 4, 1, 0, 4),
       (2, 3, 2, 0, 1),
       (3, 1, 3, 3, 0),
       (4, 3, 4, 0, 1),
       (5, 1, 2, 0, 0),
       (6, 2, 4, 2, 1);

  /*  Execute this query to drop the tables */
  -- DROP TABLE teams, matches; --

-- SOLUÇÃO --

SELECT
	(SELECT T.name FROM teams T WHERE T.id = teams.id)
	AS "name",

	(SELECT COUNT(team_1) FROM matches
		WHERE team_1 = teams.id) +
	(SELECT COUNT(team_2) FROM matches
		WHERE team_2 = teams.id)
	AS "matches",

	(SELECT SUM(CASE WHEN team_1_goals > team_2_goals THEN 1 ELSE 0 END) AS "victories" FROM matches, teams T
		WHERE T.id = matches.team_1 AND T.id = teams.id) +
	(SELECT SUM(CASE WHEN team_2_goals > team_1_goals THEN 1 ELSE 0 END) FROM matches, teams T
		WHERE T.id = matches.team_2 AND T.id = teams.id)
	AS "victories",

	(SELECT SUM(CASE WHEN team_2_goals > team_1_goals THEN 1 ELSE 0 END) AS "defeats" FROM matches, teams T
		WHERE matches.team_1 = T.id AND T.id = teams.id) +
	(SELECT SUM(CASE WHEN team_1_goals > team_2_goals THEN 1 ELSE 0 END) FROM matches, teams T
		WHERE matches.team_2 = T.id AND T.ID = teams.id)
	AS "defeats",

	(SELECT SUM(CASE WHEN team_1_goals = team_2_goals THEN 1 ELSE 0 END) AS "draws" FROM matches, teams T
		WHERE matches.team_1 = T.id AND T.id = teams.id) +
	(SELECT SUM(CASE WHEN team_1_goals = team_2_goals THEN 1 ELSE 0 END) FROM matches, teams T
		WHERE matches.team_2 = T.id AND T.id = teams.id)
	AS "draws",

	(SELECT SUM(CASE WHEN team_1_goals > team_2_goals THEN 3 WHEN team_1_goals = team_2_goals THEN 1 ELSE 0 END) AS "score" FROM matches, teams T
		WHERE matches.team_1 = T.id AND T.id = teams.id) +
	(SELECT SUM(CASE WHEN team_2_goals > team_1_goals THEN 3 WHEN team_2_goals = team_1_goals THEN 1 ELSE 0 END) FROM matches, teams T
		WHERE matches.team_2 = T.id AND T.id = teams.id)
	AS "score"


FROM teams ORDER BY score DESC;