from ClaseVehiculo import Vehiculo
class Nodo:
    __vehiculo=None
    __sig=None


    def __init__(self,vehiculo): 
        self.__vehiculo=vehiculo
        self.__sig=None


    def setsiguiente(self,sig):
        self.__sig=sig
        
        
    def getsig(self):
        return self.__sig


    def getvehiculo(self):
        return self.__vehiculo
        

