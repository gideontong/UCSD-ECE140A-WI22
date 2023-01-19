LOAD DATA INFILE '/home/gideon/firefox/teachers.csv'
    INTO TABLE teachers
    FIELDS TERMINATED BY ','
    ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS;

LOAD DATA INFILE '/home/gideon/firefox/grades.csv'
    INTO TABLE grades
    FIELDS TERMINATED BY ','
    ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS;

LOAD DATA INFILE '/home/gideon/firefox/courses.csv'
    INTO TABLE courses
    FIELDS TERMINATED BY ','
    ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS;

LOAD DATA INFILE '/home/gideon/firefox/students.csv'
    INTO TABLE students
    FIELDS TERMINATED BY ','
    ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS;
