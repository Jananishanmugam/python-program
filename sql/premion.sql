You work for an e-commerce marketplace. Your goal is to evaluate product performance relative to other products from the same seller, but only for repeat buyers who purchased from that seller more than once.

Tables
sellers
| seller_id | seller_name | onboarding_date |
| --------- | ----------------- | --------------- |
| 201 | "Urban Styles" | 2024-01-10 |
| 202 | "Home Essentials" | 2024-03-05 |

products
| product_id | seller_id | product_name | category | price |
| ---------- | --------- | -------------- | ----------- | ----- |
| 1 | 201 | "Denim Jacket" | Apparel | 80 |
| 2 | 201 | "Leather Belt" | Accessories | 35 |
| 3 | 201 | "Sneakers" | Footwear | 120 |
| 4 | 202 | "Coffee Maker" | Appliances | 150 |

orders
| order_id | user_id | order_date |
| -------- | ------- | ---------- |
| 5001 | 301 | 2025-08-05 |
| 5002 | 301 | 2025-08-18 |
| 5003 | 302 | 2025-08-10 |
| 5004 | 303 | 2025-08-20 |

order_items
| order_item_id | order_id | product_id | quantity |
| ------------- | -------- | ---------- | -------- |
| 9001 | 5001 | 1 | 1 |
| 9002 | 5001 | 2 | 1 |
| 9003 | 5002 | 3 | 1 |
| 9004 | 5003 | 1 | 1 |
| 9005 | 5004 | 4 | 1 |


Find the top-performing product per seller in August 2025, but only considering repeat buyers who purchased from more than one product of the same seller.
For these qualified buyers:
Count total orders, units sold, and revenue per product.
Calculate Revenue per Order (RPO)
RPO = total_revenue / total_orders


Exclude products with:
0 orders
0 revenue from qualified buyers
Rank products per seller by RPO (highest first).
Return only the top 1 product per seller.

o/p :
seller_id product_id total_order RTO
201      


















ans:

with cte as (
select  user_id, seller_id, count(distinct(product_id) ) as cnt  from order o

left join order_items oi
on o.order_id = oi.order_id

left join products p
on p.product_id = oi.product_id

where order_date between '2025-08-01' and '2025-08-31'
group by user_id, seller_id
having cnt > 1

),

select *, dense_rank() over(partition by seller_id order by RTO desc) as rank from (
select seller_id, product_id, count(order_id) as total_orders, sum(quantity) as units_sold, (sum(price) /count(order_id) ) as RPO

from cte c
left join products p
on p.product_id = c.product_id

left join order_items oi
on p.product_id = oi.product_id

group by seller_id, product_id
order by 3 desc)

where rank = 1

