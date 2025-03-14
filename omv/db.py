from platformdirs import user_data_dir
import sqlite3
import os
from models.gasto import Gasto
from models.ingreso import Ingreso 
from models.tipo_gasto import Tipo_gasto

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

# Función para insertar un tipo de gasto en la base de datos
def add_tipo_gasto(db, tipo_gasto):
    cursor = db.cursor()
    query = f'INSERT INTO tipo_gasto (id,nombre,descripcion) VALUES {tipo_gasto};")'
    cursor.execute(query)
    db.commit()
    print(query)
    print("Tipo de gasto insertado exitosamente.")

# Función para insertar un gasto en la base de datos
def add_gasto(db, gasto):
    cursor = db.cursor()
    query = f'INSERT INTO gasto (id,tipo_gasto_id,fecha,monto,descripcion) VALUES {gasto};")'
    cursor.execute(query)
    db.commit()
    print(query)
    print("Gasto insertado exitosamente.")


def add_ingreso(db, ingreso):
    cursor = db.cursor()
    query = f'INSERT INTO ingreso (id,fecha,monto,descripcion) VALUES {ingreso};")'
    cursor.execute(query)
    db.commit()
    print(query)
    print("Ingreso insertado exitosamente.")

if(__name__ == "__main__"):
    print(os.getcwd())