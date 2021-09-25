/* SQL Exercise
====================================================================
We will be working with database imdb.db
You can download it here: https://drive.google.com/file/d/1E3KQDdGJs4a0i1RoYb8DEq0PFxCgI6cN/view?usp=sharing
*/


-- MAKE YOURSELF FAIMLIAR WITH THE DATABASE AND TABLES HERE

SELECT schema_name FROM information_schema.schemata

SELECT nspname FROM pg_catalog.pg_namespace;
SELECT * FROM movies

SELECT * from distributors
SELECT distributor_id, name FROM distributors where name = 'Universal Pictures'
--==================================================================
/* TASK I
 Find the id's of movies that have been distributed by “Universal Pictures”.
*/
SELECT movies.movie_id, movies.title FROM movies
JOIN movie_distributors on movies.movie_id = movie_distributors.movie_id
JOIN distributors ON distributors.distributor_id = movie_distributors.distributor_id
WHERE distributors.distributor_id IN (SELECT distributor_id FROM distributors where name = 'Universal Pictures')


/* TASK II
 Find the name of the companies that distributed movies released in 2006.
*/

SELECT distributors.name, movies.title, movies.year FROM movies
JOIN movie_distributors on movies.movie_id = movie_distributors.movie_id
JOIN distributors ON distributors.distributor_id = movie_distributors.distributor_id
WHERE movies.year = "2006"


/* TASK III
Find all pairs of movie titles released in the same year, after 2010.
hint: use self join on table movies.
*/
SELECT * FROM movies WHERE year > 2010
SELECT * FROM aka_titles


/* TASK IV
 Find the names and movie titles of directors that also acted in their movies.
*/


SELECT movies.title, movies.movie_id, people.person_id, people.name, roles.role FROM movies JOIN directors ON directors.movie_id = movies.movie_id 
JOIN people ON people.person_id = directors.person_id
JOIN roles ON roles.person_id = directors.person_id AND roles.movie_id = directors.movie_id


/* TASK V
Find ALL movies realeased in 2011 and their aka titles.
hint: left join
*/

SELECT * from aka_names
SELECT * from aka_titles

SELECT movies.title, movies.movie_id, aka_titles.title FROM movies LEFT JOIN aka_titles 
ON aka_titles.movie_id = movies.movie_id WHERE movies.year = '2011'


/* TASK VI
Find ALL movies realeased in 1976 OR 1977 and their composer's name.
*/

SELECT * FROM composers

SELECT movies.title, people.name FROM movies 
JOIN COMPOSERS ON movies.movie_id = composers.movie_id
JOIN people ON composers.person_id = people.person_id
WHERE movies.year = 1976 or movies.year = 1977


/* TASK VII
Find the most popular movie genres.
*/

SELECT * from genres
SELECT * FROM movie_genres

SELECT count(movies.movie_id) as numb,  genres.label FROM movies 
JOIN movie_genres ON movie_genres.movie_id = movies.movie_id
JOIN genres ON genres.genre_id = movie_genres.genre_id
GROUP BY genres.label
ORDER BY numb DESC
LIMIT 3

SELECT 

/* TASK VIII
Find the people that achieved the 10 highest average ratings for the movies 
they cinematographed.
*/
SELECT * FROM cinematographers
SELECT * FROM movies

SELECT COUNT(movies.rating) as num_movies, AVG(movies.rating) as avg_rating, people.name from movies 
JOIN cinematographers ON movies.movie_id = cinematographers.movie_id
JOIN people ON people.person_id = cinematographers.person_id
GROUP BY people.name
ORDER BY avg_rating DESC
LIMIT 10

/* TASK IX
Find all countries which have produced at least one movie with a rating higher than
8.5.
hint: subquery
*/
SELECT DISTINCT(countries.name) from countries 
JOIN movie_countries ON countries.country_id = movie_countries.country_id
JOIN movies ON movie_countries.movie_id = movies.movie_id
WHERE movies.movie_id IN (SELECT movie_id from movies WHERE rating >8.5)


/* TASK X
Find the highest-rated movie, and report its title, year, rating, and country. There
can be ties; if so, you should report for each of them.
*/

SELECT movies.title, movies.rating, movies.year, countries.name from movies 
JOIN movie_countries ON movie_countries.movie_id = movies.movie_id
JOIN countries ON countries.country_id = movie_countries.country_id
ORDER by movies.rating DESC
LIMIT 1


/* STRETCH BONUS
Find the pairs of people that have directed at least 5 movies and whose 
carees do not overlap (i.e. The release year of a director's last movie is 
lower than the release year of another director's first movie).
*/
SELECT people.name, people.person_id, movies.year, movies.title from directors 
JOIN people ON directors.person_id = people.person_id
JOIN movies ON movies.movie_id = directors.movie_id 
WHERE people.person_id IN (SELECT person_id from (SELECT directors.person_id, COUNT(directors.movie_id) as num_movies 
from directors
GROUP BY person_id)
WHERE num_movies > 5 )

-- person_id and num_movies
SELECT person_id from (SELECT directors.person_id, COUNT(directors.movie_id) as num_movies 
from directors
GROUP BY person_id)
WHERE num_movies > 5 


