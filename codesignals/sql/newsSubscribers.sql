CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */

	select distinct(res.subscriber)
	 from (
	 	select subscriber 
		from full_year
		where newspaper like '%Daily%'
		union all
		select subscriber
		from half_year 
		where newspaper like '%Daily%'
		) as res
	 order by subscriber;
END

/*Please add ; after each select statement*/
CREATE PROCEDURE solution()
BEGIN
	SELECT subscriber FROM full_year WHERE newspaper LIKE '%daily%'
    UNION (SELECT subscriber FROM half_year WHERE newspaper LIKE '%daily%')
    ORDER BY subscriber;
END