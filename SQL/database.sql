-- ============================================
-- step:1 Create a Database --
-- ============================================
create database telecom_churn; 
USE telecom_churn;




-- ============================================
-- Step 2 — Don't use the Table Data Import Wizard yet --
-- Since it is repeatedly stopping at exactly 4,835 rows, let's use MySQL's CSV loading method instead. --
-- However, on Windows, LOAD DATA LOCAL INFILE may be disabled by default. --
-- ============================================

-- SHOW VARIABLES LIKE 'local_infile';

-- ============================================
-- Step 3 — Check current status -- "SHOW VARIABLES LIKE 'local_infile';" -- using this--
-- Step 4 — shows "local_infile    OFF" then, --
-- Step 6 — Enable it temporarily --
-- ============================================

-- SET GLOBAL local_infile = 1;

-- then recheck using -> "SHOW VARIABLES LIKE 'local_infile';" --


-- ============================================
-- Step 7 — If local_infile is ON --
-- ============================================

-- LOAD DATA LOCAL INFILE 'C:/Users/LENOVO/OneDrive/Desktop/Telecom+Customer+Churn capstone project/Python/telecom_customer_churn_cleaned.csv'
-- INTO TABLE customers
-- FIELDS TERMINATED BY ','
-- ENCLOSED BY '"'
-- LINES TERMINATED BY '\r\n'
-- IGNORE 1 ROWS;

-- SELECT COUNT(*) FROM customers;
-- SELECT COUNT(*) as total_customers FROM customers;
-- SHOW VARIABLES LIKE 'local_infile';  
-- -- 

