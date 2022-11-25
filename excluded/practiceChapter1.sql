/* 1.	Determine the structure of 
the departments table 
and its contents */
desc departments

/* 2.	Determine the structure of 
the employees table. The HR department 
wants a query to display 
the last name, job code, hire date 
and employee number for each employee, 
with employee number appearing first. 
Provide an alias 
startdate for the hire_date column. */
select employee_id, last_name, job_id, hire_date as startdate 
from employees;

/* 3.	The HR department needs a query 
to display all unique job codes from the 
employees table.*/
select distinct job_id from employees;

/* 4.	The HR department wants more 
descriptive column headings for its report 
on employees. Copy the statement from 
lab_01_02 and name the column headings 
as EMP#, Employee, Job and Hire date. */

/* 5.	The HR department has requested 
a report of all employees and their job IDs. 
Display the last name concatenated with the 
job ID (separated by a comma and space) and 
name the column Employee and Title. */

/*6.	To familiarize yourself with the data 
in the Employees table, create a query to display 
all the data from that table. Separate each column 
output by a comma. Name the column title THE_OUTPUT. */
