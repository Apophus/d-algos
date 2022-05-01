CREATE PROCEDURE mischievousNephews()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    select case when dayname(week_day) = 'Monday' then 0
        when dayname(mischief_date) = 'Tuesday' then 1
        when dayname(mischief_date) = 'Wednesday' then 2
        when dayname(mischief_date) = 'Thursday' then 3
        when dayname(mischief_date) = 'Friday' then 4
        when dayname(mischief_date) = 'Saturday' then 5
        when dayname(mischief_date) = 'Sunday' then 6
        
        end as weekday,
        mischief_date,
        author
        from mischief

        order by weekday asc, field(author, 'Huey', 'Dewey','Louie'), mischief_date, title asc;
END