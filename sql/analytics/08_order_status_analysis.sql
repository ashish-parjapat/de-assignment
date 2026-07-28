-- Order Status Distribution

SELECT
    order_status,
    COUNT(*) AS total_orders,
    ROUND(SUM(price),2) AS revenue
FROM warehouse.fact_sales

GROUP BY order_status

ORDER BY total_orders DESC;