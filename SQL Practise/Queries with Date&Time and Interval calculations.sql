-- Queries with Date/Time and Interval calculations

-- Current Date and Time
select now() as current_time_date;

-- Date Difference
SELECT DATEDIFF('2023-06-01', '2022-06-01') as date_diff; 

select datediff(now(), '2021/06/01') as date_diff;

-- Date Addition
SELECT DATE_ADD('2023-07-20', INTERVAL 7 DAY) as date_after_7_days;

-- Date Subtraction
select date_sub('2023-07-20', INTERVAL 12 DAY) AS DATE_BEFORE_12_DAYS; 

-- Date format
select date_format('2023-06-09', '%Y/%m/%d') as full_date;

-- Date Extraction
select year('2023-07-20') as year_no;
select month('2023-07-20') as month_no;
select day('2023-07-20') as day_no;

use classicmodels;


select * from payments ;

select * from payments where
paymentDate Between '2004-12-31' AND '2005-02-20';


select * from payments where
year(paymentDate) between '2005' and '2006';