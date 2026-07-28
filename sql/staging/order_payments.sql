CREATE TABLE IF NOT EXISTS staging.order_payments
(
    order_id String,
    payment_sequential UInt8,
    payment_type LowCardinality(String),
    payment_installments UInt8,
    payment_value Decimal(10,2)
)
ENGINE = MergeTree
ORDER BY (order_id, payment_sequential);