from pipeline.quality.rules import RAW_TABLE_RULES
from pipeline.quality.validator import DataQualityValidator


def main():
    validator = DataQualityValidator(schema="raw")

    print("\n" + "=" * 60)
    print("RAW DATA QUALITY REPORT")
    print("=" * 60)

    total_tables = 0
    passed_tables = 0

    for table, rules in RAW_TABLE_RULES.items():
        total_tables += 1

        print(f"\nTable: {table}")
        print("-" * 60)

        rows = validator.get_row_count(table)
        print(f"Rows              : {rows:,}")

        primary_key = rules.get("primary_key")

        table_passed = True

        if primary_key:
            null_count = validator.get_null_count(table, primary_key)
            duplicate_count = validator.get_duplicate_count(table, primary_key)

            print(f"Null PK           : {null_count}")
            print(f"Duplicate PK      : {duplicate_count}")

            if null_count > 0 or duplicate_count > 0:
                table_passed = False

        else:
            print("Null PK           : SKIPPED")
            print("Duplicate PK      : SKIPPED")

        if table_passed:
            print("Status            : PASS")
            passed_tables += 1
        else:
            print("Status            : FAIL")

    print("\n" + "=" * 60)
    print(f"Tables Passed : {passed_tables}/{total_tables}")

    if passed_tables == total_tables:
        print("Overall Status : PASS")
    else:
        print("Overall Status : FAIL")

    print("=" * 60)


if __name__ == "__main__":
    main()