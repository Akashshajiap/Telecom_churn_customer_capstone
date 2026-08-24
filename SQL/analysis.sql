-- ============================================
-- step:1 -- check total customers count from customers--
-- ============================================
use telecom_churn;

select count(*) as total_customers
from customers;

-- ============================================
-- step:2 -- check churned customers count from customers--
-- ============================================

select count(*) as churned_customers
from customers
where customer_status="churned";

-- ============================================
-- step:3 -- check churn rate from customers--
-- ============================================

select
	round(
		100.0*
        sum(customer_status='churned')
        /count(*),
        2
	) as churn_rate
from customers;

-- ============================================
-- step:4 -- Join Customers with zip population from customers--
-- ============================================

select
	c.customer_id,
    c.city,
    c.zip_code,
    z.population,
    c.contract,
    c.monthly_charge,
    c.total_revenue,
    c.customer_status
from customers c
left join zip_population z
	on c.zip_code=z.zip_code;

-- you have now combined information from: customers+zip_population usinig zip_code --

-- ============================================
-- step:5 -- churn by zip population from customers--
-- ============================================

select
	c.zip_code,
    z.population,
    count(c.customer_id) as customers,
    sum(c.customer_status = 'churned')
as churned_customers
from customers c
left join zip_population z
	on c.zip_code=z.zip_code
group by 
	c.zip_code,
    z.population
order by churned_customers desc;

-- this allows you to analyze churn geographically --

-- ============================================
-- step:6 -- Revenue by zip population from customers--
-- ============================================

select
	c.zip_code,
    z.population,
    count(c.customer_id) as customers,
    sum(c.total_revenue) as total_revenue
from customers c
left join zip_population z
	on c.zip_code=z.zip_code
group by
	c.zip_code,
    z.population
order by total_revenue desc;

-- ============================================
-- step:7 -- churn by city + population from customers--
-- ============================================

select
	c.city,
    z.zip_code,
    z.population,
    count(c.customer_id) as total_customers,
    sum(c.customer_status='churned') as churned_customers
from customers c
left join zip_population z
	on c.zip_code=z.zip_code
group by
	c.city,
    c.zip_code,
    z.population
order by churned_customers desc;

-- ============================================
-- step:8 -- churn rate by zip from customers--
-- ============================================

select
	c.zip_code,
    z.population,
    count(c.customer_id) as total_customers,
    sum(c.customer_status='churned') as churned_customers,
    round(
		100.0*
        sum(c.customer_status='churned')
        /count(c.custmer_id),2) as churn_rate
from customers c
left join zip_population z
	on c.zip_code=z.zip_code
group by
	c.zip_code,
    z.population
order by churn_rate desc;

-- this is a strong SQL interview example because it demonstrates: join, group by, count, sum, case/boolean aggregation, calculated metrics, business analysis --


    