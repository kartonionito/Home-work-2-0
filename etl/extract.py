import pandas as pd
import os

FILE_URL = "https://drive.google.com/uc?export=download&id=1J9aRbFxCiK_ueByy8_ius5ymk3vinwgC"
RAW_PATH = os.path.join("data", "raw", "employee_raw.csv")

def extract_and_validate():
    print("🔹 Скачиваем и сохраняем сырые данные из источника...")
    df = pd.read_csv(FILE_URL)
    assert isinstance(df, pd.DataFrame), "Не удалось загрузить DataFrame"
    os.makedirs(os.path.dirname(RAW_PATH), exist_ok=True)
    df.to_csv(RAW_PATH, index=False)
    print(f"✓ Данные загружены и сохранены: {RAW_PATH}")
    return RAW_PATH
