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