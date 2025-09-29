import pandas as pd


def main():
    print("Загрузка датасета...")

    # Прямая ссылка на скачивание
    file_url = "https://drive.google.com/uc?export=download&id=1J9aRbFxCiK_ueByy8_ius5ymk3vinwgC"

    try:
        raw_data = pd.read_csv(file_url)
        print("Датасет загружен!")

        # Вывод информации о датасете
        print("\n" + "=" * 60)
        print("ПЕРВЫЕ 10 СТРОК ДАТАСЕТА:")
        print("=" * 60)
        print(raw_data.head(10))

        # Вывод информации о типах данных ДО преобразования
        print("\n" + "=" * 60)
        print("ИНФОРМАЦИЯ О ТИПАХ ДАННЫХ (ДО ПРЕОБРАЗОВАНИЯ):")
        print("=" * 60)
        print(raw_data.dtypes)

        # Приведение типов данных
        print("\n" + "=" * 60)
        print("ПРИВЕДЕНИЕ ТИПОВ ДАННЫХ...")
        print("=" * 60)

        df_processed = convert_data_types(raw_data)

        # Вывод информации о типах данных ПОСЛЕ преобразования
        print("\n" + "=" * 60)
        print("ИНФОРМАЦИЯ О ТИПАХ ДАННЫХ (ПОСЛЕ ПРЕОБРАЗОВАНИЯ):")
        print("=" * 60)
        print(df_processed.dtypes)

        # Сохранение в CSV формате
        print("\n" + "=" * 60)
        print("СОХРАНЕНИЕ ДАТАСЕТА...")
        print("=" * 60)
        save_dataset(df_processed)

        print("\nОбработка завершена успешно!")

    except Exception as e:
        print(f"Ошибка: {e}")
        print("Проверьте доступность файла и интернет-соединение")


def convert_data_types(df):
    """
    Приведение типов данных для DataFrame
    """
    df_processed = df.copy()

    # Категориальные переменные
    categorical_columns = [
        'Attrition', 'BusinessTravel', 'Department', 'EducationField',
        'Gender', 'JobRole', 'MaritalStatus', 'Over18', 'OverTime'
    ]

    # Числовые переменные (целые числа)
    integer_columns = [
        'Age', 'DailyRate', 'DistanceFromHome', 'Education', 'EmployeeCount',
        'EmployeeNumber', 'EnvironmentSatisfaction', 'HourlyRate',
        'JobInvolvement', 'JobLevel', 'JobSatisfaction', 'MonthlyIncome',
        'MonthlyRate', 'NumCompaniesWorked', 'PercentSalaryHike',
        'PerformanceRating', 'RelationshipSatisfaction', 'StandardHours',
        'StockOptionLevel', 'TotalWorkingYears', 'TrainingTimesLastYear',
        'WorkLifeBalance', 'YearsAtCompany', 'YearsInCurrentRole',
        'YearsSinceLastPromotion', 'YearsWithCurrManager'
    ]

    # Преобразование категориальных переменных
    for col in categorical_columns:
        if col in df_processed.columns:
            df_processed[col] = df_processed[col].astype('category')
            print(f"Преобразовано {col} в категориальный тип")

    # Преобразование числовых переменных
    for col in integer_columns:
        if col in df_processed.columns:
            # Замена нечисловых значений и преобразование в целые числа
            df_processed[col] = pd.to_numeric(df_processed[col], errors='coerce').fillna(0).astype('int64')
            print(f"Преобразовано {col} в целочисленный тип")

    return df_processed


def save_dataset(df):
    """
    Сохранение DataFrame в CSV формате
    """
    filename = "employee_attrition_processed.csv"
    df.to_csv(filename, index=False)
    print(f"✓ Датaсет сохранен как: {filename}")
    print(f"✓ Колонки: {list(df.columns)}")
    print(f"✓ Строк: {len(df)}")


if __name__ == "__main__":
    main()