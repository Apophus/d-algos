/*Please add ; after each select statement*/
CREATE PROCEDURE securityBreach()
BEGIN
	SELECT * FROM users
            WHERE attribute LIKE 
                   CONCAT('%_!%', first_name, '!_', second_name, '!%%') Collate utf8_bin ESCAPE '!' 
            ORDER BY attribute;
END