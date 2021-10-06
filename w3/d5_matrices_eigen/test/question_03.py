"""
 - Connect to the hr.db (stored in supporting-files directory) with sqlite3 
 - Write a query to find the names (first_name, last_name) of the employees who have a manager who works for a department based in the United States. 
 

Expected columns:
    - first_name	
    - last_name	
    - manager_od

Notes:
    - Use tables employees, departments and locations
    - You shouldn’t use JOINs here. 
    - You can connect to DB from Jupyter Lab/Notebook, explore the table and try different queries
    - In the variable 'SQL' store only the final query ready for validation 
"""


SQL = '''SELECT employees.first_name, employees.last_name, manager_id
FROM employees WHERE manager_id in (
SELECT manager_id FROM employees
WHERE department_id IN (SELECT department_id FROM departments 
WHERE location_id IN (SELECT location_id
FROM locations WHERE country_id = 'US')))'''