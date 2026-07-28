-- Delivery Performance

SELECT
    ROUND(AVG(delivery_days),2) AS average_delivery_days,

    ROUND(
        AVG(estimated_delivery_days),
        2
    ) AS average_estimated_days,

    COUNTIf(
        delivery_days >
        estimated_delivery_days
    ) AS delayed_orders
FROM warehouse.fact_sales;