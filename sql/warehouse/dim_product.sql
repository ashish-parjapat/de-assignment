CREATE TABLE IF NOT EXISTS warehouse.dim_product
(
    product_id String,
    product_category_name LowCardinality(Nullable(String)),
    product_weight_g Nullable(UInt32),
    product_length_cm Nullable(UInt16),
    product_height_cm Nullable(UInt16),
    product_width_cm Nullable(UInt16)
)
ENGINE = MergeTree
ORDER BY product_id;