CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */

	SELECT count(name) as number,
		avg(population) as average,
		sum(population) as total 
		from countries;

END