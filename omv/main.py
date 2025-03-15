import argparse
import comandos
import db

def main():
    # Parser para la funcion principal de la aplicacion (registrar gasto)
    parser = argparse.ArgumentParser(description='Ontamivaro CLI')
    parser.add_argument("-m", "--monto", required=True, help="Nombre de la persona")
    parser.add_argument("-d", "--descripcion", required=False, help="Descripcion del gasto")
    parser.add_argument("-t", "--tipo", required=False, help="Id delipo de gasto")
    parser.add_argument("-f", "--fecha", required=False, help="Id delipo de gasto")
    args = parser.parse_args()
    print(args)
    comandos.agregar_gasto(args)
    # python main.py -m 100 -d "comida" -t 1

    # subparsers = parser.add_subparsers(help='sub-command help')

if __name__ == "__main__":
    main()