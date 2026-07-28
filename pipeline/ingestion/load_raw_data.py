from pathlib import Path

from pipeline.ingestion.csv_loader import load_csv_to_postgres

RAW_DATA_DIR = Path("data/raw")

DATASETS = {
    "olist_customers_dataset.csv": "customers",
    "olist_orders_dataset.csv": "orders",
    "olist_order_items_dataset.csv": "order_items",
    "olist_order_payments_dataset.csv": "order_payments",
    "olist_order_reviews_dataset.csv": "order_reviews",
    "olist_products_dataset.csv": "products",
    "olist_sellers_dataset.csv": "sellers",
    "product_category_name_translation.csv": "product_category_name_translation",
}


def main():
    print("🚀 Starting raw data ingestion...\n")

    failed_tables = []

    for csv_file, table_name in DATASETS.items():
        csv_path = RAW_DATA_DIR / csv_file

        if not csv_path.exists():
            print(f"⚠️ File not found: {csv_file}")
            failed_tables.append(table_name)
            continue

        try:
            load_csv_to_postgres(
                csv_path=csv_path,
                table_name=table_name,
            )
        except Exception as e:
            print(f"❌ Error loading '{table_name}': {e}\n")
            failed_tables.append(table_name)

    print("\n========================================")

    if failed_tables:
        print("⚠️ Raw data ingestion completed with errors.")
        print("Failed tables:")
        for table in failed_tables:
            print(f"  - {table}")
    else:
        print("🎉 Raw data ingestion completed successfully!")

    print("========================================")


if __name__ == "__main__":
    main()