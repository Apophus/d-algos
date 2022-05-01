CREATE PROCEDURE suspectsInvestigation()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
selct id, name, surname
    from suspect 
    where height <= 170
    and name like 'B%'
    and surname like 'Gre%'
    and length(surname) = 5

END