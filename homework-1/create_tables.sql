-- SQL-команды для создания таблиц

CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
	first_name varchar(20) NOT NULL,
	last_name varchar(20) NOT NULL,
	title varchar(50) NOT NULL,
	birth_date date,
	notes varchar(1000)
);

CREATE TABLE customers
(
	customer_id char(5) PRIMARY KEY,
	company_name varchar(80) NOT NULL,
	contact_name varchar(80) NOT NULL
);

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id char(5) REFERENCES customers(customer_id) NOT NULL,
	employee_id int REFERENCES employees(employee_id) NOT NULL,
	order_date date NOT NULL,
	ship_city varchar(30)
);

