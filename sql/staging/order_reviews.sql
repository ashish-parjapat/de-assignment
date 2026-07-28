CREATE TABLE IF NOT EXISTS staging.order_reviews
(
    review_id String,
    order_id String,
    review_score UInt8,
    review_comment_title Nullable(String),
    review_comment_message Nullable(String),
    review_creation_date DateTime,
    review_answer_timestamp DateTime
)
ENGINE = MergeTree
ORDER BY order_id;