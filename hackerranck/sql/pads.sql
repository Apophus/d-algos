SELECT CONCAT(name,'(',LEFT(occupation,1),')')
    from occupations
    order by name;
SELECT GROUPCONCAT('There are a total of', count(occupation),
     case
         WHEN occupation='doctor' then 'doctors'
         WHEN occupation='actor' then 'actors'
         WHEN occupation='professor' then 'professors'
         ELSE 'singers' end)
    from occupations
    group by occupation
    order by count(occupation) asc


SELECT CONCAT(name,'(',LEFT(occupation,1),')')
    from occupations
    order by name;

SELECT CONCAT('There are a total of', count(occupation),
     case
         WHEN occupation='doctor' then 'doctors'
         WHEN occupation='actor' then 'actors'
         WHEN occupation='professor' then 'professors'
         ELSE 'singers')
    from occupations
    group by occupation
    order by count(occupation) asc;