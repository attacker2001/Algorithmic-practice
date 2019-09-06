/*
@file: 176. Second Highest Salary.py 
@time: 2019/09/06

https://leetcode.com/problems/second-highest-salary/

SQL Schema
Write a SQL query to get the second highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+

For example, given the above Employee table, the query should return 200 as the second highest salary.

If there is no second highest salary, then the query should return null.

+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
"""
*/


SELECT MAX(salary)
FROM Employee
WHERE Salary NOT IN (
    SELECT Max(Salary) FROM Employee
);



/*

Other solutions:

// solution 1
SELECT
  MAX(Salary) as SecondHighestSalary
From
  Employee
WHERE
  Salary < ( SELECT Max(Salary) FROM Employee);

// solution 2
SELECT IFNULL(
  (SELECT DISTINCT Salary
  FROM Employee ORDER BY Salary DESC
  LIMIT 1 OFFSET 1), NULL)
AS SecondHighestSalary


Background knowledge:

MySQL的if既可以作为表达式用，也可在存储过程中作为流程控制语句使用。

如下是做为表达式使用：

IF表达式
IF(expr1,expr2,expr3)

如果 expr1 是TRUE (expr1 <> 0 and expr1 <> NULL)，则 IF()的返回值为expr2;
否则返回值则为 expr3。

IF() 的返回值为数字值或字符串值，具体情况视其所在语境而定。


*/