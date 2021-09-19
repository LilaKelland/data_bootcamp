/* SQL Stretch Exercise
====================================================================
We will be working with database chinook.db
You can download it here: https://drive.google.com/file/d/0Bz9_0VdXvv9bWUtqM0NBYzhKZ3c/view?usp=sharing

 The Chinook Database is about an imaginary video and music store. Each track is stored using one of the digital formats and has a genre. The store has also some playlists, where a single track can be part of several playlists. Orders are recorded for customers, but are called invoices. Every customer is assigned a support employee, and Employees report to other employees.
*/



--==================================================================
/* TASK I
How many audio tracks in total were bought by German customers? And what was the total price paid for them?
hint: use subquery to find all of tracks with their prices
*/
SELECT customers.CustomerId, COUNT(invoice_items.InvoiceLineId) as NumItems, SUM(invoice_items.UnitPrice) as totalSpent, invoice_items.Quantity  FROM customers
JOIN invoices ON invoices.CustomerId = customers.CustomerId
JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId
JOIN tracks ON invoice_items.TrackId = tracks.TrackId
WHERE customers.Country = 'Germany' 
GROUP BY customers.CustomerId

-- SELECT customers.CustomerId, tracks.UnitPrice, invoices.InvoiceId, invoice_items.InvoiceLineId, invoice_items.UnitPrice, invoice_items.Quantity  FROM customers
-- JOIN invoices ON invoices.CustomerId = customers.CustomerId
-- JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId
-- JOIN tracks ON invoice_items.TrackId = tracks.TrackId
-- WHERE customers.Country = 'Germany' 


/* TASK II
What is the space, in bytes, occupied by the playlist “Grunge”, and how much would it cost?
(Assume that the cost of a playlist is the sum of the price of its constituent tracks).
*/
SELECT playlists.Name, SUM(tracks.UnitPrice) as TotalPrice, SUM(tracks.Bytes) as TotalBytes from playlists 
JOIN playlist_track ON playlists.PlaylistId = playlist_track.PlaylistId
JOIN tracks ON tracks.TrackId = playlist_track.TrackId
WHERE playlists.Name = 'Grunge'
GROUP BY playlists.PlaylistId

/* TASK III
List the names and the countries of those customers who are supported by an employee who was younger than 35 when hired. 
*/

SELECT customers.FirstName, customers.LastName, customers.Country FROM customers
JOIN employees ON employees.EmployeeId = customers.SupportRepId
WHERE customers.SupportRepId IN 
(SELECT employees.EmployeeId FROM employees WHERE (employees.HireDate - employees.BirthDate) <35)

