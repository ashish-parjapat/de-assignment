CREATE TABLE IF NOT EXISTS staging.products
(
    product_id String,
    product_category_name LowCardinality(Nullable(String)),
    product_name_length Nullable(UInt16),
    product_description_length Nullable(UInt16),
    product_photos_qty Nullable(UInt16),
    product_weight_g Nullable(UInt32),
    product_length_cm Nullable(UInt16),
    product_height_cm Nullable(UInt16),
    product_width_cm Nullable(UInt16)
)
ENGINE = MergeTree
ORDER BY product_id;