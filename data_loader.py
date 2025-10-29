import sys
import subprocess
import importlib
import pandas as pd


FILE_URL = "https://drive.google.com/uc?export=download&id=1J9aRbFxCiK_ueByy8_ius5ymk3vinwgC"


def ensure_pyarrow() -> None:
    """
    Гарантирует доступность pyarrow: импорт, при необходимости установка через pip, затем повторный импорт.
    Если установить не удалось — выбрасывает RuntimeError.
    """
    try:
        importlib.import_module("pyarrow")
        return
    except ImportError:
        print("pyarrow не найден — пытаюсь установить...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pyarrow", "--quiet"])
            importlib.invalidate_caches()
            importlib.import_module("pyarrow")
            print("✓ pyarrow установлен")
            return
        except Exception as e:
            raise RuntimeError(
                f"Не удалось установить/импортировать pyarrow: {e}\n"
                "Установите вручную: pip install pyarrow или conda install -c conda-forge pyarrow"
            )


def convert_data_types(df: pd.DataFrame) -> pd.DataFrame:
    """
    Приведение типов данных для DataFrame.
    """
    df_processed = df.copy()

    categorical_columns = [
        "Attrition", "BusinessTravel", "Department", "EducationField",
        "Gender", "JobRole", "MaritalStatus", "Over18", "OverTime"
    ]

    integer_columns = [
        "Age", "DailyRate", "DistanceFromHome", "Education", "EmployeeCount",
        "EmployeeNumber", "EnvironmentSatisfaction", "HourlyRate",
        "JobInvolvement", "JobLevel", "JobSatisfaction", "MonthlyIncome",
        "MonthlyRate", "NumCompaniesWorked", "PercentSalaryHike",
        "PerformanceRating", "RelationshipSatisfaction", "StandardHours",
        "StockOptionLevel", "TotalWorkingYears", "TrainingTimesLastYear",
        "WorkLifeBalance", "YearsAtCompany", "YearsInCurrentRole",
        "YearsSinceLastPromotion", "YearsWithCurrManager"
    ]

    for col in categorical_columns:
        if col in df_processed.columns:
            df_processed[col] = df_processed[col].astype("category")
            print(f"Преобразовано {col} в категориальный тип")

    for col in integer_columns:
        if col in df_processed.columns:
            df_processed[col] = (
                pd.to_numeric(df_processed[col], errors="coerce")
                  .fillna(0)
                  .astype("int64")
            )
            print(f"Преобразовано {col} в целочисленный тип")

    return df_processed


def save_dataset_parquet(df: pd.DataFrame) -> None:
    """
    Обязательное сохранение в Parquet с движком pyarrow.
    Без отката в CSV. В случае сбоя — исключение.
    """
    ensure_pyarrow()
    filename_parquet = "data_processed.parquet"
    # Явно указываем движок 'pyarrow'
    df.to_parquet(filename_parquet, index=False, engine="pyarrow")
    print(f"✓ Датасет сохранен как: {filename_parquet}")
    print(f"✓ Колонки: {list(df.columns)}")
    print(f"✓ Строк: {len(df)}")


def main():
    print("Загрузка датасета...")
    raw_data = pd.read_csv(FILE_URL)
    print("Датасет загружен!")

    print("\n" + "=" * 60)
    print("ПЕРВЫЕ 10 СТРОК ДАТАСЕТА:")
    print("=" * 60)
    print(raw_data.head(10))

    print("\n" + "=" * 60)
    print("ИНФОРМАЦИЯ О ТИПАХ ДАННЫХ (ДО ПРЕОБРАЗОВАНИЯ):")
    print("=" * 60)
    print(raw_data.dtypes)

    print("\n" + "=" * 60)
    print("ПРИВЕДЕНИЕ ТИПОВ ДАННЫХ...")
    print("=" * 60)
    df_processed = convert_data_types(raw_data)

    print("\n" + "=" * 60)
    print("ИНФОРМАЦИЯ О ТИПАХ ДАННЫХ (ПОСЛЕ ПРЕОБРАЗОВАНИЯ):")
    print("=" * 60)
    print(df_processed.dtypes)

    print("\n" + "=" * 60)
    print("СОХРАНЕНИЕ В PARQUET...")
    print("=" * 60)
    save_dataset_parquet(df_processed)

    print("\nОбработка завершена успешно!")


if __name__ == "__main__":
    main()

