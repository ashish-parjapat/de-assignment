CREATE TABLE IF NOT EXISTS warehouse.dim_seller
(
    seller_id String,
    seller_city LowCardinality(String),
    seller_state FixedString(2)
)
ENGINE = MergeTree
ORDER BY seller_id;