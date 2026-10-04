CREATE DATABASE IF NOT EXISTS sample_db;
use sample_db;
create table if not EXISTS departments (
    id int primary key auto_increment,
    name varchar(200) not null,
    location varchar(200)
);

create table if not EXISTS hi (
    id int,
    name varchar(200)
);

insert into departments (name, location) values ('computer', 'chennai');

select * from departments;

