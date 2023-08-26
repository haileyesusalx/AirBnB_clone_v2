-- Creates a MySQL server with:
--   Database hbnb_test_db.
--   User hbnb_test
--   password hbnb_test_pwd in localhost.
--   Grants all privileges for hbnb_test on hbnb_test_db.
--   Grants SELECT privilege for hbnb_test on performance_schema.

-- Create the database 
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create the user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant privilege
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Grant privileges to hbnb_test
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Flush privileges 
FLUSH PRIVILEGES;
