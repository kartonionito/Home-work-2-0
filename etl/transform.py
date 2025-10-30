import pandas as pd

def convert_data_types(df: pd.DataFrame) -> pd.DataFrame:
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
        if col in df.columns:
            df[col] = df[col].astype("category")
    for col in integer_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0).astype("int64")
    return df

def transform(raw_csv_path):
    print(f"🔹 Чтение и приведение типов данных из {raw_csv_path}...")
    df = pd.read_csv(raw_csv_path)
    df = convert_data_types(df)
    print("✓ Типы данных успешно приведены.")
    return df
