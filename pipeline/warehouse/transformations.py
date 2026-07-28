from datetime import date, timedelta
import pandas as pd


def generate_date_dimension(start_date: str, end_date: str) -> pd.DataFrame:
    """
    Generate a Date Dimension DataFrame.
    """
    start = date.fromisoformat(start_date)
    end = date.fromisoformat(end_date)

    rows = []

    current = start

    while current <= end:
        rows.append(
            {
                "date_key": int(current.strftime("%Y%m%d")),
                "date": current,
                "day": current.day,
                "month": current.month,
                "month_name": current.strftime("%B"),
                "quarter": (current.month - 1) // 3 + 1,
                "year": current.year,
                "week": current.isocalendar().week,
                "weekday": current.isoweekday(),
                "weekday_name": current.strftime("%A"),
                "is_weekend": current.weekday() >= 5,
            }
        )

        current += timedelta(days=1)

    return pd.DataFrame(rows)

def transform_dim_customer(df: pd.DataFrame) -> pd.DataFrame:
    columns = [
        "customer_id",
        "customer_city",
        "customer_state",
    ]

    return (
        df[columns]
        .drop_duplicates()
        .reset_index(drop=True)
    )


def transform_dim_product(df: pd.DataFrame) -> pd.DataFrame:
    columns = [
        "product_id",
        "product_category_name",
        "product_weight_g",
        "product_length_cm",
        "product_height_cm",
        "product_width_cm",
    ]

    return (
        df[columns]
        .drop_duplicates()
        .reset_index(drop=True)
    )


def transform_dim_seller(df: pd.DataFrame) -> pd.DataFrame:
    columns = [
        "seller_id",
        "seller_city",
        "seller_state",
    ]

    return (
        df[columns]
        .drop_duplicates()
        .reset_index(drop=True)
    )