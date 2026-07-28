
import pandas as pd

from pipeline.database import get_clickhouse_client, get_postgres_engine
from pipeline.warehouse.transformations import (
    generate_date_dimension,
    transform_dim_customer,
    transform_dim_product,
    transform_dim_seller,
)

def load_dim_date():
    client = get_clickhouse_client()

    df = generate_date_dimension(
        start_date="2016-01-01",
        end_date="2018-12-31",
    )

    client.command("TRUNCATE TABLE warehouse.dim_date")

    client.insert_df(
        "warehouse.dim_date",
        df,
    )

    print(f"Loaded {len(df)} rows into warehouse.dim_date")



def load_dim_customer():
    load_dimension(
        staging_table="customers",
        warehouse_table="dim_customer",
        transform_function=transform_dim_customer,
    )


def load_dim_product():
    load_dimension(
        staging_table="products",
        warehouse_table="dim_product",
        transform_function=transform_dim_product,
    )


def load_dim_seller():
    load_dimension(
        staging_table="sellers",
        warehouse_table="dim_seller",
        transform_function=transform_dim_seller,
    )


def load_dimension(
    staging_table: str,
    warehouse_table: str,
    transform_function,
):
    client = get_clickhouse_client()

    query = f"SELECT * FROM staging.{staging_table}"

    df = client.query_df(query)

    df = transform_function(df)

    client.command(f"TRUNCATE TABLE warehouse.{warehouse_table}")

    client.insert_df(
        f"warehouse.{warehouse_table}",
        df,
    )

    print(
        f"Loaded {len(df)} rows into warehouse.{warehouse_table}"
    )

def build_fact_sales():
    client = get_clickhouse_client()

    query = """
    SELECT
    oi.order_id AS order_id,
    oi.order_item_id AS order_item_id,

    o.customer_id AS customer_id,

    oi.product_id AS product_id,
    oi.seller_id AS seller_id,

    toUInt32(formatDateTime(o.order_purchase_timestamp, '%Y%m%d')) AS date_key,

    o.order_status AS order_status,

    p.payment_type AS payment_type,
    p.payment_installments AS payment_installments,

    r.review_score AS review_score,

    oi.price AS price,
    oi.freight_value AS freight_value,

    dateDiff(
        'day',
        toDate(o.order_purchase_timestamp),
        toDate(o.order_delivered_customer_date)
    ) AS delivery_days,

    dateDiff(
        'day',
        toDate(o.order_purchase_timestamp),
        toDate(o.order_estimated_delivery_date)
    ) AS estimated_delivery_days

    FROM staging.order_items oi

    INNER JOIN staging.orders o
        ON oi.order_id = o.order_id

    LEFT JOIN
(
    SELECT
        order_id,
        any(payment_type) AS payment_type,
        max(payment_installments) AS payment_installments
    FROM staging.order_payments
    GROUP BY order_id
) p
ON oi.order_id = p.order_id

    LEFT JOIN
(
    SELECT
        order_id,
        max(review_score) AS review_score
    FROM staging.order_reviews
    GROUP BY order_id
) r
ON oi.order_id = r.order_id
    """

    return client.query_df(query)


def load_fact_sales():
    client = get_clickhouse_client()

    df = build_fact_sales()

    client.command("TRUNCATE TABLE warehouse.fact_sales")

    client.insert_df(
        "warehouse.fact_sales",
        df,
    )

    print(f"Loaded {len(df)} rows into warehouse.fact_sales")