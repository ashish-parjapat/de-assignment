import pandas as pd

COLUMN_RENAME_MAP = {
    "product_name_lenght": "product_name_length",
    "product_description_lenght": "product_description_length",
}


def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Rename inconsistent column names.
    """
    return df.rename(columns=COLUMN_RENAME_MAP)


def standardize_nulls(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert pandas NaN to None.
    """
    return df.where(pd.notnull(df), None)


def parse_timestamps(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert timestamp columns to datetime.
    """
    for column in df.columns:
        if (
            "timestamp" in column
            or column.endswith("_date")
            or column.endswith("_at")
        ):
            df[column] = pd.to_datetime(
                df[column],
                errors="coerce",
            )

    return df


def remove_duplicates(df: pd.DataFrame, primary_key: list[str] | None) -> pd.DataFrame:
    """
    Remove duplicate records based on the configured primary key.
    """
    if primary_key:
        return df.drop_duplicates(subset=primary_key)

    return df