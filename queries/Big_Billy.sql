create database Billy_store;
use Billy_store;
-- create table 
create table cust_details(
     cust_id int not null primary key, 
     cust_name varchar(30) not null,
     Address char (40) not null unique ,
     email  varchar (25) null,
     phone_number bigint null,
     gender   varchar (10) null,
     date_birth date null,
     account_status varchar (15) not null
);
create table orders_cust(
order_id int primary key,
cust_id int,
order_date datetime,
order_status varchar(10) default 'Delivered',
sub_total int,
constraint cus_idt foreign key (cust_id) references cust_details(cust_id)
);
create table Payment_info(
payment_method varchar (40) default 'Credit Card',
Payment_status varchar (40) default 'Paid',
Tracking_id varchar(10) primary key,
order_id int,
constraint O_id foreign key (order_id) references orders_cust(order_id) 
);
create table shipping(
shipping_address char (40) not null,
shipping_method varchar (30) not null default 'Express',
Ship_Tracker varchar(10),
constraint Tracker foreign key (Ship_Tracker) references payment_info(Tracking_id)
);

INSERT INTO cust_details (cust_id, cust_name, address, email, phone_number, gender, date_birth, account_status) VALUES
(1, 'John Doe', '100 Main St', 'johndoe@hotmail.com', 8298339716, 'Female', '1978-05-23', 'Active'),
(2, 'Jane Smith', '101 Main St', 'janesmith@gmail.com', 7952292459, 'Female', '1978-12-04', 'Inactive'),
(3, 'Alice Johnson', '102 Main St', 'Alicejohnson@hotmail.com', 9910432287, 'Female', '1973-06-16', 'Inactive'),
(4, 'Robert Brown', '103 Main St', 'Robertbrown@gmail.com', 9435074435, 'Male', '1974-01-15', 'Active'),
(5, 'Emily Davis', '104 Main St', 'EmilyDavis@hotmail.com', 8717452060, 'Female', '1994-03-13', 'Inactive'),
(6, 'Michael Wilson', '105 Main St', 'michaelwilson@gmail.com', 9814444077, 'Female', '1992-02-17', 'Inactive'),
(7, 'Sarah Clark', '106 Main St', 'sarahclark@hotmail.com', 9619482150, 'Female', '1976-05-16', 'Inactive'),
(8, 'David Lee', '107 Main St', 'davidlee@yahoo.com', 9517361334, 'Female', '2001-12-29', 'Active'),
(9, 'Laura Hall', '108 Main St', 'laurahall@gmail.com', 9099488742, 'Male', '1971-09-18', 'Active'),
(10, 'Daniel Young', '109 Main St', 'danielyoung@hotmail.com', 7837412086, 'Male', '1990-10-25', 'Active'),
(11, 'Jessica King', '110 Main St', 'jessicaking@gmail.com', 9882453689, 'Male', '1994-02-28', 'Inactive'),
(12, 'William Wright', '111 Main St', 'williamwright@gmail.com', 7170057085, 'Female', '1983-11-14', 'Active'),
(13, 'Olivia Scott', '112 Main St', 'Oliviascott@yahoo.com', 9901346620, 'Female', '1986-11-16', 'Inactive'),
(14, 'Thomas Green', '113 Main St', 'Thomasgreen@gmail.com', 9205823132, 'Male', '1987-01-08', 'Active'),
(15, 'Emma Baker', '114 Main St', 'emmabaker@yahoo.com', 7316559709, 'Female', '1983-04-17', 'Inactive'),
(16, 'James Adams', '115 Main St', 'jamesadams@hotmail.com', 9963182207, 'Female', '2004-02-10', 'Inactive'),
(17, 'Ava Mitchell', '116 Main St', 'Avamitchell@gmail.com', 7113243993, 'Female', '1984-08-19', 'Active'),
(18, 'Henry Carter', '117 Main St', 'HenryCarter@yahoo.com', 7312428090, 'Female', '1995-10-11', 'Active'),
(19, 'Sophia Turner', '118 Main St', 'SophiaTurner@gmail.com', 9827566036, 'Male', '1990-01-22', 'Inactive'),
(20, 'Liam Phillips', '119 Main St', 'Liamphillips@hotmail.com', 9375073507, 'Female', '2004-08-18', 'Active'),
(21, 'Isabella Evans', '120 Main St', 'IsabellaEvans@yahoo.com', 7322483266, 'Male', '1987-04-11', 'Inactive'),
(22, 'Noah Collins', '121 Main St', 'Noahcollins@gmail.com', 8914573067, 'Male', '1986-06-13', 'Active'),
(23, 'Mia Morris', '122 Main St', 'MiaMorris@yahoo.com', 8930352823, 'Female', '1996-09-17', 'Inactive'),
(24, 'Lucas Stewart', '123 Main St', 'LucasStewart@hotmail.com', 7756821244, 'Male', '1987-09-04', 'Active'),
(25, 'Amelia Rogers', '124 Main St', 'AmeliaRogers@gmail.com', 7294085647, 'Male', '1993-08-15', 'Inactive'),
(26, 'Mason Reed', '125 Main St', 'MasonReed@gmail.com', 7949326250, 'Female', '1993-09-09', 'Active'),
(27, 'Harper Cook', '126 Main St', 'Harpercook@hotmail.com', 7388161854, 'Male', '1985-05-23', 'Inactive'),
(28, 'Elijah Morgan', '127 Main St', 'ElijahMorgan@hotmail.com', 7784422915, 'Female', '1997-07-30', 'Active'),
(29, 'Evelyn Bell', '128 Main St', 'EvelynBell@yahoo.com', 7585083443, 'Female', '1992-02-24', 'Inactive'),
(30, 'Logan Murphy', '129 Main St', 'LoganMurphy@gmail.com', 9406404421, 'Male', '1976-09-26', 'Inactive'),
(31, 'Abigail Bailey', '130 Main St', 'AbigailBailey@yahoo.com', 8378763683, 'Female', '1981-02-25', 'Inactive'),
(32, 'Jacob Rivera', '131 Main St', 'JacobRivera@gmail.com', 9121641831, 'Male', '1997-08-20', 'Inactive'),
(33, 'Emily Cooper', '132 Main St', 'EmilyCooper@gmail.com', 7374198776, 'Female', '2002-09-26', 'Active'),
(34, 'Ethan Richardson', '133 Main St', 'EthanRichardson@yahoo.com', 7938041081, 'Male', '1991-10-13', 'Active'),
(35, 'Elizabeth Cox', '134 Main St', 'Elizabethcox@hotmail.com', 8075245417, 'Male', '1985-05-29', 'Active'),
(36, 'Benjamin Howard', '135 Main St', 'BenjaminHoward@gmail.com', 7644186577, 'Male', '2002-10-24', 'Active'),
(37, 'Chloe Ward', '136 Main St', 'ChloeWard@gmail.com', 7580829165, 'Male', '1972-04-18', 'Inactive'),
(38, 'Sebastian Torres', '137 Main St', 'SebastianTorres@yahoo.com', 9360090043, 'Male', '1988-04-06', 'Active'),
(39, 'Grace Peterson', '138 Main St', 'Gracepeterson@gmail.com', 7531318455, 'Male', '2003-12-03', 'Active'),
(40, 'Alexander Gray', '139 Main St', 'Alexandergray@yahoo.com', 9361697699, 'Female', '1981-08-07', 'Inactive');


INSERT INTO orders_cust (order_id, cust_id, order_date, order_status, sub_total) VALUES
(1, 1, '2023-08-21 13:54:02', 'Pending', 337),
(2, 2, '2023-12-23 07:43:14', 'Pending', 729),
(3, 3, '2024-08-06 19:48:37', default, 521),
(4, 4, '2023-05-24 00:30:35', 'Pending', 640),
(5, 5, '2023-11-16 10:23:08', 'Pending', 288),
(6, 6, '2024-10-15 02:32:31', 'Shipped', 663),
(7, 7, '2023-11-30 12:37:11', 'Pending', 149),
(8, 8, '2024-11-12 18:10:17', default, 365),
(9, 9, '2024-01-25 11:20:41', default, 515),
(10, 10, '2024-01-17 17:26:34', 'Shipped', 326),
(11, 11, '2023-10-06 22:21:08', 'Shipped', 243),
(12, 12, '2024-02-17 08:18:43', default, 100),
(13, 13, '2024-11-28 09:59:01', 'Pending', 954),
(14, 14, '2023-02-13 18:00:27', 'Pending', 578),
(15, 15, '2024-11-13 02:15:03', 'Pending', 682),
(16, 16, '2023-05-03 10:03:39', 'Shipped', 489),
(17, 17, '2023-09-10 15:13:55', default, 798),
(18, 18, '2023-03-27 19:45:31', 'Pending', 425),
(19, 19, '2024-04-23 20:21:42', 'Pending', 541),
(20, 20, '2024-12-02 03:32:26', 'Shipped', 127),
(21, 21, '2023-08-13 11:08:28', 'Pending', 455),
(22, 22, '2023-07-15 15:38:24', 'Shipped', 821),
(23, 23, '2023-05-10 23:58:42', 'Pending', 459),
(24, 24, '2024-11-05 14:52:10', default, 1000),
(25, 25, '2024-01-02 12:41:13', 'Shipped', 138),
(26, 26, '2024-08-14 13:29:33', default, 749),
(27, 27, '2024-06-22 06:42:46', 'Shipped', 201),
(28, 28, '2024-01-03 16:00:16', default, 898),
(29, 29, '2023-10-09 10:48:25', 'Shipped', 253),
(30, 30, '2023-09-14 04:50:40', 'Shipped', 389),
(31, 31, '2023-01-08 15:04:51', default, 314),
(32, 32, '2024-07-11 07:22:56', 'Pending', 619),
(33, 33, '2024-01-27 14:06:02', 'Shipped', 352),
(34, 34, '2023-10-18 08:28:14', default, 854),
(35, 35, '2024-10-03 02:44:01', default, 547),
(36, 36, '2023-12-27 06:46:19', default, 176),
(37, 37, '2024-03-06 01:17:50', 'Shipped', 632),
(38, 38, '2023-01-18 11:44:45', 'Pending', 180),
(39, 39, '2023-03-31 17:11:59', 'Shipped', 174),
(40, 40, '2023-06-17 21:27:26', default, 728);



INSERT INTO payment_info (payment_method, payment_status, tracking_id, order_id) VALUES
('PayPal', default, 'TID001', 1),
(default, 'Pending', 'TID002', 2),
('Bank Transfer', 'Paid', 'TID003', 3),
('PayPal', default, 'TID004', 4),
(default, default, 'TID005', 5),
('Bank Transfer', 'Failed', 'TID006', 6),
('PayPal', 'Pending', 'TID007', 7),
(default, default, 'TID008', 8),
('Bank Transfer', default, 'TID009', 9),
('PayPal', 'Paid', 'TID010', 10),
(default, 'Paid', 'TID011', 11),
('Bank Transfer', 'Pending', 'TID012', 12),
('PayPal',default, 'TID013', 13),
(default, default, 'TID014', 14),
('Bank Transfer', 'Failed', 'TID015', 15),
('PayPal', default, 'TID016', 16),
(default, default, 'TID017', 17),
('Bank Transfer', 'Pending', 'TID018', 18),
('PayPal', default, 'TID019', 19),
(default,default, 'TID020', 20),
('Bank Transfer', 'Failed', 'TID021', 21),
('PayPal', 'Failed', 'TID022', 22),
(default, default, 'TID023', 23),
('Bank Transfer', 'Pending', 'TID024', 24),
('PayPal', 'Failed', 'TID025', 25),
(default, default, 'TID026', 26),
('Bank Transfer', default, 'TID027', 27),
('PayPal', 'Pending', 'TID028', 28),
(default, default, 'TID029', 29),
('Bank Transfer', 'Failed', 'TID030', 30),
('PayPal', default, 'TID031', 31),
(default, 'Failed', 'TID032', 32),
('Bank Transfer', 'Pending', 'TID033', 33),
('PayPal', default, 'TID034', 34),
(default, 'Pending', 'TID035', 35),
('Bank Transfer', default, 'TID036', 36),
('PayPal', 'Failed', 'TID037', 37),
(default, default, 'TID038', 38),
('Bank Transfer', 'Pending', 'TID039', 39),
('PayPal', default, 'TID040', 40);

INSERT INTO shipping (shipping_address, shipping_method, ship_tracker) VALUES
('100 Main St', 'Overnight', 'TID020'),
('101 Main St',  default, 'TID005'),
('102 Main St', 'Standard', 'TID014'),
('103 Main St', 'Overnight', 'TID001'),
('104 Main St', 'Standard', 'TID019'),
('105 Main St',  default, 'TID037'),
('106 Main St', 'Overnight', 'TID004'),
('107 Main St',  default, 'TID025'),
('108 Main St', 'Standard', 'TID018'),
('109 Main St', 'Overnight', 'TID033'),
('110 Main St', 'Standard', 'TID003'),
('111 Main St',  default, 'TID032'),
('112 Main St', 'Overnight', 'TID007'),
('113 Main St', 'Standard', 'TID036'),
('114 Main St', 'Overnight', 'TID010'),
('115 Main St',  default, 'TID040'),
('116 Main St', 'Standard', 'TID011'),
('117 Main St', 'Overnight', 'TID021'),
('118 Main St', 'Standard', 'TID015'),
('119 Main St', 'Overnight', 'TID026'),
('120 Main St',  default, 'TID002'),
('121 Main St', 'Standard', 'TID034'),
('122 Main St', 'Overnight', 'TID006'),
('123 Main St', 'Standard', 'TID022'),
('124 Main St', 'Overnight', 'TID017'),
('125 Main St',  default, 'TID030'),
('126 Main St', 'Standard', 'TID023'),
('127 Main St', 'Overnight', 'TID009'),
('128 Main St', 'Standard', 'TID012'),
('129 Main St', 'Overnight', 'TID027'),
('130 Main St',  default, 'TID035'),
('131 Main St', 'Standard', 'TID028'),
('132 Main St', 'Overnight', 'TID016'),
('133 Main St',  default, 'TID038'),
('134 Main St', 'Overnight', 'TID008'),
('135 Main St', 'Standard', 'TID039'),
('136 Main St',  default, 'TID031'),
('137 Main St', 'Standard', 'TID029'),
('138 Main St', 'Overnight', 'TID024'),
('139 Main St',  default, 'TID013');

/*Alter , Drop , Delete, Sql constraints, insert , select , update  view */

-- Alter is used to modify a table , -option Drop , Add , modify , Rename 
Alter table cust_details add country varchar(15);
-- retrieve  table details
Select * from cust_order;

-- update table 
update cust_details set country = case   
when cust_id in (1, 3) then 'Lagos'
when cust_id in  (2, 4, 8, 9, 10) then 'Abuja'
when cust_id in (12, 13, 14, 15, 16) then 'Warri'
when cust_id in (17, 18 , 19, 20, 21) then 'jos'end  
where cust_id in (1,2, 3, 4, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18 , 19, 20, 21);
 -- to add a constraint to column in sql server
 -- for  specifies the column that is constraint
Alter table cust_order add constraint default_order default 'Delivered' for order_status;

-- to get a constraint name 
 SELECT 
    TABLE_NAME,
    CONSTRAINT_NAME,
    CONSTRAINT_TYPE
FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS where  CONSTRAINT_TYPE = 'primary key' and TABLE_NAME = 'cust_order';



-- we have drop the default constraint before we can modify 
Alter table cust_order drop constraint default_order;

-- modify in sql server is Alter column
Alter table cust_order Alter column  order_status char(15)
--Rename sp_rename  table name 
exec sp_rename 'orders_cust' , 'cust_order';
exec sp_rename 'cust_order.order_date' , 'date_order';

EXEC sp_rename 'PK__cust_det__A1B71F9086D3E7BA', 'PK_cust_detials', 'OBJECT';

-- clone in sql server
select * into Big_payment from Payment_info ;

-- Describe command 
EXEC sp_help 'Big_payment ';


select column_name, DATA_TYPE, IS_NULLABLE, column_default from 
information_schema.columns where table_name = 'payment_info';

-- view  is a virtual table that is stored in a database with
--- a particular report i want to save on the database 
create view billy_view as select * from  Cust_details where account_status ='Active' with check option;

-- drop a view 
drop view billy_view;

Select * from billy_viewq;

-- update table  
update cust_details set account_status = 'Active' where cust_id in (27,31, 32);

-- in mysql to rename a Table 
/*Rename table billy_view to view_billy; */


-- sql server 
exec sp_rename 'billy_view', 'billy_viewq';

-- insert data into another table 
create table Big_pay(
payment_method varchar (40) default 'Credit Card',
Payment_status varchar (40) default 'Paid',
Tracking_id varchar(10) primary key,
order_id int,
constraint O_di foreign key (order_id) references cust_order(order_id) 
);

insert into Big_pay() select * from Payment_info;
select * from Big_pay

-- insert table : if the we have the structure of a table are the same you could just insert 
-- instead of selecting specfic columns
-- first create a table
create table Big_pad(
     cust_id int not null primary key, 
     cust_name varchar(30) not null,
     Address char (40) not null unique ,
     email  varchar (25) null,
     phone_number bigint null,
     gender   varchar (10) null,
     date_birth date null,
     account_status varchar (15) not null
); 

-- select query
-- it use to fetch and retrieve  data from a database  
-- this is how will clone in sql 
select * into cust_ord  from cust_order;
-- where clause 
select * from cust_ord; 
select *  from cust_order where order_id in (1, 2, 4, 5);

select * from cust_details;
update cust_details set  Address = case 
when cust_id in (5) then '200 Main St'
when cust_id  in( 4) then '205 Main St'
when cust_id  in ( 7) then '206 Main St'
end where  cust_id in (5, 4, 7)
;
select * from cust_details  where gender ='Female';
-- top clause ,  Distinct keyword , Group by clause , Having clause ,Order by clause 
select top  4  * from cust_details  where gender = 'Female';

-- top clause with percent 
select top  40 percent * from cust_details  where gender = 'Female';

-- top clause with ties clause 
select top 40 Percent with ties  * from cust_details  where Country = 'Abuja' order by account_status Asc

-- Distintct keyword 
select distinct cust_name ,address , email, gender from cust_details where gender = 'Male' ;

-- Group by clause  with a halving clause 
select cust_name , count(phone_number) as 'Phone Number', email , account_status from 
cust_details group by cust_name, account_status, email having account_status = 'Active';

-- And or Or conjuctive Operation 
select cust_name , phone_number , email , account_status from 
cust_details where email = 'AbigailBailey@yahoo.com' and  account_status = 'Active';

delete from cust_details where cust_name like 'Abigail%' or  account_status ='Inactive';

select Table_Name, Constraint_Name, Constraint_Type from 
INFORMATION_SCHEMA.Table_CONSTRAINTS where Table_Name 
in('Cust_details', 'Shipping', 'Payment_info','cust_order');

 -- alter table cust_order drop constraint cus_idt;

 -- Boolean datatype , like , IN ,Not IN , iN with subquery , Any , ALL , Exists
 -- Boolean datatype in sql server only store true or false as 1, 0 and also can have a null value 
 alter table cust_details add Value_T bit;
-- update the column Value_T
update cust_details set Value_T = case  
when cust_id between 1 and 10 then 0
when cust_id between 11 and 20  then 1 
else Null
end where  cust_id between 1 and 40
;
select * from cust_details;
 
select Column_Name ,Data_Type from INFORMATION_SCHEMA.columns where Table_Name = 'cust_details';

SELECT 
    TABLE_NAME,
    COLUMN_NAME,
    DATA_TYPE,
    CHARACTER_MAXIMUM_LENGTH,
    IS_NULLABLE,
    COLUMN_DEFAULT
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'cust_details';

-- like clause  is used  to check if pattern exist  in column and retrieve result
-- NOT like 
select * from cust_details where Value_T not like '%0%';
--  in , Any , All Operators , exists , case , NoT operator , Not equal, is Null , 
-- Between operator , union and union all operator, interset, Except, Alias , join 

-- using in with a subquery 

select P.Payment_status, P.order_id, P.Tracking_id,S.shipping_address,S.shipping_method 
from Payment_info as P join shipping as S on P.Tracking_id = S.Ship_Tracker
where cast(S.shipping_method as varchar(40)) in 
(select  cast(shipping_method  as varchar(40)) from shipping where cast(shipping_method  as varchar(40)) = 'Express');

-- in clause with a select  
select * from cust_details  where cust_name   in ('john Doe', 'Jane smith');

-- in clause with an update
update cust_details set Address = case 
when cust_id in (1)  then '500 Main st' 
when cust_id in (2)  then '600 Main st' 
when cust_id in (3)  then '700 Main st' 
end 
where cust_id in (1, 2, 3)

-- in clause with not 
select * from cust_details  where cust_name  not in ('john Doe', 'Jane smith');

-- in clause with a subquery 
select B.payment_method, B.Payment_status, B.Tracking_id, B.Order_id from Big_payment as B 
join Payment_info as P  on P.Tracking_id = B.Tracking_id where B.Payment_status in 
(select P.Payment_status from  Payment_info as P  where P.Payment_status = 'Paid');

-- Any  Operator 
 select shipping_address , shipping_method , ship_tracker from shipping where shipping_address > Any
 (select shipping_address from shipping  where shipping_method = 'Overnight');

 -- All  Operator 
 select shipping_address , shipping_method , ship_tracker from shipping where shipping_address > All
 (select shipping_address from shipping  where shipping_method = 'Overnight');

 -- exists , case , NoT operator , Not equal <> / !=, is Null , Between operator 
--  union and union all operator, intercept, Except, Alias , join 

-- exists 
select C.cust_id, C.cust_name,C.country, C.Address, CO.order_id, CO.order_status, CO.sub_total  
from cust_details as C join cust_order as CO on C.cust_id = CO.cust_id where exists
(select cust_name from cust_details where country ='London');

-- exists with update 
update cust_details set Country = 
case when cust_id between 1 and 10 then 'London' 
when cust_id between 11 and 20  then 'Lagos' 
when cust_id between 21 and 30 then 'USA' 
when cust_id between 31 and 40 then 'Canada' 
end
where exists
(select country from cust_details where country = 'London');

-- delete with exists
delete from cust_details where  exists
(select country from cust_details where country = 'London');

-- exists with  not operator
select C.cust_id, C.cust_name,C.country, C.Address, CO.order_id, CO.order_status, CO.sub_total  
from cust_details as C join cust_order as CO on C.cust_id = CO.cust_id where not exists
(select cust_name from cust_details where country ='London')

-- exists with aggregate 
select C.cust_id, C.cust_name,C.country,avg(C.phone_number) as 'Phone Number', C.Address, CO.order_id, CO.order_status, CO.sub_total  
from cust_details as C join cust_order as CO on C.cust_id = CO.cust_id where exists
(select cust_name from cust_details where country ='London') group by C.cust_id, C.cust_name,C.country,C.Address,
CO.order_id, CO.order_status, CO.sub_total ; 

-- case statement 
-- case with select statement
select cust_id , 
case 
when cust_id between 1 and 10 then 'Raheem Family'
when cust_id between 11 and 20 then 'Akande Family'
when cust_id between 21  and 30 then 'Solomon Family'
else 'Adeleke Family' end as Family_Group , cust_name, gender , date_birth from cust_details ;

-- case with order by 
select cust_id ,cust_name, gender , date_birth from cust_details where gender = 'Male' 
order by case 
when year(date_birth) between 1990 and 1999 then '1990'
when year(date_birth) between 2000 and 2020 then '2000'
end Asc ;

-- case with group by 
select cust_id, cust_name, gender ,date_birth, 
case 
when year(date_birth) between 1990 and 1999 then '1990'
when year(date_birth) between 2000 and 2020 then '2000'
end as 'Birth Date', avg(phone_number) as 'Phone Number' from cust_details
where cust_id between 1 and 20 and 
(year(date_birth) between 1990 and 1999 
or year(date_birth) between 2000 and 2020 )
group by case 
when year(date_birth) between 1990 and 1999 then '1990'
when year(date_birth) between 2000 and 2020 then '2000'
end,cust_id, cust_name, gender , date_birth; 

select Table_Name, CONSTRAINT_TYPE from INFORMATION_SCHEMA.TABLE_Constraints
where CONSTRAINT_CATALOG = 'Billy_Store';

select Table_Name, Table_Type from INFORMATION_SCHEMA.TABLES
where Table_CATALOG = 'Billy_Store';


update o set o.Status ='Active' from order o join customers C on  O.customerid = C.customerid 
where c.isActive = 1; 