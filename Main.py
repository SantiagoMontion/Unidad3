import os
from Menu import Menu

def test(num,o1,o2,o3,Menu):

    Menu.opcion(o1,num)
    Menu.opcion(o2,num)
    Menu.opcion(o3,num)

if __name__=='__main__':
    Menu=Menu()
    num=int(input("Ingrese un numero de viajero frecuente "))

    while num!=0:
        
        print("\na- Consultar Cantidad de Millas.\n")
        print("b- Acumular Millas.\n")
        print("c- Canjear Millas.\n")
        op=str(input("Seleccione una opcion: ")).lower()
        os.system('cls')
        Menu.opcion(op,num)

        
        num=int(input("\nIngrese otro numero o 0 para finalizar "))

    test(5,'a','b','c',Menu)


   