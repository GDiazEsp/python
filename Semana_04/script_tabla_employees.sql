CREATE TABLE employees (
	emp_no int(11) NOT NULL AUTO_INCREMENT,
	first_name varchar(14) NOT NULL,
	last_name varchar(16) NOT NULL,
	gender enum('H','M') NOT NULL,
	birth_date date ,
	hire_date date ,
	PRIMARY KEY (emp_no)
)