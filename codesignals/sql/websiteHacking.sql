CREATE PROCEDURE solution()
    SELECT id,login,name
    FROM users
    WHERE type='user'
    OR type in (SELECT distinct(type) from users)
    ORDER BY id
