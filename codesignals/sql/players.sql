CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	select GROUP_CONCAT(CONCAT(first_name, ' ',surname,' ','#', player_number) order by player_number asc separator '; ')
	as players
	from soccer_team;
END