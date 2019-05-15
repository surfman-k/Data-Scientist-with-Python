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
