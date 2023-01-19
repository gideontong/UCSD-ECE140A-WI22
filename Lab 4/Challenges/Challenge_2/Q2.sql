CREATE TABLE teachers (
    id INT NOT NULL auto_increment,
    name VARCHAR(50) NOT NULL,
    primary key (id)
);

CREATE TABLE grades (
    id INT NOT NULL auto_increment,
    student_id integer NOT NULL,
    course_id integer NOT NULL,
    grade VARCHAR(5) NULL,
    primary key (id)
);

CREATE TABLE courses (
    id INT NOT NULL auto_increment,
    name VARCHAR(50) NOT NULL,
    teacher_id integer NULL,
    primary key (id)
);

CREATE TABLE students (
    id INT NOT NULL auto_increment,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL,
    primary key (id)
);
