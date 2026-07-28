CREATE TABLE IF NOT EXISTS warehouse.dim_customer
(
    customer_id String,
    customer_city LowCardinality(String),
    customer_state FixedString(2)
)
ENGINE = MergeTree
ORDER BY customer_id;