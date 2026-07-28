from pipeline.ingestion.load_raw_data import main as load_raw
from pipeline.quality.validate_raw_data import main as validate_raw
from pipeline.staging.load_staging import main as load_staging
from pipeline.warehouse.load_warehouse import main as load_warehouse
from pipeline.warehouse.validate_warehouse import main as validate_warehouse


PIPELINE_STEPS = [
    ("1/5 Load Raw Data", load_raw),
    ("1/5 Validate Raw Data", validate_raw),
    ("2/5 Load Staging Layer", load_staging),
    ("3/5 Load Warehouse", load_warehouse),
    ("4/5 Validate Warehouse", validate_warehouse),
]


def main():
    print("=" * 80)
    print("DATA ENGINEERING PIPELINE")
    print("=" * 80)

    for step_name, step in PIPELINE_STEPS:
        print(f"\n{'=' * 80}")
        print(step_name)
        print("=" * 80)

        step()

    print("\n🎉 Pipeline completed successfully!")


if __name__ == "__main__":
    main()


PIPELINE_STEPS = [
    ("Load Raw Data", load_raw),
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