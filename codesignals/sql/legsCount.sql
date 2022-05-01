DROP PROCEDURE IF EXISTS solution;
CREATE PROCEDURE solution()
    SELECT (SUM(IF(type = 'human', 2, 4))) as summary_legs
    FROM creatures
    ORDER BY id;

DROP PROCEDURE IF EXISTS solution;
CREATE PROCEDURE solution()
    SELECT SUM(CASE WHEN type='human' THEN 2 WHEN type='cat' THEN 4 when type='dog' then 4 ELSE 0 END)as summary_legs
    FROM creatures
    ORDER BY id;
