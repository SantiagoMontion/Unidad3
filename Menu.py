from ManejadorEmpledo import ManejadorEmpleado
import os
from datetime import date
from ClaseITesorero import ITesorero
from ClaseIGerente import IGerente
class Menu:
    __switcher=None
    __ME=None

    def __init__(self,dim):
        self.__switcher = { 
            1:self.opcion1,
            2:self.opcion2,
            3:self.opcion3,
            4:self.opcion4,
            5:self.opcion5,
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



    def Tesorero(self,lista):
        DNI=input("Ingrese su numero de documento: ")
        lista.gastosSueldoPorEmpleado(DNI)


    def opciones(self,op):
        DNI=input("\nIngrese su numero de documento: ")
        valor=input("\nIngrese el valor a modificar: ")
        if op==1:
            self.__ME.modificarBasicoEPlanta(DNI,valor)

        if op == 2:
            self.__ME.modificarViaticoEExterno(DNI,valor)

        elif op ==3:
            self.__ME.modificarValorEPorHora(DNI,valor)

        
    def Gerente(self,lista):
        op = int(input("1. Modificar Sueldo Basico \n 2. Modificar Viatico \n 3. Modificar Valor de Hora \n 0. Salir \n Ingrese Opcion: " ))
        while op > 0:
            self.opciones(op)
            op = int(input("1. Modificar Báscio \n 2. Modificar Viatico \n 3. Modificar Valor de Hora \n 0. Salir \n Ingrese Otra Opcion: " ))


    def opcion5(self):
        usuario=input("\nIngrese el nombre de usuario: ")
        contra=input("\nIngrese la contraseña: ")

        if usuario == "uTesorero" and contra == "ag@74ck":
            self.Tesorero(ITesorero(self.__ME))

        elif usuario== "uGerente" and contra =="ufC77#!1":
            self.Gerente(IGerente(self.__ME))
        else:
            print("Credenciales incorrectas")

    def test(self):
        print("\n-----TEST----")
        self.__ME.incrementarhoras("43078093",8)
        self.__ME.incrementarhoras("32803761",8)
        self.__ME.Totaltarea("carpinteria")
        self.__ME.ayuda()
        self.__ME.MostrarSueldos()

        