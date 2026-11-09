from pathlib import Path
# Root directory of the CricketIQ project
BASE_DIR = Path(__file__).resolve().parent.parent

# Main folders
DATA_DIR = BASE_DIR / "Data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"

MODELS_DIR = BASE_DIR / "Models"
REPORT_DIR = BASE_DIR / "Report"

# Input/output datasets
COMBINED_FILE = PROCESSED_DIR / "KOhli_delivery_Combined_2009-2026.csv"

MAPPED_FILE = PROCESSED_DIR / "kohli_ipl_with_match_metadata.csv"

# Create folders if they do not exist
for folder in [
    RAW_DIR,
    PROCESSED_DIR,
    MODELS_DIR,
    REPORT_DIR
]:
    folder.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    print("Project directory:", BASE_DIR)
    print("Raw data directory:", RAW_DIR)
    print("Processed data directory:", PROCESSED_DIR)
    print("Combined file exists:", COMBINED_FILE.exists())
    print("Mapped file exists:", MAPPED_FILE.exists())

