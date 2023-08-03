use classicmodels;
show tables;

-- select * from employees limit 20;
-- select * from offices limit 20;

select offices.country, offices.city, employees.email, 
employees.jobTitle, count(employees.employeeNumber) as number_of_employees
from offices inner join employees
on offices.officeCode = employees.officeCode
group by offices.country, offices.city, employees.jobTitle 
order by country desc, city asc;