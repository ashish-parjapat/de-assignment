WAREHOUSE_TABLE_RULES = {
    "warehouse.dim_customer": {
        "primary_key": ["customer_id"],
    },
    "warehouse.dim_product": {
        "primary_key": ["product_id"],
    },
    "warehouse.dim_seller": {
        "primary_key": ["seller_id"],
    },
    "warehouse.dim_date": {
        "primary_key": ["date_key"],
    },
    "warehouse.fact_sales": {
        "primary_key": [
            "order_id",
            "order_item_id",
        ],
    },
}