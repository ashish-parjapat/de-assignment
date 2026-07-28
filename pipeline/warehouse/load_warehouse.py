from pipeline.warehouse.staging_to_warehouse import (
    load_dim_customer,
    load_dim_date,
    load_dim_product,
    load_dim_seller,
    load_fact_sales,
)


def main():
    print("=" * 70)
    print("LOADING WAREHOUSE")
    print("=" * 70)

    load_dim_date()
    load_dim_customer()
    load_dim_product()
    load_dim_seller()
    load_fact_sales()

    print("\n🎉 Warehouse load completed successfully!")


if __name__ == "__main__":
    main()