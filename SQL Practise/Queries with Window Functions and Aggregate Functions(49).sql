select * from classicmodels.orderdetails limit 10;

select *, row_number() over (order by priceEach desc) as row_num
from classicmodels.orderdetails;