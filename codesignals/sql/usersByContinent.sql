CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    select continent, sum(users) as users
        from countries
    group by continent 
    order by users desc
END