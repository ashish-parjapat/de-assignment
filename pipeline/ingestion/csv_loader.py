from pathlib import Path

import pandas as pd

from pipeline.database import get_postgres_engine

# Fix incorrect column names in the Olist dataset
COLUMN_RENAME_MAP = {
    "product_name_lenght": "product_name_length",
    "product_description_lenght": "product_description_length",
}


def load_csv_to_postgres(
    csv_path: Path,
    table_name: str,
    schema: str = "raw",
    chunksize: int = 10000,
):
    """
    Load a CSV file into a PostgreSQL table.
    """

    engine = get_postgres_engine()

    print(f"\n📂 Loading {csv_path.name} -> {schema}.{table_name}")

    try:
        for chunk in pd.read_csv(
            csv_path,
            chunksize=chunksize,
            keep_default_na=True,
        ):
            # Rename incorrect Olist column names
            chunk.rename(columns=COLUMN_RENAME_MAP, inplace=True)

            # Convert NaN to SQL NULL
            chunk = chunk.where(pd.notnull(chunk), None)

            chunk.to_sql(
                name=table_name,
                schema=schema,
                con=engine,
                if_exists="append",
                index=False,
                method="multi",
            )

        print(f"✅ Loaded {csv_path.name}")

    except Exception as e:
        print(f"❌ Failed to load {csv_path.name}")
        raise e