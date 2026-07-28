-- Top Product Categories

SELECT
    p.product_category_name,
    COUNT(*) AS items_sold,
    ROUND(SUM(f.price),2) AS revenue,
    ROUND(AVG(f.review_score),2) AS average_review
FROM warehouse.fact_sales f

JOIN warehouse.dim_product p
ON f.product_id=p.product_id

GROUP BY
    p.product_category_name

ORDER BY revenue DESC

LIMIT 10;