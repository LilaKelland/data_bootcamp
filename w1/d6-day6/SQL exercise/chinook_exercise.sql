/* SQL Exercise
====================================================================
We will be working with database chinook.db
You can download it here: https://drive.google.com/file/d/0Bz9_0VdXvv9bWUtqM0NBYzhKZ3c/view?usp=sharing

 The Chinook Database is about an imaginary video and music store. Each track is stored using one of the digital formats and has a genre. The store has also some playlists, where a single track can be part of several playlists. Orders are recorded for customers, but are called invoices. Every customer is assigned a support employee, and Employees report to other employees.
*/


-- MAKE YOURSELF FAIMLIAR WITH THE DATABASE AND TABLES HERE





--==================================================================
/* TASK I
Which artists did not make any albums at all? Include their names in your answer.
*/
SELECT artists.Name, artists.ArtistId FROM artists 
JOIN albums ON albums.ArtistId = artists.ArtistId
WHERE artists.ArtistId NOT IN (SELECT albums.ArtistId FROM albums);
# no artists

/* TASK II
Which artists recorded any tracks of the Latin genre?
*/
SELECT DISTINCT(artists.Name) FROM artists
JOIN albums ON artists.ArtistId = albums.ArtistId
JOIN tracks ON albums.AlbumId = tracks.TrackId
JOIN genres ON genres.GenreId = tracks.GenreId
WHERE genres.Name = 'Latin';

/* TASK III
Which video track has the longest length?
*/
-- Find media type - video
SELECT media_types.name, media_types.MediaTypeId FROM media_types

SELECT tracks.Name, MAX(tracks.Milliseconds) FROM tracks
JOIN media_types ON media_types.MediaTypeId = tracks.MediaTypeId
WHERE media_types.MediaTypeId = 3


/* TASK IV
Find the names of customers who live in the same city as the top employee (The one not managed by anyone).
*/

SELECT customers.FirstName, customers.LastName, customers.city
FROM employees 
JOIN customers ON customers.SupportRepId = employees.EmployeeId
WHERE customers.City = 
(SELECT employees.City FROM employees WHERE ReportsTo IS NULL)


-- WHERE employees.ReportsTo = NULL
/* TASK V
Find the managers of employees supporting Brazilian customers.
*/
SELECT managers.FirstName, managers.LastName FROM employees 
JOIN customers ON customers.SupportRepId = employees.EmployeeId
JOIN employees managers ON employees.ReportsTo = managers.EmployeeId
WHERE customers.Country = 'Brazil'
GROUP BY managers.LastName

-- SELECT * FROM customers WHERE Country = 'Brazil'
-- SELECT employees.EmployeeId, employees.ReportsTo FROM employees

/* TASK VI
Which playlists have no Latin tracks?
*/
SELECT playlists.Name, genres.Name FROM genres
JOIN tracks ON genres.GenreId = tracks.GenreId
JOIN playlist_track ON playlist_track.TrackId = tracks.TrackId
JOIN playlists ON playlists.PlaylistId = playlist_track.PlaylistId
WHERE genres.Name != 'Latin'
GROUP BY playlists.Name