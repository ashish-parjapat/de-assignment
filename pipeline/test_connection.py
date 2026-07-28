from sqlalchemy import text
from pipeline.config import config

print(config)
from pipeline.database import (
    get_clickhouse_client,
    get_postgres_engine,
)


def test_postgres():
    engine = get_postgres_engine()

    with engine.connect() as conn:
        version = conn.execute(text("SELECT version();")).scalar()

    print("✅ PostgreSQL Connected")
    print(version)


def test_clickhouse():
    client = get_clickhouse_client()

    version = client.command("SELECT version()")

    print("✅ ClickHouse Connected")
    print(version)


if __name__ == "__main__":
    test_postgres()
    test_clickhouse()