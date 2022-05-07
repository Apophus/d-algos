SELECT CASE
	WHEN (a=b) and (a=c)
		THEN 'Equilateral'
	WHEN (a=b) or (c=a) or (b=c)
		THEN 'Isosceles'
	WHEN (a!=b) and (b!=c) and c(!=a)
		THEN 'Scalene'
	WHEN (a+b) < c 
		THEN 'Not A Triangle'
	end 
	from triangles

SELECT CASE WHEN A + B <= C OR A + C <= B OR B + C <= A THEN 'Not A Triangle'
            WHEN A = B AND B = C THEN 'Equilateral'
            WHEN A = B OR A = C OR B = C THEN 'Isosceles'
            ELSE 'Scalene'
        END
FROM TRIANGLES
