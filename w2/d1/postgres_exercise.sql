/* SQL Exercise
====================================================================
We will be working with database northwind.db we have set up and connected to in the activity Connect to Remote PostgreSQL Database earlier.


-- MAKE YOURSELF FAIMLIAR WITH THE DATABASE AND TABLES HERE





--==================================================================
/* TASK I
-- Q1. Write a query to get Product name and quantity/unit.
*/

SELECT ProductName, unitsinstock FROM products;
/* TASK II
Q2. Write a query to get most expense and least expensive Product list (name and unit price)
*/

-- SELECT MIN(unitprice) as least_expensive, MAX(unitprice) as most_expensive
-- FROM products;


SELECT productname, unitprice FROM products ORDER BY unitprice;


/* TASK III
Q3. Write a query to count current and discontinued products.
*/

SELECT discontinued, count(*) FROM products GROUP BY discontinued
-- should these be labeled?

/* TASK IV
Q4. Select all product names and their category names (77 rows)
*/
SELECT products.productname, categories.categoryname FROM products
JOIN categories ON categories.categoryid = products.categoryid;


/* TASK V
Q5. Select all product names, unit price and the supplier region that don't have suppliers from USA region. (26 rows)
*/
SELECT products.productname, products.unitprice, suppliers.region from products
JOIN suppliers ON suppliers.supplierid = products.supplierid
WHERE region != 'USA';
-- not region USA is actuallu NULL

/* TASK VI
Q6. Get the total quantity of orders sold.( 51317)
*/
SELECT count(orderid) FROM orders;
-- 830
SELECT count(productid) FROM order_details;
-- 2155 products... abbrev
SELECT SUM(quantity) FROM order_details 
--- 51317 - is the number of products in all the orders


/* TASK VII
Q7. Get the total quantity of orders sold for each order.(830 rows)
*/
SELECT count(orderid) FROM orders;
-- 830

/* TASK VIII
Q8. Get the number of employees who have been working more than 5 year in the company. (9 rows)
*/



select count(*) 
from (
  select firstname, lastname, current_date, hiredate from employees where (current_date - hiredate) > 5
) as a