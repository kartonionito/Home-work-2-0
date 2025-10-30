import os
import pandas as pd
import sqlite3
from sqlalchemy import create_engine

def get_pg_creds_from_sqlite(sqlite_path):
    conn = sqlite3.connect(sqlite_path)
    cur = conn.cursor()
    cur.execute('SELECT url, port, user, pass FROM access LIMIT 1;')
    row = cur.fetchone()
    conn.close()
    url, port, user, password = row
    dbname = "homeworks"
    return url, port, user, password, dbname

def save_to_parquet(df, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_parquet(path, index=False, engine="pyarrow")
    print(f"✓ Data сохранён в Parquet: {path}")

def write_to_pg(df, table_name, creds_db_path):
    url, port, user, password, dbname = get_pg_creds_from_sqlite(creds_db_path)
    conn_str = f'postgresql+psycopg2://{user}:{password}@{url}:{port}/{dbname}'
    engine = create_engine(conn_str)
    df100 = df.head(100)
    df100.to_sql(table_name, engine, schema="public", if_exists="replace", index=False)
    print(f"✓ Загружено {len(df100)} строк в таблицу PostgreSQL: {table_name}")

def load(df, creds_db_path, parquet_path, table_name):
    # Сохранение обработанных данных
    save_to_parquet(df, parquet_path)
    # Выгрузка первых 100 строк в PostgreSQL
    write_to_pg(df, table_name, creds_db_path)
    print("✓ Выгрузка завершена.")
