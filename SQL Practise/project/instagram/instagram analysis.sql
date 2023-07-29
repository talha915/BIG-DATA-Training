use ig_clone;

show tables;

describe users;

-- 1) Find 5 oldest users of instagram from database provided

select * from users order by created_at limit 5; 

-- 2) Find users who never posted single photo on instagram
-- select * from photos limit 10;

select * from users u left join photos p 
on u.id = p.user_id where image_url is NULL order by u.username;

