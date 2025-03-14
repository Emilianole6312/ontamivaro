from platformdirs import user_data_dir
import sqlite3
import os

APP_NAME = "omv"
DB_NAME = "omv.db"
SCHEMA_PATH = "../scheme.sql"

# Función para obtener el path de la base de datos
def get_db_path():
    DATA_DIR = user_data_dir(APP_NAME)
    os.makedirs(DATA_DIR, exist_ok=True)
    DB_PATH = os.path.join(DATA_DIR, DB_NAME)
    return DB_PATH

# Función para obtener una conexión a la base de datos
def get_db_connection(DB_PATH):
    db = sqlite3.connect(DB_PATH)
    db.execute("PRAGMA foreign_keys = ON;")  # Activa claves foráneas
    return db

# Función para inicializar la base de datos en caso de que no existan tablas
def init_db(db):
    cursor = db.cursor()
    # Verifica si existen tablas en la base de datos
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' LIMIT 1;")
    table_exists = cursor.fetchone()
    
    if not table_exists:  # Si no existen tablas, ejecuta el esquema SQL
        with open(SCHEMA_PATH, "r") as f:
            db.executescript(f.read())  # Ejecuta el esquema SQL
        db.commit()
        db.close()
        print("Base de datos creada o inicializada exitosamente.")
    else:
        print("La base de datos ya está inicializada.")

if(__name__ == "__main__"):
    print(os.getcwd())
    
    