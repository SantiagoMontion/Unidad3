from Menu import Menu
import os

def opciones():
    print("----Menu----")
    print("\n1- Registrar un helado.")
    print("\n2- Mostrar sabores mas vendidos.")
    print("\n3- Total de gramos vendidos.")
    print("\n4- Sabores vendidos segun tamaño.")
    print("\n0- Salir")

    op=int(input("\nSeleccione una opcion: "))

    return op


if __name__ == '__main__':
    M=Menu()

    op=opciones()
    while op>0:
        M.opcion(op)
        op=opciones()
        os.system("cls")


    M.test()
