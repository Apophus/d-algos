CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT item_name, item_type, count(item_name) as item_count
		from availableitems
		group by item_type
		order by item_type asc, item_count;

	
END