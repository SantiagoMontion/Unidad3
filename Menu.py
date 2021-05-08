

from ManejadorLibro import ManejadorLibro

class Menu:
    __switcher=None
    __M=None

    def __init__(self):
        self.__switcher = { 
            1:self.opcion1,
            2:self.opcion2,
            0:self.salir
            }
        self.__M=ManejadorLibro()
        self.__M.CargarLibros()

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    def salir(self):
        print('Salir')

    def opcion1(self):
        id=int(input("\nIngrese el id del libro: "))
        self.__M.Muestraporid(id)

    def opcion2(self):
        palabra=input("Ingrese una palabra a buscar: ")
        self.__M.BuscarPalabra(palabra)

    def test(self):
        print("\n-----TEST----")
        self.__M.Muestraporid(10004)
        self.__M.Muestraporid(10002)
        self.__M.BuscarPalabra("Objects")


 


    


    