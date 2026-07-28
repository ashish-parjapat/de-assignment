from pathlib import Path
import shutil

import kagglehub

RAW_DATA_DIR = Path("data/raw")


def download_dataset() -> Path:
    print("Downloading Olist dataset...")

    dataset_path = Path(
        kagglehub.dataset_download("olistbr/brazilian-ecommerce")
    )

    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    for file in dataset_path.glob("*.csv"):
        destination = RAW_DATA_DIR / file.name

        if not destination.exists():
            shutil.copy(file, destination)

    print(f"Dataset available at: {RAW_DATA_DIR.resolve()}")

    return RAW_DATA_DIR


if __name__ == "__main__":
    download_dataset()