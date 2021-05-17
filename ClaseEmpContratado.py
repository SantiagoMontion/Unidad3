from ClaseEmpleado import Empleado

class EmpleadoContratado(Empleado):
    #fecha de inicio y de finalización de contrato, 
    # cantidad de horas trabajadas y valor por hora (es el mismo para todos los empleados contratados)
    __FechaInicio=None
    __FechaFin=None
    __CantHoras=0
    valorhora=240

    def __init__(self, dni, nom, direc, tel,fechaI,fechaF,canth):
        super().__init__(dni, nom, direc, tel)
        self.__FechaInicio=fechaI
        self.__FechaFin=fechaF
        self.__CantHoras=int(canth)

    def getdni(self):
        return super().getdni()

    def getfechaI(self):
        return self.__FechaInicio

    def getfechaF(self):
        return self.__FechaFin

    def getcanths(self):
        return self.__CantHoras

    def acumularhoras(self,cant):
        self.__CantHoras+=cant
        print("\nHoras acumuladas con exito!")


    def getsueldo(self):
        sueldo=self.__CantHoras*self.getValorporhora()
        #Sueldo = cantidad de horas trabajadas * valor de la hora
        return sueldo

    @classmethod
    def getValorporhora(cls):
        return int(cls.valorhora)

