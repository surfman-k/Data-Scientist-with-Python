/* TABLES */

SELECT 'DataCamp <3 SQL'
AS result;


SELECT 'SQL is cool!'
AS result;

/* TYPICAL SELECTS */

Select title from films;
Select release_year from films;
Select name from people;

SELECT title, release_year, country
FROM films;

SELECT *
FROM films;

/* SELECT DISTINCT */

SELECT DISTINCT country
FROM films;
SELECT DISTINCT certification
FROM films;
SELECT DISTINCT role
FROM roles;

/* COUNTS */

SELECT COUNT(*)
FROM people;

SELECT COUNT(DISTINCT language)
FROM films;

/* WHERE */

SELECT *
FROM films
WHERE release_year = 2016;

/* FILTERING */

SELECT COUNT(*)
FROM films
WHERE release_year < 2000;

SELECT title, release_year
FROM films
WHERE release_year > 2000;
