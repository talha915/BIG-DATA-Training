create database testing_db;

use testing_db;

create table customers(
    CustomerID int not null primary key,
    CustomerName varchar(50),	
    Country varchar(50)
);

insert into customers
(CustomerID, CustomerName, Country)
values
(1,'John','USA'),
(2,'Alice','Canada'),
(3,'Bob','UK'),
(4,'Eve','Australia'),
(5,'Carl','Germany');

create table orders(
	OrderID int not null primary key,	
	CustomerID int,
	OrderDate date,
	OrderAmount int not null
); 

Alter table orders add constraint fk_customer_id foreign key (CustomerID) references customers(CustomerID);

insert into orders 
(OrderID, CustomerID, OrderDate, OrderAmount)
values
(101,1,'2023-07-15',200)
,(102,1,'2023-07-18',300)
,(103,2,'2023-07-20',150)
,(104,3,'2023-07-22',1000)
,(105,1,'2023-07-25',250)
,(106,4,'2023-07-28',500)
,(107,3,'2023-07-30',800)
,(108,5,'2023-08-01',1200);

-- Question 1: Find the total order amount for each customer along with their names. 

select customers.CustomerID, customers.CustomerName, customers.Country, sum(orders.OrderAmount) as total_amount from customers 
inner join 
orders 
on orders.CustomerID = customers.CustomerID
group by customers.CustomerID, customers.CustomerName, customers.Country;

-- Question 2: Find the maximum order amount for each customer along with their names. 
select customers.CustomerID, customers.CustomerName, customers.Country, max(orders.OrderAmount) as max_order_amount from customers
inner join 
orders
on orders.CustomerID = customers.CustomerID
group by customers.CustomerID, customers.CustomerName, customers.Country;


-- Question 3: Find the number of orders placed by each customer along with their names. 
select customers.CustomerID, customers.CustomerName, customers.Country, count(orders.OrderAmount) as num_of_orders from customers
inner join 
orders
on orders.CustomerID = customers.CustomerID
group by customers.CustomerID, customers.CustomerName, customers.Country
order by num_of_orders desc;