from ManejadorInscripcion import ManejadorInscripcion
from ManejadorPersona import ManejadorPersona
from ManejadorTallerC import ManejadorTaller
from ClasePersona import Persona
from ClaseInscripcion import Inscripcion
from ClaseTallerCapacitacion import TallerCapacitacion
import os
from datetime import date
class Menu:
    __switcher=None
    __MP=None
    __MT=None
    __MI=None

    def __init__(self):
        self.__switcher = { 
            1:self.opcion1,
            2:self.opcion2,
            3:self.opcion3,
            4:self.opcion4,
            5:self.opcion5,
            0:self.salir
            }
        self.__MP=ManejadorPersona()
        self.__MT=ManejadorTaller()
        self.__MI=ManejadorInscripcion()

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    def salir(self):
        print('Salir')


    def opcion1(self):
        nom=input("\nIngrese su nombre: ")
        dni=input("\nIngrese su dni: ")
        direc=input("\nIngrese su direccion: ")
        P=Persona(nom,dni,direc)
        self.__MP.cargarpersona(P)

        id=int(input("\nIngrese el id del taller: "))
        T=self.__MT.buscartaller(id)
        while T==None:
            id=int(input("\nError, Ingrese nuevamente el id del taller: "))
            T=self.__MT.buscartaller(id)

        I=Inscripcion(date.today(),P,T)

        self.__MI.inscribir(I)


    def opcion2(self):
        dni=input("\nIngrese su dni: ")
        self.__MI.Consultar(dni)
            
        

    def opcion3(self):
        id=int(input("\nIngrese el id del taller: "))
        self.__MI.Listar(id)


    def opcion4(self):
        
        dni=input("\nIngrese su dni: ")
        self.__MI.registrarpago(dni)

    def opcion5(self):
        self.__MI.GuardarArchivo()

    def test(self):
        print("\n-----TEST----")
        


 


    


    