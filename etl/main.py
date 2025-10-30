import argparse
import os
from etl.extract import extract_and_validate
from etl.transform import transform
from etl.load import load

def main():
    parser = argparse.ArgumentParser(description="ETL pipeline для employee-attrition.")
    parser.add_argument("--creds-db", type=str, required=True, help="Путь к creds.db (SQLite файл)")
    parser.add_argument("--table", type=str, required=True, help="Имя таблицы для PostgreSQL (фамилия латиницей)")
    args = parser.parse_args()

    print("=== ETL Pipeline запущен ===")
    # 1. Extract
    raw_csv_path = extract_and_validate()

    # 2. Transform
    df = transform(raw_csv_path)

    # 3. Load
    processed_parquet = os.path.join("data", "processed", "employee_processed.parquet")
    load(df, args.creds_db, processed_parquet, args.table)
    print("=== ETL Pipeline завершён успешно ===")

if __name__ == "__main__":
    main()
