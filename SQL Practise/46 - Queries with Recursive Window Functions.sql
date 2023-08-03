WITH RECURSIVE numbers AS (
  SELECT 1 AS n -- Initial Condition
  UNION ALL
  SELECT n + 1 FROM numbers WHERE n < 10 -- Recursive Condition
)

SELECT * FROM numbers;

WITH RECURSIVE numbers AS (
	SELECT 2 AS recursive_number
    UNION ALL
    SELECT recursive_number * 2 FROM numbers WHERE recursive_number <= 10
)
SELECT * FROM numbers;



WITH RECURSIVE table_of_2 AS (
	SELECT 1 AS counter, 2 AS base_number
    UNION ALL
    SELECT counter + 1, base_number from table_of_2 where counter < 10
)
SELECT base_number, counter, base_number*counter as multiple from table_of_2;