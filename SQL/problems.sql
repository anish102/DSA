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

--Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.
delete p1
from
    Person as P1,
    Person as P2
where
    P1.email = P2.email
    and p1.id > p2.id;

--Write a solution to find all the classes that have at least five students.
select
    class
from
    Courses
group by
    class
having
    count(class) > 4;

--Write a solution to report the name and bonus amount of each employee with a bonus less than 1000.
SELECT
    employee.NAME,
    bonus.bonus
FROM
    employee
    LEFT OUTER JOIN bonus ON employee.empid = bonus.empid
WHERE
    bonus.bonus < 1000
    OR bonus IS NULL;

--Write a solution to find all dates' Id with higher temperatures compared to its previous dates (yesterday).
select
    R1.id
from
    Weather as R1,
    Weather as R2
where
    dateDiff(R1.recordDate, R2.recordDate) = 1
    and R1.temperature > R2.temperature;

--Find the names of the customer that are not referred by the customer with id = 2.
--select name from Customer where referee_id != 2 or referee_id is null;
SELECT
    NAME
FROM
    customer
WHERE
    COALESCE(referee_id, '') != 2;

--Write a solution to find the customer_number for the customer who has placed the largest number of orders.
SELECT
    customer_number
FROM
    orders
GROUP BY
    customer_number
ORDER BY
    Count(*) DESC
LIMIT
    1;

--Write a solution to find the name, population, and area of the big countries.
Select
    name,
    population,
    area
from
    World
where
    area >= 3000000
    or population >= 25000000;

--Write a solution to find the names of all the salespersons who did not have any orders related to the company with the name "RED".
SELECT
    name
FROM
    SalesPerson
WHERE
    sales_id NOT IN (
        SELECT
            O.sales_id
        FROM
            Orders AS O
            LEFT JOIN Company AS C ON O.com_id = C.com_id
        WHERE
            C.name = "RED"
    );

--Write a solution to swap all 'f' and 'm' values (i.e., change all 'f' values to 'm' and vice versa).
update
    salary
set
    sex = if(sex = 'm', 'f', 'm');

--Write a solution to report the movies with an odd-numbered ID and a description that is not "boring". Return the result table ordered by rating in descending order.
SELECT
    *
FROM
    cinema
WHERE
    description != "boring"
    AND id % 2 != 0
ORDER BY
    rating DESC;

--Write a solution to show the unique ID of each user, If a user does not have a unique ID replace just show null.
SELECT
    employeeuni.unique_id,
    employees.NAME
FROM
    employees
    LEFT OUTER JOIN employeeuni ON employees.id = employeeuni.id;

--Write a solution to find the first login date for each player.
SELECT
    player_id,
    Min(event_date) AS "first_login"
FROM
    activity
GROUP BY
    player_id;

--Report for every three line segments whether they can form a triangle.
SELECT
    x,
    y,
    z,
    CASE
        WHEN x + y > z
        AND y + z > x
        AND z + x > y THEN 'Yes'
        ELSE 'No'
    end AS triangle
FROM
    Triangle;

--Write a solution to find all the pairs (actor_id, director_id) where the actor has cooperated with the director at least three times.
SELECT
    actor_id,
    director_id
FROM
    ActorDirector
GROUP BY
    actor_id,
    director_id
HAVING
    Count(*) >= 3;

--Write a solution to find the ids of products that are both low fat and recyclable.
Select
    product_id
FROM
    Products
WHERE
    low_fats = "Y"
    AND recyclable = "Y";

--Write a solution to calculate the number of unique subjects each teacher teaches in the university.
SELECT
    teacher_id,
    COUNT(DISTINCT subject_id) AS cnt
FROM
    Teacher
GROUP BY
    teacher_id;

--Write a solution to find the IDs of the invalid tweets.
SELECT tweet_id
FROM   Tweets
WHERE  Length(content) > 15;
