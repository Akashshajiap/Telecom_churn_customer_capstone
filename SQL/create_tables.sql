-- ============================================
-- step:2 Create a tables --
-- ============================================
-- create customer table --
  
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (

    customer_id VARCHAR(20) PRIMARY KEY,

    gender VARCHAR(20),
    age INT,
    married VARCHAR(20),
    number_of_dependents INT,

    city VARCHAR(100),
    zip_code INT,

    latitude DECIMAL(10,6),
    longitude DECIMAL(10,6),

    number_of_referrals INT,
    tenure_in_months INT,

    offer VARCHAR(100),

    phone_service VARCHAR(30),
    avg_monthly_long_distance_charges DECIMAL(10,2),
    multiple_lines VARCHAR(50),

    internet_service VARCHAR(50),
    internet_type VARCHAR(50),
    avg_monthly_gb_download DECIMAL(10,2),

    online_security VARCHAR(50),
    online_backup VARCHAR(50),
    device_protection_plan VARCHAR(50),
    premium_tech_support VARCHAR(50),

    streaming_tv VARCHAR(50),
    streaming_movies VARCHAR(50),
    streaming_music VARCHAR(50),

    unlimited_data VARCHAR(50),

    contract VARCHAR(50),
    paperless_billing VARCHAR(50),
    payment_method VARCHAR(100),

    monthly_charge DECIMAL(10,2),
    total_charges DECIMAL(12,2),
    total_refunds DECIMAL(12,2),
    total_extra_data_charges DECIMAL(12,2),
    total_long_distance_charges DECIMAL(12,2),
    total_revenue DECIMAL(12,2),

    customer_status VARCHAR(30),
    churn_category VARCHAR(100),
    churn_reason VARCHAR(255)

);

DESCRIBE customers;

select * FROM CUSTOMERS;

-- create ZIP population table --

-- the exact columns depend on the actual csv --
-- print(zip_population.columns.tolist())--  
   
create table zip_population(zip_code int primary key, population int);
   
describe zip_population;
select* from zip_population;


-- ============================================
-- step:3 -- check customers --
-- ============================================

select count(*) as customer_rows from customers;

-- ============================================
-- step:4 -- check unique customers --
-- ============================================

select count(distinct customer_id) as unique_customers from customers;

-- ============================================
-- step:5 -- check zip code --
-- ============================================

select count(*) as zip_rows from zip_population;