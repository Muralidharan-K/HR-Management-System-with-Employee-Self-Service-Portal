# HR-Management-System-with-Employee-Self-Service-Portal
An integrated HR platform that streamlines HR processes from employee enrollment to payroll, attendance, and leave management. Features an employee self-service portal that allows employees to clock-in/clock-out, apply for leave, and view their attendance records.

# Attendance Table
Field         | Type        | Null | Key | Default | Extra |
+---------------+-------------+------+-----+---------+-------+
| Employee_ID   | varchar(12) | YES  | MUL | NULL    |       |
| Employee_Name | varchar(30) | YES  |     | NULL    |       |
| clk_date      | varchar(10) | YES  |     | NULL    |       |
| mo_yr         | varchar(10) | YES  |     | NULL    |       |
| clock_in      | varchar(10) | YES  |     | NULL    |       |
| clock_out     | varchar(10) | YES  |     | NULL    |       |
| status        | varchar(15) | YES  |     | NULL    |       |
+---------------+-------------+------+-----+---------+-------+

# Employee_info Table
 Field               | Type         | Null | Key | Default | Extra |
+---------------------+--------------+------+-----+---------+-------+
| Employee_ID         | varchar(12)  | NO   | PRI | NULL    |       |
| Employee_Name       | varchar(30)  | YES  |     | NULL    |       |
| Email_ID            | varchar(30)  | YES  |     | NULL    |       |
| Mob_number          | varchar(10)  | YES  |     | NULL    |       |
| Date_of_birth       | varchar(10)  | YES  |     | NULL    |       |
| Marriage_status     | varchar(10)  | YES  |     | NULL    |       |
| Father_name         | varchar(30)  | YES  |     | NULL    |       |
| Mother_name         | varchar(30)  | YES  |     | NULL    |       |
| Spouse_name         | varchar(30)  | YES  |     | NULL    |       |
| Employee_type       | varchar(15)  | YES  |     | NULL    |       |
| Designation         | varchar(15)  | YES  |     | NULL    |       |
| Department_name     | varchar(30)  | YES  |     | NULL    |       |
| Date_of_joining     | varchar(10)  | YES  |     | NULL    |       |
| PF_Number           | varchar(20)  | YES  |     | NULL    |       |
| UAN_number          | varchar(12)  | YES  |     | NULL    |       |
| PAN_number          | varchar(10)  | YES  |     | NULL    |       |
| Aadhar_number       | varchar(12)  | YES  |     | NULL    |       |
| Basic_pay           | varchar(5)   | YES  |     | NULL    |       |
| HRA                 | varchar(5)   | YES  |     | NULL    |       |
| Special_allowance   | varchar(5)   | YES  |     | NULL    |       |
| Gross               | varchar(6)   | YES  |     | NULL    |       |
| PF_Emp_cont         | varchar(4)   | YES  |     | NULL    |       |
| PF_Org_cont         | varchar(4)   | YES  |     | NULL    |       |
| Cost_to_the_company | varchar(6)   | YES  |     | NULL    |       |
| AC_number           | varchar(20)  | YES  |     | NULL    |       |
| Bank_name           | varchar(20)  | YES  |     | NULL    |       |
| Branch              | varchar(20)  | YES  |     | NULL    |       |
| IFSC                | varchar(20)  | YES  |     | NULL    |       |
| Address             | varchar(200) | YES  |     | NULL    |       |
+---------------------+--------------+------+-----+---------+-------+
