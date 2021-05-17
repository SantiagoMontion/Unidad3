from ClaseEmpleado import Empleado
from ClaseFechaHora import FechaHora
class EmpleadoExterno(Empleado):
    # tarea, fecha de inicio, fecha de finalización, monto viático, el costo de la obra y monto del seguro de vida.
    __Tarea=''
    __FechaInicio=None
    __FechaFin=None
    __MontoViatico=0
    __CostoObra=0
    __MontoSeguro=0

    def __init__(self, dni, nom, direc, tel,tarea,fechaI,fechaF,viatico,costo,seguro):
        super().__init__(dni, nom, direc, tel)
        self.__Tarea=tarea
        self.__FechaInicio=fechaI
        self.__FechaFin=fechaF
        self.__MontoViatico=viatico
        self.__CostoObra=costo
        self.__MontoSeguro=seguro

    def getdni(self):
        return super().getdni()

    def gettarea(self):
        return self.__Tarea

    def getfechaI(self):
        return self.__FechaInicio

    def getfechaF(self):
        return self.__FechaFin

    def getviatico(self):
        return self.__MontoViatico

    def getcosto(self):
        return self.__CostoObra

    def getseguro(self):
        return self.__MontoSeguro


    def montoapagar(self):
        suma=int(self.__MontoViatico)+int(self.__MontoSeguro)+int(self.__CostoObra)
        return suma


    def comprobarfecha(self,fecha):
        bandera=False

        sep=self.__FechaFin.split('-')
        f=FechaHora(int(sep[0]),int(sep[1]),int(sep[2]))

        sep2=str(fecha).split('-')
        f2=FechaHora(int(sep2[0]),int(sep2[1]),int(sep2[2]))
        if f>f2:
            bandera=True
        else:
            bandera=False
            
        return bandera


    def getsueldo(self):
        #Sueldo = costo de la obra - viático- monto del seguro de vida
        sueldo= int(self.__CostoObra)-int(self.__MontoViatico)-int(self.__MontoSeguro)
        return sueldo