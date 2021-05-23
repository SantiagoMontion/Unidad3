from ClaseLista import Lista
from ClaseObjectEncoder import ObjectEncoder
from ClaseVehiculoNuevo import VehiculoNuevo
from ClaseVehiculoUsado import VehiculoUsado
import os

class Menu:
    __switcher=None
    __Encoder=None

    def __init__(self):
        self.__switcher = { 
            1:self.opcion1,
            2:self.opcion2,
            3:self.opcion3,
            4:self.opcion4,
            5:self.opcion5,
            6:self.opcion6,
            7:self.opcion7,
            0:self.salir
            }
        self.__Encoder=ObjectEncoder()

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op,lista):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func(lista)

    def CargarVehiculo(self):
        tipo=input("\nIngrese el tipo de vehiculo (N: nuevo , U: usado): ").lower()

        mod=input("\nIngrese el modelo del vehiculo: ")
        cantp=int(input("\nIngrese la cantidad de puertas: "))
        color=input("\nIngrese el color del vehiculo: ")
        precio=int(input("\nIngrese el precio del vehiculo: "))

        if tipo=="n":
            version=input("\nIngrese la version del vehiculo (full , base): ").lower()
            vehiculo=VehiculoNuevo(mod,cantp,color,precio,version)

        elif tipo =="u":
            marca=input("\nIngrese la marca: ")
            patente=input("\nIngrese la patente: ")
            anio=int(input("\nIngrese el año: "))
            km=int(input("\nIngrese los kilometros: "))
            vehiculo=VehiculoUsado(mod,cantp,color,precio,marca,patente,anio,km)

        return vehiculo


    def salir(self,lista):
        print('Salir')


    def opcion1(self,lista):
        pos=int(input("\nIngrese la posicion: "))
        vehiculo=self.CargarVehiculo()
        lista.instertarvehiculo(vehiculo,pos-1)




    def opcion2(self,lista):
        vehiculo=self.CargarVehiculo()
        lista.agregarvehiculo(vehiculo)
        
        

    def opcion3(self,lista):
        pos=int(input("\nIngrese la posicion: "))
        lista.mostrarporpos(pos-1)

    def opcion4(self,lista):
        patente=input("\nIngrese la patente a mostrar: ")
        lista.modificarpreciobase(patente)
        

    def opcion5(self,lista):
        lista.maseconomico()

    def opcion6(self,lista):
        lista.Mostrar()

    def opcion7(self,lista):
        self.__Encoder.GuardarArchivo(lista.toJSON(),"vehiculos.json")

    def test(self,lista):
        print("\n-----TEST----")
        vehiculo=VehiculoUsado("C3",4,"rojo",2500,"Citroen","aaab",2018,20000)
        lista.instertarvehiculo(vehiculo,1)
        lista.mostrarporpos(1)
        lista.modificarpreciobase("aaab")
        lista.maseconomico()
        lista.Mostrar()
        self.opcion7(lista)




        