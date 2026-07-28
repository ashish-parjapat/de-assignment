CREATE TABLE IF NOT EXISTS warehouse.fact_sales
(
    order_id String,
    order_item_id UInt8,

    customer_id String,
    product_id String,
    seller_id String,

    date_key UInt32,

    order_status LowCardinality(String),

    payment_type LowCardinality(Nullable(String)),
    payment_installments Nullable(UInt8),

    review_score Nullable(UInt8),

    price Decimal(10,2),
    freight_value Decimal(10,2),

    delivery_days Nullable(Int16),
    estimated_delivery_days Nullable(Int16)
)
ENGINE = MergeTree
ORDER BY (date_key, order_id, order_item_id);