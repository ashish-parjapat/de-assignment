CREATE TABLE IF NOT EXISTS staging.sellers
(
    seller_id String,
    seller_zip_code_prefix UInt32,
    seller_city String,
    seller_state FixedString(2)
)
ENGINE = MergeTree
ORDER BY seller_id;