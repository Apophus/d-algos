CREATE PROCEDURE solution()
BEGIN
	SELECT COUNT(*) AS number_of_nulls
    FROM departments
    WHERE LOWER(TRIM(description)) IN ('null', 'nil', '-')
    OR description IS NULL;
END

CREATE PROCEDURE solution()
BEGIN
	SELECT COUNT(CASE
                 WHEN description IS NULL
                 OR TRIM(description) = "NULL"
                 OR TRIM(description) = "nil"
                 OR TRIM(description) = "-"
                 THEN 1 END) AS number_of_nulls
    FROM departments;
END