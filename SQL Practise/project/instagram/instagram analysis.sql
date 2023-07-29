use ig_clone;

show tables;

describe users;

-- Find 5 oldest users of instagram from database provided

select * from users order by created_at limit 5; 