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

    except Exception as e:
        print(f"Ошибка: {e}")
        print("Проверьте доступность файла и интернет-соединение")


if __name__ == "__main__":
    main()