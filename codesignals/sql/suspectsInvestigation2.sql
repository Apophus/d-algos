CREATE PROCEDURE suspectsInvestigation2()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    select id, name, surname
    from suspect
    where hieght >= 170
    and name not like 'B%'
    and surname not like 'Gre%'
    and surname not like '%n'
    and length(surname) !=5
    order by id asc
END