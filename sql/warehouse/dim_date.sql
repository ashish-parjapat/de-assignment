CREATE TABLE IF NOT EXISTS warehouse.dim_date
(
    date_key UInt32,
    date Date,
    day UInt8,
    month UInt8,
    month_name LowCardinality(String),
    quarter UInt8,
    year UInt16,
    week UInt8,
    weekday UInt8,
    weekday_name LowCardinality(String),
    is_weekend Bool
)
ENGINE = MergeTree
ORDER BY date_key;