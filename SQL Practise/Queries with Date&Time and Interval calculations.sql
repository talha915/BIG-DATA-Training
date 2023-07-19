-- Queries with Date/Time and Interval calculations

-- Current Date and Time
select now() as current_time_date;

-- Date Difference
SELECT DATEDIFF('2023-06-01', '2022-06-01') as date_diff; 

select datediff(now(), '2021/06/01') as date_diff;