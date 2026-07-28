-- Top Customers

SELECT
    customer_id,
    COUNT(DISTINCT order_id) AS total_orders,
    ROUND(SUM(price),2) AS total_spent
FROM warehouse.fact_sales

GROUP BY customer_id

ORDER BY total_spent DESC

LIMIT 20;