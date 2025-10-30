# Home-work-2-0
# 🏢 Employee Attrition EDA & ETL Pipeline
Комплексный проект по анализу, визуализации и интеграции данных об увольнениях сотрудников (attrition). Курс Data Science.

# 📚 Описание проекта
Этот репозиторий содержит полный цикл работы с корпоративными HR-данными:

Загрузка и подготовка "сырых" данных

Разведочный анализ (EDA) с интерактивными визуализациями

Сохранение и запись в реляционные базы данных

ETL-пакет с удобным CLI для автоматизации обработки

# 🚀 Быстрый старт
```bash
Клонируйте репозиторий
git clone https://github.com/kartonionito/Home-work-2-0.git
cd Home-work-2-0

Создайте виртуальное окружение и установите зависимости
python -m venv .venv
source .venv/bin/activate      # на Mac/Linux
.\.venv\Scripts\Activate.ps1   # на Windows

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

Запустите ETL-процесс (вся обработка одной командой)
python -m etl.main --creds-db creds.db --table gavriliev
--creds-db — путь к SQLite-файлу с учеткой для PostgreSQL
--table — название вашей таблицы (фамилия латиницей)
```
# 🏗️ Структура проекта
```Home-work-2-0/
├── etl/
│   ├── __init__.py
│   ├── extract.py         # Получение и валидация исходных данных, сохранение .csv в data/raw
│   ├── transform.py       # Преобразование типов, очистка
│   ├── load.py            # Сохранение в .parquet и в PostgreSQL (до 100 строк!)
│   ├── validate.py        # (опционально) — проверки данных
│   └── main.py            # CLI для запуска всего процесса
├── notebooks/
│   └── EDA.ipynb          # Подробный EDA-ноутбук с визуализациями
├── data/                  # Сырые и обработанные данные (исключить через .gitignore!)
│   ├── raw/
│   └── processed/
├── requirements.txt
├── README.md
├── creds.db
└── ...
```

# 📊 Визуализация и EDA
Plotly Express:
Интерактивные scatter-графики (возраст, доход, пол, стаж, статус увольнения)
Стиль plotly_dark, всплывающие подсказки, zoom

Seaborn:
Сеточные визуализации: гистограммы, boxplot, violinplot, countplot
Все графики выполнены в едином стиле: фон, палитра, размер шрифта

Пример EDA-графика (Plotly):

```python
import plotly.express as px
fig = px.scatter(df, x="Age", y="MonthlyIncome", color="Attrition", template="plotly_dark")
fig.show()
```
Пример сетки с Seaborn:

```python
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="darkgrid")
fig, axes = plt.subplots(2, 2)
sns.histplot(df["Age"], ax=axes[0,0])
... другие графики ...
plt.tight_layout()
plt.show()
```
В ноутбуке к каждому блоку добавлены пояснения и выводы.

# 🌐 Работа с базами данных
SQLite (creds.db) — хранит учетные данные для подключения к PostgreSQL

PostgreSQL — хранит итоговые таблицы с вашими данными (таблица с вашей фамилией)

# 🛠️ ETL Pipeline: обработка и загрузка
extract.py — скачивает исходные данные, валидирует, сохраняет .csv

transform.py — приводит типы, очищает и стандартизирует данные

load.py — сохраняет данные в parquet и выгружает 100 строк в PostgreSQL

validate.py — (опционально) дополнительные проверки данных

main.py — общий интерфейс запуска

Запуск всего процесса:

bash
python -m etl.main --creds-db creds.db --table gavriliev
# 📑 Ссылки
#### Исходный датасет:
(https://drive.google.com/file/d/1J9aRbFxCiK_ueByy8_ius5ymk3vinwgC/view?usp=drive_link)

#### Пример результата:
(https://drive.google.com/file/d/1HL4RvKognD_6_3-cL4UMC2poBAUIurXH/view?usp=drive_link)

#### EDA-наблюдение (nbviewer):
(https://nbviewer.org/github/kartonionito/Home-work-2-0/blob/main/notebooks/EDA.ipynb)

# ⚙️ Детали реализации
Все зависимости указаны в requirements.txt

Каталог data/ исключён из git для безопасности

Готово к работе с Python 3.9+

Для визуализации используются Plotly Express >= 5, Seaborn >= 0.12

# 📈 Логика ETL
Extract: загружает данные, хранит .csv в data/raw

Transform: чистит и приводит к нужным типам

Load: сохраняет parquet, записывает 100 строк в PostgreSQL

main.py: запуск всего процесса одной командой

# 📝 Контакты и поддержка
По вопросам или предложениям:

Открывайте Issue

Пишите на: game-kollfee@mail.ru
