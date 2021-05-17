from ManejadorEmpledo import ManejadorEmpleado
import os
from datetime import date
class Menu:
    __switcher=None
    __ME=None

    def __init__(self,dim):
        self.__switcher = { 
            1:self.opcion1,
            2:self.opcion2,
            3:self.opcion3,
            4:self.opcion4,
            0:self.salir
            }
        self.__ME=ManejadorEmpleado(dim)
        self.__ME.LeerEmpleadosdeplanta()
        self.__ME.LeerEmpleadosContratado()
        self.__ME.LeerEmpleadosExterno()        

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    def salir(self):
        print('Salir')


    def opcion1(self):
        dni=input("\nIngresar DNI: ")
        cant=int(input("\nIngresar la cantidad de horas trabajadas hoy: "))
        self.__ME.incrementarhoras(dni,cant)


    def opcion2(self):
        tarea=input("\nIngrese una tarea: (carpinteria, electricidad, plomeria) ").lower()
        self.__ME.Totaltarea(tarea)

            
        

    def opcion3(self):
        self.__ME.ayuda()

    def opcion4(self):
        self.__ME.MostrarSueldos()

    def test(self):
        print("\n-----TEST----")
        self.__ME.incrementarhoras("43078093",8)
        self.__ME.incrementarhoras("32803761",8)
        self.__ME.Totaltarea("carpinteria")
        self.__ME.ayuda()
        self.__ME.MostrarSueldos()

        