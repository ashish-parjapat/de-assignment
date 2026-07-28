-- Top Sellers

SELECT
    s.seller_id,
    s.seller_state,
    COUNT(*) AS items_sold,
    ROUND(SUM(f.price),2) AS revenue
FROM warehouse.fact_sales f

JOIN warehouse.dim_seller s
ON f.seller_id=s.seller_id

GROUP BY
    s.seller_id,
    s.seller_state

ORDER BY revenue DESC

LIMIT 10;