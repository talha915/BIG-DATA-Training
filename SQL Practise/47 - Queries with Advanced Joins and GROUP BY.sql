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


-- Proper Format

SELECT
    offices.country,
    offices.city,
    employees.email,
    employees.jobTitle,
    COUNT(employees.employeeNumber) AS number_of_employees
FROM
    offices
INNER JOIN
    employees ON offices.officeCode = employees.officeCode
GROUP BY
    offices.country,
    offices.city,
    employees.jobTitle
ORDER BY
    offices.country DESC,
    offices.city ASC;
 