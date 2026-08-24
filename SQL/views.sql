-- ============================================
-- step:1 -- Create power BI view from customers--
-- ============================================
use telecom_churn;

create view vw_customer_geography as 
select
	c.customer_id,
    c.gender,
    c.age,
    c.city,
    c.zip_code,
    z.population,
    c.tenure_in_months,
    c.contract,
    c.internet_service,
    c.internet_type,
    c.payment_method,
    c.monthly_charge,
    c.total_charges,
    c.total_revenue,
    c.customer_status,
    c.churn_category,
    c.churn_reason
from customers c
left join zip_population z
	on c.zip_code=z.zip_code;
    
-- NOW: --

SELECT * FROM VW_CUSTOMER_GEOGRAPHY 
LIMIT 10;

-- THIS VIEW COMBINES THE TWO TABLES FOR POWER BI ANALYSIS --
    