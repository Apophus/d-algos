CREATE PROCEDURE solution()
BEGIN
	SELECT * FROM expressions
    WHERE CASE operation
        WHEN '+' THEN a + b
        WHEN '-' THEN a - b
        WHEN '*' THEN a * b
        WHEN '/' THEN a / b
      END = c
    ORDER BY id;
END

CREATE PROCEDURE solution()
BEGIN
    SELECT * FROM expressions
        WHERE (operation = '+' AND a + b = c) OR 
              (operation = '-' AND a - b = c) OR 
              (operation = '*' AND a * b = c) OR
              (operation = '/' AND b != 0 AND C * b = a);
END

CREATE PROCEDURE solution()
SELECT   *
FROM     expressions
WHERE    c = IF( operation = '+', a+b,
             IF( operation = '-', a-b,
             IF( operation = '*', a*b,
             IF( operation = '/', a/b, NULL ))))
ORDER BY id
