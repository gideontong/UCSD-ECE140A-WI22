CREATE TABLE TestUesrs (
    id         integer     AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(30) NOT NULL,
    last_name  VARCHAR(30) NOT NULL,
    email      VARCHAR(30) NOT NULL,
    age        int,
    created_at TIMESTAMP
);