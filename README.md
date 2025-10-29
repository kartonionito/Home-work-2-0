# Home-work-2-0
Ссылка на dataset - https://drive.google.com/drive/folders/1ZqEjlc6ZzwO_qOo8KXJLXcbCtexi2UGJ?usp=drive_link
Ссылка на скрин - https://drive.google.com/file/d/1HL4RvKognD_6_3-cL4UMC2poBAUIurXH/view?usp=sharing

Установка и запуск
Клонируйте репозиторий:

bash
git clone https://github.com/kartonionito/Home-work-2-0.git
cd Home-work-2-0
Создайте и активируйте виртуальное окружение

macOS / Linux:

bash
python3 -m venv .venv
source .venv/bin/activate
Windows:

powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
# Если активация заблокирована политикой:
# Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
Установите зависимости:

bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
Запустите обработку данных:

bash
python data_loader.py
Альтернатива: conda
bash
conda create -n hw2env python=3.11 -y
conda activate hw2env
pip install -r requirements.txt
python data_loader.py
Результат выполнения:
В проекте появится обработанный датасет employee_attrition_processed.csv.
Количество строк и колонок, а также фрагменты таблицы выведутся в консоли; пример результата есть по ссылке на скриншот.
