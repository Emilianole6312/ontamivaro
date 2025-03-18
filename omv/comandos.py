from omv import db
from omv.models.gasto import Gasto
from omv.models.ingreso import Ingreso 
from omv.models.tipo_gasto import Tipo_gasto
from datetime import datetime

bd = db.get_db_connection(db.get_db_path())

def inicializar_bd(args):
    db.init_db(bd)

def agregar_tipo_gasto(args):
    # crea el tipo de gasto
    tipo_gasto = Tipo_gasto(args.nombre, args.descripcion)
    
    # inserta el tipo de gasto en la base de datos
    db.add_tipo_gasto(bd, tipo_gasto)

def agregar_gasto(args):
    # obtiene el tipo de gasto por id
    tipo_gasto = db.get_tipo_gasto_by_id(bd, args.tipo)
    # en caso de no incluir fecha, esta se obtiene de la fecha actual
    if args.fecha:
        try:
            fecha = datetime.strptime(args.fecha, '%Y-%m-%d').replace(hour=0, minute=0, second=0, microsecond=0)
        except ValueError:
            print("Formato de fecha incorrecto. Debe ser YYYY-MM-DD")
            return
    else:
        fecha = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    fecha = int(fecha.timestamp())

    # crea el gasto
    gasto = Gasto(fecha, args.monto, tipo_gasto, args.descripcion)

    # inserta el gasto en la base de datos
    db.add_gasto(bd, gasto)

def agregar_ingreso(args):
    # en caso de no incluir fecha, esta se obtiene de la fecha actual
    if args.fecha:
        try:
            fecha = datetime.strptime(args.fecha, '%Y-%m-%d').replace(hour=0, minute=0, second=0, microsecond=0)
        except ValueError:
            print("Formato de fecha incorrecto. Debe ser YYYY-MM-DD")
            return
    else:
        fecha = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    fecha = int(fecha.timestamp())

    # crea el ingreso
    ingreso = Ingreso(fecha, args.monto)
    # inserta el ingreso en la base de datos
    db.add_ingreso(bd, ingreso)

def ver_tipo_gasto(args):
    # obtiene el tipo de gasto por id
    tipos_gasto = db.get_tipos_gasto(bd)
    print("ID Nombre               Descripción")
    for tipo in tipos_gasto:
        print(f'{tipo.id:<2} {tipo.nombre:<20} {tipo.descripcion}')
    pass

def ver_gastos(args):
    # obtiene la fecha en timestamp
    if args.fecha:
        try:
            fecha = datetime.strptime(args.fecha, '%Y-%m-%d').replace(hour=0, minute=0, second=0, microsecond=0)
        except ValueError:
            print("Formato de fecha incorrecto. Debe ser YYYY-MM-DD")
            return
    else:
        fecha = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    fecha = int(fecha.timestamp())
    
    # obtiene los gastos y los imprime
    gastos = db.get_gastos_dia(bd, fecha)
    for gasto in gastos:
        gasto.fecha = datetime.fromtimestamp(gasto.fecha).strftime('%Y-%m-%d')
    print("ID Fecha      Monto  Descripción")
    for gasto in gastos:
        print(f'{gasto.id:<2} {gasto.fecha} {gasto.monto:<6} {gasto.descripcion}')
    pass

def ver_ingresos(args):
    # obtiene la fecha en timestamp
    if args.fecha:
        try:
            fecha = datetime.strptime(args.fecha, '%Y-%m-%d').replace(hour=0, minute=0, second=0, microsecond=0)
        except ValueError:
            print("Formato de fecha incorrecto. Debe ser YYYY-MM-DD")
            return
    else:
        fecha = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    fecha = int(fecha.timestamp())

    # obtiene los ingresos y los imprime
    ingresos = db.get_ingresos_dia(bd, fecha)
    for ingreso in ingresos:
        ingreso.fecha = datetime.fromtimestamp(ingreso.fecha).strftime('%Y-%m-%d')
    print("ID Fecha      Monto")
    for ingreso in ingresos:
        print(f'{ingreso.id:<2} {ingreso.fecha} {ingreso.monto}')
    pass

# Elimina un tipo de gasto
def eliminar_tipo_gasto(args):
    # obtiene el tipo de gasto por id
    tipo_gasto = db.get_tipo_gasto_by_id(bd, args.id)
    if tipo_gasto:
        db.remove_tipo_gasto(bd, tipo_gasto.id)
        print("Tipo de gasto eliminado exitosamente.")
    else:
        print("No se encontró el tipo de gasto con el ID especificado.")

    # Elimina un gasto
def eliminar_gasto(args):
    # obtiene la fecha en timestamp
    if args.fecha:
        try:
            fecha = datetime.strptime(args.fecha, '%Y-%m-%d').replace(hour=0, minute=0, second=0, microsecond=0)
        except ValueError:
            print("Formato de fecha incorrecto. Debe ser YYYY-MM-DD")
            return
    else:
        fecha = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    fecha = int(fecha.timestamp())

    # obtiene el gasto por id
    gasto = db.get_gasto_by_id(bd, args.id, fecha)
    if gasto:
        db.remove_gasto(bd, args.id, fecha)
        print("Gasto eliminado exitosamente.")
    else:
        print("No se encontró el gasto con el ID especificado.")

# Elimina un ingreso
def eliminar_ingreso(args):
    # obtiene la fecha en timestamp
    if args.fecha:
        try:
            fecha = datetime.strptime(args.fecha, '%Y-%m-%d').replace(hour=0, minute=0, second=0, microsecond=0)
        except ValueError:
            print("Formato de fecha incorrecto. Debe ser YYYY-MM-DD")
            return
    else:
        fecha = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    fecha = int(fecha.timestamp())

    # obtiene el ingreso por id
    ingreso = db.get_ingreso_by_id(bd, args.id, fecha)
    if ingreso:
        db.remove_ingreso(bd, args.id, fecha)
        print("Ingreso eliminado exitosamente.")
    else:
        print("No se encontró el ingreso con el ID especificado.")

if (__name__ == '__main__'):
    ver_tipo_gasto(None)    
    ver_gastos(None)
    ver_ingresos(None)
    pass