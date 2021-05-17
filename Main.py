from Menu import Menu
import os

def opciones():
    print("\n-----Menu-----\n")
    print("\n1- Registrar horas.")
    print("\n2- Total de tarea.")
    print("\n3- Ayuda.")
    print("\n4- Calcular sueldo.")
    op=int(input("\nSeleccione una opcion: "))
    return op




if __name__=='__main__':
    
    dim=int(input("\nIngrese la Cantidad Total de empleados: "))
    os.system("cls")
    M=Menu(dim)
    op=opciones()

    while op>0 and op<=4:
        M.opcion(op)
        op=opciones()
        os.system("cls")


    M.test()
