CREATE DATABASE `onlysync` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

create table if not exists User (id int(10) primary key unique auto_increment not null, u varchar(50) not null, p varchar(100) not null, sex int(2), email varchar(50));
