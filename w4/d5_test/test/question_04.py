"""
 - Connect to the hr.db (stored in supporting-files directory) with sqlite3 
 - Write a query to get the department name and number of employees in the department.
 - Sort the data by number of employees starting from the highest.



Expected columns:
    - department_name
    - number_of_employees

Notes:
    - Use tables employees and departments
    - You can connect to DB from Jupyter Lab/Notebook, explore the table and try different queries
    - In the variable 'SQL' store only the final query ready for validation 
"""


SQL = """SELECT departments.department_name, COUNT(employee_id) as number_of_employees FROM employees 
JOIN departments ON departments.department_id = employees.department_id
GROUP BY departments.department_name
ORDER BY number_of_employees DESC"""