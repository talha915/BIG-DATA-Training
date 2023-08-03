use classicmodels;

select * from customers limit 20;
select * from orders limit 20;
select * from orderdetails limit 20;

select customers.customerName, customers.customerNumber, orders.orderNumber, orders.status,
sum(orderdetails.priceEach) as cumulative_prices
from customers inner join orders
on customers.customerNumber = orders.customerNumber
inner join orderdetails
on orders.orderNumber = orderdetails.orderNumber
group by customers.customerName, customers.customerNumber, orders.orderNumber, orders.status;

-- 					Trying with window functions									-- 
SELECT
	customers.customerName, 
    customers.customerNumber, 
    orders.orderNumber, 
    orders.status,
	sum(orderdetails.priceEach) OVER (PARTITION BY customers.customerName, customers.customerNumber, orders.orderNumber, orders.status) as cumulative_prices
from 
	customers 
inner join 
	orders on customers.customerNumber = orders.customerNumber
inner join 
	orderdetails on orders.orderNumber = orderdetails.orderNumber;
    
-- 					Trying with window functions									-- 
SELECT 
  customers.customerName,
  customers.customerNumber,
  orders.orderNumber,
  orders.status,
  SUM(orderdetails.priceEach) OVER (PARTITION BY customers.customerNumber, orders.orderNumber) as cumulative_prices
FROM 
  customers
INNER JOIN 
  orders ON customers.customerNumber = orders.customerNumber
INNER JOIN 
  orderdetails ON orders.orderNumber = orderdetails.orderNumber;
