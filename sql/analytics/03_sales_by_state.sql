-- Revenue by State

SELECT
    c.customer_state,
    COUNT(DISTINCT f.order_id) AS total_orders,
    ROUND(SUM(f.price),2) AS revenue
FROM warehouse.fact_sales f

JOIN warehouse.dim_customer c
ON f.customer_id=c.customer_id

GROUP BY
    c.customer_state

ORDER BY revenue DESC;