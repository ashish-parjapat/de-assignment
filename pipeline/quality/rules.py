RAW_TABLE_RULES = {
    "customers": {
        "primary_key": ["customer_id"],
    },
    "orders": {
        "primary_key": ["order_id"],
    },
    "order_items": {
        "primary_key": ["order_id", "order_item_id"],
    },
    "order_payments": {
        "primary_key": ["order_id", "payment_sequential"],
    },
    "order_reviews": {
        # review_id is not unique in the Olist dataset
        "primary_key": None,
    },
    "products": {
        "primary_key": ["product_id"],
    },
    "sellers": {
        "primary_key": ["seller_id"],
    },
    "product_category_name_translation": {
        "primary_key": ["product_category_name"],
    },
}