--Write a solution to report the first name, last name, city, and state of each person in the Person table. If the address of a personId is not present in the Address table, report null instead.
SELECT
    Person.firstName,
    Person.lastName,
    Address.city,
    Address.state
FROM
    Person
    LEFT OUTER JOIN Address ON Person.personId = Address.personId;

--Write a solution to find the employees who earn more than their managers.
select
    e1.name 'Employee'
from
    employee e1
    inner join employee e2 on e1.managerid = e2.id
where
    e1.salary > e2.salary;

--Write a solution to report all the duplicate emails.
select
    email as Email
from
    Person
group by
    email
having
    count(email) > 1;

--Write a solution to find all customers who never order anything.
select
    name as Customers
from
    Customers C1
    left outer join Orders O1 on C1.id = O1.customerId
where
    O1.id is Null;