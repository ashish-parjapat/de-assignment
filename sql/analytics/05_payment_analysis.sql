-- Payment Method Analysis

SELECT
    payment_type,
    COUNT(*) AS total_orders,
    ROUND(SUM(price),2) AS revenue,
    ROUND(AVG(payment_installments),2) AS avg_installments
FROM warehouse.fact_sales

GROUP BY payment_type

ORDER BY revenue DESC;