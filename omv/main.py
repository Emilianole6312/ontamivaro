import argparse
import comandos
import db

def main():
    # Parser para la función principal de la aplicación
    parser = argparse.ArgumentParser(description='Ontamivaro CLI')
    subparsers = parser.add_subparsers(help='Subcomandos disponibles', dest='subcomando')

    # Subcomando para registrar un gasto
    parser_registrar_gasto = subparsers.add_parser('gasto', help='Registrar un gasto')
    parser_registrar_gasto.add_argument("-m", "--monto", required=True, help="Monto del gasto")
    parser_registrar_gasto.add_argument("-d", "--descripcion", required=False, help="Descripción del gasto")
    parser_registrar_gasto.add_argument("-t", "--tipo", required=False, help="ID del tipo de gasto")
    parser_registrar_gasto.add_argument("-f", "--fecha", required=False, help="Fecha del gasto")
    parser_registrar_gasto.set_defaults(func=comandos.agregar_gasto)

    # Subcomando para agregar un tipo de gasto
    parser_agregar_tipo_gasto = subparsers.add_parser('tipo_gasto', help='Agregar un tipo de gasto')
    parser_agregar_tipo_gasto.add_argument("-n", "--nombre", required=True, help="Nombre del tipo de gasto")
    parser_agregar_tipo_gasto.add_argument("-d", "--descripcion", required=False, help="Descripción del tipo de gasto")
    parser_agregar_tipo_gasto.set_defaults(func=comandos.agregar_tipo_gasto)

    # Subcomando para agregar un ingreso
    parser_agregar_ingreso = subparsers.add_parser('ingreso', help='Agregar un ingreso')
    parser_agregar_ingreso.add_argument("-m", "--monto", required=True, help="Monto del ingreso")
    parser_agregar_ingreso.add_argument("-f", "--fecha", required=False, help="Fecha del ingreso")
    parser_agregar_ingreso.set_defaults(func=comandos.agregar_ingreso)
    
    # Subcomando para ver los tipos de gasto
    parser_ver_tipo_gasto = subparsers.add_parser('ver_tipos_gasto', help='Ver los tipos de gasto')
    parser_ver_tipo_gasto.set_defaults(func=comandos.ver_tipo_gasto)

    # Subcomando para ver los gastos
    parser_ver_gastos = subparsers.add_parser('ver_gastos', help='Ver los gastos')
    parser_ver_gastos.add_argument("-f", "--fecha", required=False, help="Fecha de los gastos") 
    parser_ver_gastos.set_defaults(func=comandos.ver_gastos)

    # Subcomando para ver los ingresos
    parser_ver_ingresos = subparsers.add_parser('ver_ingresos', help='Ver los ingresos')
    parser_ver_ingresos.add_argument("-f", "--fecha", required=False, help="Fecha de los ingresos")
    parser_ver_ingresos.set_defaults(func=comandos.ver_ingresos)

    # Parseo de argumentos
    args = parser.parse_args()

    # Verifica si se especificó un subcomando
    if hasattr(args, 'func'):
        args.func(args)  # Llama a la función asociada al subcomando
    else:
        parser.print_help()  # Muestra la ayuda si no se especificó un subcomando


if __name__ == "__main__":
    main()