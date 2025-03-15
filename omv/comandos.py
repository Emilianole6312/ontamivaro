import db 
from models.gasto import Gasto
from models.ingreso import Ingreso 
from models.tipo_gasto import Tipo_gasto
from datetime import datetime

bd = db.get_db_connection(db.get_db_path())

def agregar_tipo_gasto(args):
    # crea el tipo de gasto
    tipo_gasto = Tipo_gasto(args.nombre, args.descripcion)
    
    # inserta el tipo de gasto en la base de datos
    db.add_tipo_gasto(bd, tipo_gasto)

def agregar_gasto(args):
    # obtiene el tipo de gasto por id
    tipo_gasto = db.get_tipo_gasto_by_id(bd, args.tipo)

    # en caso de no incluir fecha, esta se obtiene de la fecha actual
    fecha = (args.fecha) if args.fecha else datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    fecha = int(fecha.timestamp())

    # crea el gasto
    gasto = Gasto(fecha, args.monto, tipo_gasto, args.descripcion)

    # inserta el gasto en la base de datos
    db.add_gasto(bd, gasto)

def agregar_ingreso(args):
    # en caso de no incluir fecha, esta se obtiene de la fecha actual
    fecha = (args.fecha) if args.fecha else datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    fecha = int(fecha.timestamp())

    # crea el ingreso
    ingreso = Ingreso(fecha, args.monto)
    # inserta el ingreso en la base de datos
    db.add_ingreso(bd, ingreso)