use ig_clone;

show tables;

describe users;

-- 1) Find 5 oldest users of instagram from database provided

select * from users order by created_at limit 5; 

-- 2) Find users who never posted single photo on instagram
-- select * from photos limit 10;
select * from users u left join photos p 
on u.id = p.user_id where image_url is NULL order by u.username;

-- 3) Identify the winner of contest and provide their details to team
select users.username, likes.photo_id, likes.created_at as image_posted_date, 
photos.image_url, count(likes.user_id) as total_likes from likes 
inner join photos on likes.photo_id = photos.id
inner join users on photos.user_id = users.id
group by likes.photo_id, users.username 
order by total_likes desc;

-- 4) Identify and suggest the top 5 most commonly used hashtags on the platform 

select * from photo_tags limit 20;

select * from tags limit 20;
