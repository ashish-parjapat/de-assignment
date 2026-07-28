import pandas as pd

from pipeline.database import (
    get_clickhouse_client,
    get_postgres_engine,
)
from pipeline.staging.transformations import (
    parse_timestamps,
    remove_duplicates,
    rename_columns,
    standardize_nulls,
)


class PostgresToClickHouseLoader:
    def __init__(self):
        self.pg_engine = get_postgres_engine()
        self.ch_client = get_clickhouse_client()

    def load_table(
        self,
        source_table: str,
        target_table: str,
        primary_key: list[str] | None = None,
    ):
        print(f"\nLoading {source_table} -> staging.{target_table}")

        # Read from PostgreSQL
        query = f"SELECT * FROM raw.{source_table}"

        df = pd.read_sql(query, self.pg_engine)

        print(f"Rows extracted : {len(df):,}")

        # -----------------------------
        # Apply staging transformations
        # -----------------------------
        df = rename_columns(df)
        df = parse_timestamps(df)
        df = standardize_nulls(df)
        df = remove_duplicates(df, primary_key)

        print(f"Rows after cleaning : {len(df):,}")

        # -----------------------------
        # Load into ClickHouse
        # -----------------------------
        self.ch_client.command(
            f"TRUNCATE TABLE staging.{target_table}"
        )

        self.ch_client.insert_df(
            table=f"staging.{target_table}",
            df=df,
        )

        print(f"Loaded {len(df):,} rows into staging.{target_table}")