from platformdirs import user_data_dir
import sqlite3
import os
import models.tipo_gasto as tipo_gasto
import models.gasto as gasto
import models.ingreso as ingreso
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

# Funcion para obtener un id de tipo_gasto no usado
def get_tipo_gasto_new_id(db):
    try:
        cursor = db.cursor()
        query = "SELECT MAX(id) + 1 FROM tipo_gasto;"
        cursor.execute(query)
        tipo_gasto_id = cursor.fetchone()
        return (tipo_gasto_id[0]) if tipo_gasto_id[0] else 0  # Si no hay registros, retorna 1
    except sqlite3.Error as e:
        print(f"Error al obtener el nuevo id: {e}")
        return None

# Funcion para obtener un id de gasto no usado
def get_gasto_new_id(db, fecha):
    try:
        cursor = db.cursor()
        query = f"SELECT MAX(id) + 1 FROM gasto WHERE fecha = {fecha};"
        cursor.execute(query)
        gasto_id = cursor.fetchone()
        print(gasto_id)
        return (gasto_id[0]) if gasto_id[0] else 0  # Si no hay registros, retorna 1
    except sqlite3.Error as e:
        print(e)

# Funcion para obtener un id de ingreso no usado
def get_ingreso_new_id(db, fecha):
    try:
        cursor = db.cursor()
        query = "SELECT MAX(id) + 1 FROM ingreso;"
        cursor.execute(query)
        ingreso_id = cursor.fetchone()
        return (ingreso_id[0]) if ingreso_id[0] else 0  # Si no hay registros, retorna 1
    except sqlite3.Error as e:
        print(f"Error al obtener el nuevo id: {e}")
        return None

# Función para insertar un tipo de gasto en la base de datos
def add_tipo_gasto(db, tipo_gasto):
    cursor = db.cursor()
    tipo_gasto.id = get_tipo_gasto_new_id(db)
    query = f'INSERT INTO tipo_gasto (id, nombre, descripcion) VALUES {tipo_gasto};'
    cursor.execute(query)
    db.commit()
    print(query)
    print("Tipo de gasto insertado exitosamente.")

# Función para insertar un gasto en la base de datos
def add_gasto(db, gasto):
    cursor = db.cursor()
    gasto.id = get_gasto_new_id(db, gasto.fecha)
    # print(gasto.id)
    query = f'INSERT INTO gasto (fecha, id, monto, descripcion, tipo_gasto_id) VALUES {gasto};'
    print(query)
    cursor.execute(query)
    db.commit()
    print(query)
    print("Gasto insertado exitosamente.")

# Función para insertar un ingreso en la base de datos
def add_ingreso(db, ingreso):
    cursor = db.cursor()
    ingreso.id = get_ingreso_new_id(db, ingreso.fecha)
    query = f'INSERT INTO ingreso (id, fecha, monto, descripcion) VALUES {ingreso};'
    cursor.execute(query)
    db.commit()
    print("Ingreso insertado exitosamente.")

# Función para obtener un tipo de gasto por ID
def get_tipo_gasto_by_id(db, tipo_gasto_id):
    try:
        with db.cursor() as cursor:
            query = "SELECT * FROM tipo_gasto WHERE id = ?"
            cursor.execute(query, (tipo_gasto_id,))
            tipo_gasto = Tipo_gasto.from_tupla(cursor.fetchone())
            print(query.replace("?", str(tipo_gasto_id)))
            if tipo_gasto:
                print("Tipo de gasto obtenido exitosamente.")
            else:
                print("No se encontró el tipo de gasto con ese ID.")
            return tipo_gasto
    except sqlite3.Error as e:
        print(f"Error al obtener tipo de gasto: {e}")
        return None

# Función para obtener un tipo de gasto por nombre
def get_tipo_gasto_by_name(db, tipo_gasto_name):
    try:
        with db.cursor() as cursor:
            query = "SELECT * FROM tipo_gasto WHERE nombre = ?"
            cursor.execute(query, (tipo_gasto_name,))
            tipo_gasto = Tipo_gasto.from_tupla(cursor.fetchone())
            print(query.replace("?", tipo_gasto_name))
            if tipo_gasto:
                print("Tipo de gasto obtenido exitosamente.")
            else:
                print("No se encontró el tipo de gasto con ese nombre.")
            return tipo_gasto
    except sqlite3.Error as e:
        print(f"Error al obtener tipo de gasto: {e}")

if(__name__ == "__main__"):
    print(os.getcwd())
    db = get_db_connection(get_db_path())