use clifordb;
drop table sales;
create table sales(
id int,
first_name varchar(20),
last_name varchar(20),
age int,
data_of_age date
);

insert into sales (id,first_name,last_name,age,data_of_age) values(1,'Cliford','Rojas', 17,'2010-1-1');
insert into sales (id,first_name,last_name,age,data_of_age) values(2,'Cliford','Rojas', 18,'2011-1-1');
insert into sales (id,first_name,last_name,age,data_of_age) values(3,'Cliford','Rojas', 19,'2012-1-1');
insert into sales (id,first_name,last_name,age,data_of_age) values(4,'Cliford','Rojas', 20,'2013-1-1');
insert into sales (id,first_name,last_name,age,data_of_age) values(5,'Cliford','Rojas', 21,'2014-1-1');
insert into sales (id,first_name,last_name,age,data_of_age) values(6,'Cliford','Rojas', 22,'2015-1-1');
insert into sales (id,first_name,last_name,age,data_of_age) values(7,'Cliford','Rojas', 23,'2016-1-1');
insert into sales (id,first_name,last_name,age,data_of_age) values(8,'Cliford','Rojas', 24,'2017-1-1');
insert into sales (id,first_name,last_name,age,data_of_age) values(9,'Cliford','Rojas', 25, '2018-1-1');
#Getting the last date and increate it by one year
insert into sales (id,first_name,last_name,age,data_of_age)
WITH cte_0 (id,first_name,last_name,age,date_of_age) as (
select * from sales order by age desc limit 1
), 
cte_1 (id,first_name,last_name,age,data_of_age) as (
select id + 1 as id,first_name,last_name,age +1 as age, DATE_ADD(date_of_age ,INTERVAL 1 YEAR) as data_of_age from cte_0
) 
select id,first_name,last_name,age,data_of_age from cte_1;

select * from sales;



