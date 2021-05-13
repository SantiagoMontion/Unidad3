from ClaseTallerCapacitacion import TallerCapacitacion
from datetime import date
from ClaseInscripcion import Inscripcion

class Persona:
    __nombre=''
    __dni=''
    __direccion=''
    __Inscripcion=None


    def __init__(self,nom,dni,direc):
        self.__nombre=nom
        self.__dni=dni
        self.__direccion=direc
        self.__Inscripcion=[]


    def getnombre(self):
        return self.__nombre

    def getdni(self):
        return self.__dni

    def getinscripcion(self):
        return self.__Inscripcion



        