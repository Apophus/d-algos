CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    select GROUP_CONCAT(distinct(country) order by country asc SEPARATOR ';')
	from diary;
END