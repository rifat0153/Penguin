1. List all courses.name and teachers.name.

SELECT name FROM courses;
SELECT name FROM teachers;

2. List teachers who take the highest number of courses.

SELECT COUNT(c.name),t.name
FROM courses as c 
inner join teachers as t
ON c.teacher_id=t.id
GROUP BY t.name
ORDER BY COUNT(c.name) DESC LIMIT 1 ;


3.List teachers who dont take any course.

SELECT t1.name FROM teachers as t1
WHERE t1.name NOT IN
(SELECT t.name FROM courses as c
inner join teachers as t
ON t.id = c.teacher_id)
;