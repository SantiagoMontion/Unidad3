from ClaseMenu import Menu
import os

def opciones():
    print("\n------Menu------\n")
    print("1 -Inscribir una persona en un taller.\n")
    print("2 -Consultar inscripción.\n")
    print("3 -Consultar inscriptos.\n")
    print("4 -Registrar pago\n")
    print("5 -Guardar inscripciones\n")
    op=int(input("\nSeleccione una opcion: "))
    return op
    



if __name__=='__main__':
    M=Menu()

    op=opciones()
    while op !=0:
        M.opcion(op)
        op=opciones()
        os.system("cls")

