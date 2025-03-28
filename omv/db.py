from platformdirs import user_data_dir
import sqlite3
import os
import omv.models.tipo_gasto as tipo_gasto
import omv.models.gasto as gasto
import omv.models.ingreso as ingreso
from omv.models.gasto import Gasto
from omv.models.ingreso import Ingreso 
from omv.models.tipo_gasto import Tipo_gasto

APP_NAME = "omv"
DB_NAME = "omv.db"
SCHEMA_PATH = "./scheme.sql"

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
    print("Tipo de gasto insertado exitosamente.")

# Función para insertar un gasto en la base de datos
def add_gasto(db, gasto):
    cursor = db.cursor()
    gasto.id = get_gasto_new_id(db, gasto.fecha)
    query = f'INSERT INTO gasto (fecha, id, monto, descripcion, tipo_gasto_id) VALUES {gasto};'
    cursor.execute(query)
    db.commit()
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
        cursor = db.cursor()
        query = "SELECT nombre, descripcion, id FROM tipo_gasto WHERE id = ?"
        cursor.execute(query, (tipo_gasto_id,))
        tipo_gasto = Tipo_gasto.from_tupla(cursor.fetchone())
        return tipo_gasto
    except sqlite3.Error as e:
        print(f"Error al obtener tipo de gasto: {e}")
        return None

# Función para obtener un tipo de gasto por nombre
def get_tipo_gasto_by_name(db, tipo_gasto_name):
    try:
        cursor = db.cursor()
        query = "SELECT * FROM tipo_gasto WHERE nombre = ?"
        cursor.execute(query, (tipo_gasto_name,))
        tipo_gasto = Tipo_gasto.from_tupla(cursor.fetchone())
        return tipo_gasto
    except sqlite3.Error as e:
        print(f"Error al obtener tipo de gasto: {e}")
    
# Función para obtener un gasto por ID y fecha
def get_gasto_by_id(db, gasto_id, fecha):
    try:
        cursor = db.cursor()
        query = "SELECT fecha, monto, tipo_gasto_id, descripcion, id FROM gasto WHERE id = ? AND fecha = ?"
        cursor.execute(query, (gasto_id, fecha))
        gasto = Gasto.from_tupla(cursor.fetchone())
        gasto.tipo_gasto = get_tipo_gasto_by_id(db, gasto.tipo_gasto)
        return gasto
    except sqlite3.Error as e:
        print(f"Error al obtener gasto: {e}")

def get_ingreso_by_id(db, ingreso_id, fecha):
    try:
        cursor = db.cursor()
        query = "SELECT fecha, monto, descripcion, id FROM ingreso WHERE id = ? AND fecha = ?"
        cursor.execute(query, (ingreso_id, fecha))
        ingreso = Ingreso.from_tupla(cursor.fetchone())
        return ingreso
    except sqlite3.Error as e:
        print(f"Error al obtener ingreso: {e}")

# Función para obtener todos los tipos de gasto
def get_tipos_gasto(db):
    try:
        cursor = db.cursor()
        query = "SELECT nombre, descripcion, id FROM tipo_gasto;"
        cursor.execute(query)
        tipos_gasto = [Tipo_gasto.from_tupla(tupla) for tupla in cursor.fetchall()]
        print("Tipos de gasto obtenidos exitosamente.")
        return tipos_gasto
    except sqlite3.Error as e:
        print(f"Error al obtener tipos de gasto: {e}")
        return None

# funcion gastos del dia
def get_gastos_dia(db, fecha):
    try:
        cursor = db.cursor()
        query = f"SELECT fecha, monto, tipo_gasto_id, descripcion, id FROM gasto WHERE fecha = {fecha};"
        cursor.execute(query)
        gastos = [Gasto.from_tupla(tupla) for tupla in cursor.fetchall()]
        for gasto in gastos:
            gasto.tipo_gasto = get_tipo_gasto_by_id(db, gasto.tipo_gasto)
        print("Gastos obtenidos exitosamente.")
        return gastos
    except sqlite3.Error as e:
        print(f"Error al obtener gastos: {e}")
        return None

# Función para obtener los ingresos del dia
def get_ingresos_dia(db, fecha):
    try:
        cursor = db.cursor()
        query = f"SELECT fecha, monto, descripcion, id FROM ingreso WHERE fecha = {fecha};"
        cursor.execute(query)
        ingresos = [Ingreso.from_tupla(tupla) for tupla in cursor.fetchall()]
        print("Ingresos obtenidos exitosamente.")
        return ingresos
    except sqlite3.Error as e:
        print(f"Error al obtener ingresos: {e}")
        return None
    
def remove_tipo_gasto(db, tipo_gasto_id):
    try:
        cursor = db.cursor()
        query = "DELETE FROM tipo_gasto WHERE id = ?"
        cursor.execute(query, (tipo_gasto_id,))
        db.commit()
    except sqlite3.Error as e:
        print(f"Error al eliminar tipo de gasto: {e}")

def remove_gasto(db, gasto_id, fecha):
    try:
        cursor = db.cursor()
        query = "DELETE FROM gasto WHERE id = ? AND fecha = ?"
        cursor.execute(query, (gasto_id, fecha))
        db.commit()
    except sqlite3.Error as e:
        print(f"Error al eliminar gasto: {e}")

def remove_ingreso(db, ingreso_id, fecha):
    try:
        cursor = db.cursor()
        query = "DELETE FROM ingreso WHERE id = ? AND fecha = ?"
        cursor.execute(query, (ingreso_id, fecha))
        db.commit()
    except sqlite3.Error as e:
        print(f"Error al eliminar ingreso: {e}")

if(__name__ == "__main__"):
    bd = get_db_connection(get_db_path())
    print(get_tipos_gasto(bd))
    print(get_gastos_dia(bd,1))
    print(get_ingresos_dia(bd,1))
    pass    