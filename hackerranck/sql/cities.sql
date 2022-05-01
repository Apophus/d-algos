select distinct(city)  
    from station 
    where lower(left(city, 1)) not in ('a', 'e','i','o', 'u')
    OR lower(right(city, 1)) not in ('a', 'e','i','o', 'u');

SELECT name 
    FROM students
    where marks > 75

    order by right(name, 3), id

SELECT name
    from employee
    order by name
