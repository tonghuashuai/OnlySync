CREATE DATABASE `onlysync` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

create table if not exists `User` (id int(10) primary key unique auto_increment not null, u varchar(50) not null, p varchar(100) not null, sex int(2), email varchar(50));

create table if not exists `SNS`(id int(10) primary key unique auto_increment not null, name varchar(50) not null, icon varchar(100) not null, code varchar(10) not null, index `code` (`code`));
insert into `SNS` (name, icon, code) values ('新浪微博', '/static/img/weibo.png', 'sweibo');
insert into `SNS` (name, icon, code) values ('微信', '/static/img/weixin.png', 'weixin');

create table if not exists `Access` (id int(10) primary key unique auto_increment not null, u_id int(10) not null, sns_code varchar(10) not null, access_token varchar(100), expires_time datetime, expires_in int(10), open_id varchar(100));


insert into `SNS` (name, icon, code) values ('新浪微博', 'http://www.sinaimg.cn/blog/developer/wiki/LOGO_48x48.png', 'sweibo');
insert into SNS (name, icon, code) value("腾讯微博", "http://mat1.gtimg.com/app/opent/images/wiki/share/32.png", "tweibo");
insert into SNS (name, icon, code) values ('人人网', 'http://wiki.dev.renren.com/mediawiki/images/e/ef/%E7%BA%AF%E8%89%B2%E8%83%8C%E6%99%AF%E8%89%B232px.jpg', 'renren');
insert into `SNS` (name, icon, code) values ('微信', '/static/img/weixin.png', 'weixin');
