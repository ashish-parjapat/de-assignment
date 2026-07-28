CREATE TABLE IF NOT EXISTS staging.customers
(
    customer_id String,
    customer_unique_id String,
    customer_zip_code_prefix UInt32,
    customer_city String,
    customer_state FixedString(2)
)
ENGINE = MergeTree
ORDER BY customer_id;