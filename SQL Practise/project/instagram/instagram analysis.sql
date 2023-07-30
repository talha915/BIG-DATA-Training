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
select tags.tag_name, count(photo_tags.tag_id) as count_of_tags, tags.created_at 
from tags inner join photo_tags 
on tags.id = photo_tags.tag_id
group by tags.tag_name
order by count_of_tags desc limit 5; 


-- 5) What day of week do most users register on? Provide when to schedule an ad campaign
select date_format(created_at, "%W") as day_of_week, count(username) as registered_user
from users
group by day_of_week
order by registered_user desc, day_of_week asc; 


-- 6) Provide how many times does average user post on instagram. Also, provide the total number of
-- photos on instagram / total number of users 
select * from photos;
select * from users;

with posted_users as(
	select users.id as user_id, users.username, count(photos.id) as registered_posts
    from users left join photos
    on users.id = photos.user_id
    group by users.id
    order by registered_posts desc
)
select sum(registered_posts) as total_photos, count(user_id) total_users, 
sum(registered_posts)/count(user_id) as per_user from posted_users;