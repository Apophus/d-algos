CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    select t.country as country, t.competitor as competitors
        FROM(
            SELECT country, count(country) as competitor
            from foreignCompetitors
            group by country order by country asc) as t
    union
    select "Total:" as country, count(competitor) as competitors
    from foreignCompetitors;
    
END

/*Please add ; after each select statement*/
CREATE PROCEDURE solution()
BEGIN
    SELECT *
    FROM (
        SELECT country,COUNT(country) AS competitors
        FROM foreignCompetitors
        GROUP BY country
        ORDER BY country
    ) first
    UNION
    SELECT 'Total:',COUNT(country)
    FROM foreignCompetitors last;
END

/*Please add ; after each select statement*/
CREATE PROCEDURE solution()
BEGIN
    select ifnull(country, "Total:") as country, count(competitor) as competitors
    from foreignCompetitors
    group by country
    with rollup;
END