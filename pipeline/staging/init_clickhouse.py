from pathlib import Path

from pipeline.database import get_clickhouse_client


def execute_sql_files(sql_directory: Path):
    client = get_clickhouse_client()

    # Create staging database if it doesn't exist
    client.command("CREATE DATABASE IF NOT EXISTS staging")

    sql_files = sorted(sql_directory.glob("*.sql"))

    if not sql_files:
        print(f"No SQL files found in {sql_directory}")
        return

    print("\n" + "=" * 70)
    print("INITIALIZING CLICKHOUSE STAGING")
    print("=" * 70)

    successful = 0
    failed = []

    for sql_file in sql_files:
        try:
            print(f"Creating {sql_file.name}")

            sql = sql_file.read_text(encoding="utf-8")

            client.command(sql)

            successful += 1

            print("✓ Success")

        except Exception as e:
            print(f"✗ Failed: {e}")
            failed.append(sql_file.name)

    print("\n" + "=" * 70)
    print(f"Successful : {successful}")
    print(f"Failed     : {len(failed)}")

    if failed:
        print("\nFailed Files")
        for file in failed:
            print(f" - {file}")
    else:
        print("\n🎉 ClickHouse staging initialized successfully!")

    print("=" * 70)


def main():
    project_root = Path(__file__).resolve().parents[2]

    sql_directory = project_root / "sql" / "staging"

    execute_sql_files(sql_directory)


if __name__ == "__main__":
    main()