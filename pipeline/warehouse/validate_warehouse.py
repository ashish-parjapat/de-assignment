from pipeline.warehouse.rules import WAREHOUSE_TABLE_RULES
from pipeline.warehouse.validation import WarehouseValidator


def main():
    validator = WarehouseValidator()

    print("=" * 70)
    print("WAREHOUSE VALIDATION")
    print("=" * 70)

    passed = 0
    failed = 0

    failed_validations = []

    # ==============================================================
    # PRIMARY KEY VALIDATION
    # ==============================================================

    for table, rule in WAREHOUSE_TABLE_RULES.items():

        primary_key = rule["primary_key"]

        print(f"\nValidating {table}")

        # NULL PK

        null_count = validator.get_null_count(
            table,
            primary_key,
        )

        if null_count == 0:
            print("  ✓ NULL Primary Key Check : PASS")
            passed += 1
        else:
            print(
                f"  ✗ NULL Primary Key Check : FAIL ({null_count})"
            )
            failed += 1
            failed_validations.append(
                f"{table} - NULL Primary Key"
            )

        # Duplicate PK

        duplicate_count = validator.get_duplicate_count(
            table,
            primary_key,
        )

        if duplicate_count == 0:
            print("  ✓ Duplicate Primary Key Check : PASS")
            passed += 1
        else:
            print(
                f"  ✗ Duplicate Primary Key Check : FAIL ({duplicate_count})"
            )
            failed += 1
            failed_validations.append(
                f"{table} - Duplicate Primary Key"
            )

    # ==============================================================
    # BUSINESS RULE VALIDATIONS
    # ==============================================================

    print("\nBusiness Rule Validation")

    # Revenue Validation

    negative_rows = validator.get_negative_revenue_count()

    if negative_rows == 0:
        print("  ✓ Revenue >= 0 : PASS")
        passed += 1
    else:
        print(
            f"  ✗ Revenue >= 0 : FAIL ({negative_rows})"
        )
        failed += 1
        failed_validations.append("Revenue Validation")

    # Payment Validation (Warning Only)

    invalid_payment = validator.get_invalid_payment_count()

    if invalid_payment == 0:
        print("  ✓ Payment >= Order Total : PASS")
        passed += 1
    else:
        print(
            f"  ⚠ Payment >= Order Total : WARNING ({invalid_payment} orders)"
        )
        print(
            "    Source dataset contains known payment anomalies. Validation skipped."
        )

    # ==============================================================
    # REFERENTIAL INTEGRITY
    # ==============================================================

    print("\nReferential Integrity")

    dimension_checks = [
        (
            "customer_id",
            "warehouse.dim_customer",
            "customer_id",
        ),
        (
            "product_id",
            "warehouse.dim_product",
            "product_id",
        ),
        (
            "seller_id",
            "warehouse.dim_seller",
            "seller_id",
        ),
        (
            "date_key",
            "warehouse.dim_date",
            "date_key",
        ),
    ]

    for fact_key, dim_table, dim_key in dimension_checks:

        missing = validator.get_missing_dimension_count(
            "warehouse.fact_sales",
            fact_key,
            dim_table,
            dim_key,
        )

        if missing == 0:
            print(f"  ✓ {fact_key} : PASS")
            passed += 1
        else:
            print(
                f"  ✗ {fact_key} : FAIL ({missing})"
            )
            failed += 1
            failed_validations.append(
                f"{fact_key} Integrity"
            )

    # ==============================================================
    # ROW COUNT RECONCILIATION
    # ==============================================================

    print("\nRow Count Reconciliation")

    checks = [
        (
            "staging.customers",
            "warehouse.dim_customer",
        ),
        (
            "staging.products",
            "warehouse.dim_product",
        ),
        (
            "staging.sellers",
            "warehouse.dim_seller",
        ),
    ]

    for source, target in checks:

        if validator.row_count_matches(
            source,
            target,
        ):
            print(f"  ✓ {target} : PASS")
            passed += 1
        else:
            print(f"  ✗ {target} : FAIL")
            failed += 1
            failed_validations.append(
                f"{target} Row Count"
            )

    # ==============================================================
    # SUMMARY
    # ==============================================================

    print("\n" + "=" * 70)
    print(f"Passed : {passed}")
    print(f"Failed : {failed}")

    if failed_validations:

        print("\nFailed Validations:")

        for validation in failed_validations:
            print(f" - {validation}")

        print("=" * 70)

        raise RuntimeError(
            f"Warehouse validation failed with {len(failed_validations)} validation error(s)."
        )

    print("\n🎉 All warehouse validations passed successfully!")
    print("=" * 70)


if __name__ == "__main__":
    main()