CREATE PROCEDURE solution()
    SELECT id, IF ( given_answer IS NULL, 'no answer', IF ( given_answer = correct_answer, 'correct','incorrect') ) AS checks
    FROM answers
    ORDER BY id

CREATE PROCEDURE solution()
    SELECT id, IF ( IFNULL(given_answer, "no answer") = "no answer", "no answer", IF(given_answer = correct_answer, "correct", "incorrect") ) AS checks
    FROM answers
    ORDER BY id;
