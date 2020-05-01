show databases;
use clifordb;
drop table customer_purchase;
create table customer_purchase(
	id int,
    name varchar(100),
    date varchar(100),
    item_amount double
    );

insert into customer_purchase (id,name,date,item_amount) values (1,'Cliford','2020-01-01', 100);
insert into customer_purchase (id,name,date,item_amount) values (1,'Cliford','2020-01-02', 600);
insert into customer_purchase (id,name,date,item_amount) values (1,'Cliford','2020-01-03', 300);
insert into customer_purchase (id,name,date,item_amount) values (2,'Jerry','2020-01-01', 100);
insert into customer_purchase (id,name,date,item_amount) values (2,'Jerry','2020-01-02', 200);
insert into customer_purchase (id,name,date,item_amount) values (2,'Jerry','2020-01-03', 300);
insert into customer_purchase (id,name,date,item_amount) values (3,'Miya','2020-01-01', 100);
insert into customer_purchase (id,name,date,item_amount) values (3,'Miya','2020-01-02', 200);
insert into customer_purchase (id,name,date,item_amount) values (4,'Alija','2020-01-03', 300);
insert into customer_purchase (id,name,date,item_amount) values (4,'Alija','2020-01-03', 300);

select id,name,item_amount,cp.date
from customer_purchase as cp
join (select max(date) as date from customer_purchase) m
on cp.date = m.date

;

