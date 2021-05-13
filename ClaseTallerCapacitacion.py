
class TallerCapacitacion:
    __idtaller=0
    __nombre=''
    __vacantes=0
    __montoinscripcion=0
    __Inscripcion=None


    def __init__(self,id,nom,vac,monto):
        self.__idtaller=id
        self.__nombre=nom
        self.__vacantes=vac
        self.__montoinscripcion=monto
        self.__Inscripcion=[]



    def getid(self):
        return int(self.__idtaller)

    def getnombretaller(self):
        return self.__nombre

    def getvacantes(self):
        return self.__vacantes

    def getmontoinsc(self):
        return self.__montoinscripcion

    def getinscripcion(self):
        return self.__Inscripcion

    def modificarcantidad(self):
        
        self.__vacantes=int(self.__vacantes)-1