

from ManejadorViajeros import Manejador

class Menu:
    __switcher=None
    __M=None

    def __init__(self):
        self.__switcher = { 
            'a':self.opcion1,
            'b':self.opcion2,
            'c':self.opcion3,
            'd':self.salir
            }
        self.__M=Manejador()
        self.__M.CargarLista()

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op,num):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func(num)

    def salir(self,num):
        print('Salir')

    def opcion1(self,num):
        if type(num)==int:
            print("La Cantidad de Millas es: {}".format(self.__M.ConsultaMillas(num)))

    def opcion2(self,num):
        if type(num)==int:
            millas=int(input("Ingrese La cantidad de millas para acumular "))
            self.__M.Acumular(num,millas)

    def opcion3(self,num):
        if type(num)==int:
            millas=int(input("Ingrese La cantidad de millas para canjear "))
            self.__M.Canjear(num,millas)


    


    