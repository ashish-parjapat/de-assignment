CREATE TABLE IF NOT EXISTS staging.order_items
(
    order_id String,
    order_item_id UInt16,
    product_id String,
    seller_id String,
    shipping_limit_date DateTime,
    price Decimal(10,2),
    freight_value Decimal(10,2)
)
ENGINE = MergeTree
ORDER BY (order_id, order_item_id);