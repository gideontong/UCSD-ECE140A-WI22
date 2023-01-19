UPDATE teachers SET name='Ramsin' WHERE name='Hoover';

SELECT * FROM courses INNER JOIN teachers ON courses.teacher_id = teachers.id;
