from typing import List

from pipeline.database import get_clickhouse_client


class WarehouseValidator:
    def __init__(self):
        self.client = get_clickhouse_client()

    # ------------------------------------------------------------------
    # Generic Helpers
    # ------------------------------------------------------------------

    def execute_scalar(self, query: str):
        return self.client.command(query)

    def get_count(self, table: str) -> int:
        query = f"""
        SELECT COUNT(*)
        FROM {table}
        """
        return self.execute_scalar(query)

    def get_null_count(
        self,
        table: str,
        columns: List[str],
    ) -> int:
        condition = " OR ".join(
            f"{column} IS NULL"
            for column in columns
        )

        query = f"""
        SELECT COUNT(*)
        FROM {table}
        WHERE {condition}
        """

        return self.execute_scalar(query)

    def get_duplicate_count(
        self,
        table: str,
        columns: List[str],
    ) -> int:
        group_by = ", ".join(columns)

        query = f"""
        SELECT COUNT(*)
        FROM
        (
            SELECT
                {group_by},
                COUNT(*) AS cnt
            FROM {table}
            GROUP BY {group_by}
            HAVING cnt > 1
        )
        """

        return self.execute_scalar(query)

    # ------------------------------------------------------------------
    # Business Rule Validations
    # ------------------------------------------------------------------

    def get_negative_revenue_count(self) -> int:
        query = """
        SELECT COUNT(*)
        FROM warehouse.fact_sales
        WHERE
            price < 0
            OR freight_value < 0
        """

        return self.execute_scalar(query)

    def get_invalid_payment_count(self) -> int:
        query = """
        WITH order_totals AS
        (
            SELECT
                order_id,
                SUM(price + freight_value) AS order_total
            FROM staging.order_items
            GROUP BY order_id
        ),

        payment_totals AS
        (
            SELECT
                order_id,
                SUM(payment_value) AS payment_total
            FROM staging.order_payments
            GROUP BY order_id
        )

        SELECT COUNT(*)
        FROM
        (
            SELECT
                o.order_id,
                o.order_total,
                p.payment_total
            FROM order_totals o

            INNER JOIN payment_totals p
                ON o.order_id = p.order_id

            WHERE p.payment_total < o.order_total
        )
        """

        return self.execute_scalar(query)

    # ------------------------------------------------------------------
    # Referential Integrity
    # ------------------------------------------------------------------

    def get_missing_dimension_count(
        self,
        fact_table: str,
        fact_key: str,
        dimension_table: str,
        dimension_key: str,
    ) -> int:

        query = f"""
        SELECT COUNT(*)
        FROM {fact_table} f

        LEFT JOIN {dimension_table} d
            ON f.{fact_key} = d.{dimension_key}

        WHERE d.{dimension_key} IS NULL
        """

        return self.execute_scalar(query)

    # ------------------------------------------------------------------
    # Reconciliation
    # ------------------------------------------------------------------

    def row_count_matches(
        self,
        source_table: str,
        target_table: str,
    ) -> bool:

        return (
            self.get_count(source_table)
            == self.get_count(target_table)
        )