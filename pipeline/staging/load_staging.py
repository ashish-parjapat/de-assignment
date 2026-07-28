from pipeline.quality.rules import RAW_TABLE_RULES
from pipeline.staging.postgres_to_clickhouse import (
    PostgresToClickHouseLoader,
)


def main():
    loader = PostgresToClickHouseLoader()

    print("\n" + "=" * 70)
    print("POSTGRES → CLICKHOUSE STAGING LOAD")
    print("=" * 70)

    successful = 0
    failed = []

    for table, rules in RAW_TABLE_RULES.items():

        try:
            loader.load_table(
                source_table=table,
                target_table=table,
                primary_key=rules["primary_key"],
            )

            successful += 1

        except Exception as e:
            print(f"\n❌ Failed loading {table}")
            print(e)
            failed.append(table)

    print("\n" + "=" * 70)

    print(f"Successful : {successful}")
    print(f"Failed     : {len(failed)}")

    if failed:
        print("\nFailed Tables")
        for table in failed:
            print(f" - {table}")

    else:
        print("\n🎉 All staging tables loaded successfully!")

    print("=" * 70)


if __name__ == "__main__":
    main()