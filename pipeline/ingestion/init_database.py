from pathlib import Path

from sqlalchemy import text

from pipeline.database import get_postgres_engine

SQL_DIR = Path("sql/raw")


def execute_sql_file(engine, sql_file: Path) -> None:
    """Execute a single SQL file."""

    with open(sql_file, "r", encoding="utf-8") as file:
        sql = file.read()

    with engine.begin() as connection:
        connection.execute(text(sql))

    print(f"✅ Executed {sql_file.name}")


def main():
    engine = get_postgres_engine()

    # Create schemas first
    execute_sql_file(engine, SQL_DIR / "create_raw_schema.sql")

    # Create tables
    for sql_file in sorted(SQL_DIR.glob("*.sql")):
        if sql_file.name == "create_raw_schema.sql":
            continue

        execute_sql_file(engine, sql_file)

    print("\n🎉 Database initialization completed.")


if __name__ == "__main__":
    main()