-- ============================================
-- step:1-- check customers count from customers --
-- ============================================

select count(*) as total_customers from customers;

-- ============================================
-- step:2 -- check duplicates customers count from customers --
-- ============================================

select 
	customer_id,
    count(*) as duplicate_customer
from customers
group by customer_id
having count(*)>1;

-- ============================================
-- step:3 -- check missing zip count from customers --
-- ============================================

select count(*) as missing_zip 
from customers
where zip_code is null;

-- ============================================
-- step:4 -- check duplicates zip count from zip_population--
-- ============================================

select 
	zip_code,
    count(*) as duplicate_count
from zip_population
group by zip_code
having count(*)>1;

-- ============================================
-- step:5 -- check missing population count from zip_population--
-- ============================================

select count(*) as missing_population 
from zip_population
where population is null;

