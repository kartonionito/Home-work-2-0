import argparse
import os
import sys

# Попытка обычных импортов пакета
try:
    from etl.extract import extract_and_validate
    from etl.transform import transform
    from etl.load import load
except ModuleNotFoundError:
    # Если файл запущен напрямую из etl/, добавим корень проекта в sys.path
    ETL_DIR = os.path.dirname(os.path.abspath(__file__))          # .../Home-work-2-0/etl
    PROJECT_ROOT = os.path.dirname(ETL_DIR)                       # .../Home-work-2-0
    if PROJECT_ROOT not in sys.path:
        sys.path.insert(0, PROJECT_ROOT)
    from etl.extract import extract_and_validate
    from etl.transform import transform
    from etl.load import load


def main():
    # Базовые пути от корня проекта
    etl_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(etl_dir)

    # Дефолты: creds.db и имя таблицы
    default_creds = os.path.join(project_root, "data_base", "creds.db")
    default_table = "gavriliev"

    parser = argparse.ArgumentParser(description="ETL pipeline для employee-attrition.")
    parser.add_argument("--creds-db", type=str, default=default_creds,
                        help="Путь к creds.db (SQLite файл); по умолчанию data_base/creds.db")
    parser.add_argument("--table", type=str, default=default_table,
                        help="Имя таблицы для PostgreSQL (фамилия латиницей)")
    args = parser.parse_args()

    print("=== ETL Pipeline запущен ===")
    # 1) Extract
    raw_csv_path = extract_and_validate()

    # 2) Transform
    df = transform(raw_csv_path)

    # 3) Load: подготовим абсолютный путь к Parquet и директорию
    processed_dir = os.path.join(project_root, "data", "processed")
    os.makedirs(processed_dir, exist_ok=True)
    processed_parquet = os.path.join(processed_dir, "employee_processed.parquet")

    load(df, args.creds_db, processed_parquet, args.table)
    print("=== ETL Pipeline завершён успешно ===")


if __name__ == "__main__":
    main()
