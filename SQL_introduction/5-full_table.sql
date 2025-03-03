-- Script that prints the full description of the table first_table
-- from the database hbtn_0c_0 in your MySQL server
-- The database name will be passed as an argument of the mysql command

SELECT CONCAT(
    'Table   ', TABLE_NAME, '\n',
    'Create Table: CREATE TABLE `', TABLE_NAME, '` (\n  `id` int DEFAULT NULL,\n  `name` varchar(256) DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci'
) AS '' FROM INFORMATION_SCHEMA.TABLES 
WHERE TABLE_SCHEMA = DATABASE() 
AND TABLE_NAME = 'first_table';