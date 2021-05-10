from ManejadorHelado import ManejadorHelado
from ManejadorSabor import ManejadorSabor
import os
class Menu:
    __switcher=None
    __MH=None
    __MS=None

    def __init__(self):
        self.__switcher = { 
            1:self.opcion1,
            2:self.opcion2,
            3:self.opcion3,
            4:self.opcion4,
            0:self.salir
            }
        self.__MH=ManejadorHelado()
        self.__MS=ManejadorSabor()
        self.__MS.CargarSabores()

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    def salir(self):
        print('Salir')


    def opcion1(self):
        sabores=[]
        cont=0
        gramos=int(input("\nIngrese los gramos: (100, 150, 250, 500 y 1000): "))
        s=1
        while s!=0 and cont<4:
            os.system("cls")

            print("\nListado sabores:")
            self.__MS.Muestra()
            s=int(input("\nSeleccione otro numero de sabor: (0 para terminar)"))
            if s!=0:
                sabores.append(self.__MS.retornasabor(s-1))
            cont+=1
            
        os.system("cls")
        
        self.__MH.RegistrarHelado(gramos,sabores)


    def opcion2(self):
        # Mostrar el nombre de los 5 sabores de helado más pedidos.
        os.system("cls")
        self.__MH.Maspedidos()
        

    def opcion3(self):
        print("\nListado sabores:")
        self.__MS.Muestra()
        num=int(input("Ingrese un numero de sabor: "))
        sabor=self.__MS.retornasabor(num-1)

        self.__MH.Estimargramos(sabor)

    def opcion4(self):
        tipo=int(input("Ingrese un tipo de helado (100, 150, 250, 500 y 1000) numero entero: "))
        self.__MH.SaboresvendidosxTam(tipo)

    def test(self):
        print("\n-----TEST----")
        sabores=[]
        for i in range(4):
            sabores.append(self.__MS.retornasabor(i))
        self.__MH.RegistrarHelado(1000,sabores)
        self.__MH.Maspedidos()
        sabor=self.__MS.retornasabor(1)
        self.__MH.Estimargramos(sabor)


 


    


    