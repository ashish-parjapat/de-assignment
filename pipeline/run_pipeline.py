from pipeline.ingestion.load_raw import main as load_raw
from pipeline.raw.validate_raw import main as validate_raw
from pipeline.staging.load_staging import main as load_staging
from pipeline.warehouse.load_warehouse import main as load_warehouse
from pipeline.warehouse.validate_warehouse import main as validate_warehouse


PIPELINE_STEPS = [
    ("Load Raw Data", load_raw),
    ("Validate Raw Data", validate_raw),
    ("Load Staging Layer", load_staging),
    ("Load Warehouse", load_warehouse),
    ("Validate Warehouse", validate_warehouse),
]


def main():

    print("=" * 80)
    print("DATA ENGINEERING PIPELINE")
    print("=" * 80)

    for name, step in PIPELINE_STEPS:

        print(f"\n{'=' * 80}")
        print(name)
        print("=" * 80)

        step()

    print("\n🎉 Pipeline completed successfully!")


if __name__ == "__main__":
    main()