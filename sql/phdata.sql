Given a table of transactions and a table of users, write a query to determine if users tend to order more to their primary address versus other addresses.

Note: Return the percentage of transactions ordered to their home address as home_address_percent.
Example:
Input:

transactions table:
Columns Type
id INTEGER
user_id INTEGER
created_at DATETIME
shipping_address VARCHAR

users table:
Columns Type
id INTEGER
name VARCHAR
address VARCHAR

Example Output:home_address_percent 0.76

percent = (home_address/ overall_address) * 100
user 
1      2   3


with cte as (
select user_name, count(case when t.shipping_address = u.address then 1 end) as home_address_match, count(shipping_address) as total_count
from transactions t 
join users u
on t.user_id = u.id 
group by user_name)

select user_name, ( home_address_match::numeric /total_count) * 100 from cte



Write a query to identify customers who placed more than three transactions each in both 2019 and 2020.
Example:
Input:

transactions table
Column Type
id INTEGER
user_id INTEGER
created_at DATETIME
product_id INTEGER
quantity INTEGER

users table
Column Type
id INTEGER
name VARCHAR

Output:
Column Type
customer_name VARCHAR


with cte as (
select  t.id, u.name as customer_name, EXTRACT(YEAR from t.created_at) as year_date 
from transcations t 
join users u 
on t.user_id = u.id
), 
with cte2 as (
select customer_name, year_date, count(t.id)  from cte
where year_date = 2019 or year_date = 2020
group by 1,2
having count(t.id) >= 3
)

select distinct customer_name
from cte2
group By year_date
having count(year_date)=2
