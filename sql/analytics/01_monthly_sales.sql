-- Monthly Revenue Trend

SELECT
    d.year,
    d.month,
    d.month_name,
    COUNT(DISTINCT f.order_id) AS total_orders,
    ROUND(SUM(f.price),2) AS revenue,
    ROUND(AVG(f.price),2) AS average_order_value
FROM warehouse.fact_sales f

JOIN warehouse.dim_date d
ON f.date_key=d.date_key

GROUP BY
    d.year,
    d.month,
    d.month_name

ORDER BY
    d.year,
    d.month;