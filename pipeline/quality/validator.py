from sqlalchemy import text

from pipeline.database import get_postgres_engine


class DataQualityValidator:
    def __init__(self, schema: str):
        self.schema = schema
        self.engine = get_postgres_engine()

    def get_row_count(self, table: str) -> int:
        query = text(f"""
            SELECT COUNT(*)
            FROM {self.schema}.{table}
        """)

        with self.engine.connect() as conn:
            return conn.execute(query).scalar()

    def get_null_count(self, table: str, columns: list[str]) -> int:
        where_clause = " OR ".join(f"{column} IS NULL" for column in columns)

        query = text(f"""
            SELECT COUNT(*)
            FROM {self.schema}.{table}
            WHERE {where_clause}
        """)

        with self.engine.connect() as conn:
            return conn.execute(query).scalar()

    def get_duplicate_count(self, table: str, columns: list[str]) -> int:
        group_by = ", ".join(columns)

        query = text(f"""
            SELECT COUNT(*)
            FROM (
                SELECT {group_by}
                FROM {self.schema}.{table}
                GROUP BY {group_by}
                HAVING COUNT(*) > 1
            ) duplicates
        """)

        with self.engine.connect() as conn:
            return conn.execute(query).scalar()