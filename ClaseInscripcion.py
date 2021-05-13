

from datetime import date
class Inscripcion:
    __fechainscripcion= date
    __pago=bool
    __Persona=None
    __TallerCapacitacion=None


    def __init__(self,fecha,persona,taller,pago=False):
        if type(fecha)==date and type(pago)==bool:
            self.__fechainscripcion=fecha
            self.__pago=pago
            self.__Persona=persona
            self.__TallerCapacitacion=taller

    def getfecha(self):
        return self.__fechainscripcion
    
    def getpersona(self):
        return self.__Persona


    def gettaller(self):
        return self.__TallerCapacitacion

    def getpago(self):
        return self.__pago

    def pagar(self):
        self.__pago=True


