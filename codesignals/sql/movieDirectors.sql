CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */

    select director 
        from moviesinfo
    where year > 2000
    group by director
    having sum(oscars) > 2
    order by director asc;
END