select * from classicmodels.orderdetails limit 10;

-- Row Number 
select *, row_number() over (order by priceEach desc) as row_num
from classicmodels.orderdetails;

-- WIndow function sum
select *, sum(priceEach) over(order by orderNumber) as total_sum
from classicmodels.orderdetails;