-- Listing all records of second_table score >= 10 from database hbtn_0c_0
-- DESC for ordering records in descending order
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
