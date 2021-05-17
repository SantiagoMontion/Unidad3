from ClaseEmpleado import Empleado
class EmpleadoDePlanta(Empleado):
    #sueldo básico y antigüedad.
    __sueldobasico=0
    __antiguedad=0

    def __init__(self, dni, nom, direc, tel,sueldo,antig):
        super().__init__(dni, nom, direc, tel)
        self.__sueldobasico=sueldo
        self.__antiguedad=antig

    def getnombre(self):
        return super().getnombre()

    def getdireccion(self):
        return super().getdireccion()

    def gettelefono(self):
        return super().gettelefono()

    def getdni(self):
        return super().getdni()

    def getsueldobasico(self):
        return int(self.__sueldobasico)

    def getsueldo(self):
        #Sueldo = sueldo básico+ 1% del sueldo básico*antigüedad
        sueldo=int(self.__sueldobasico)+ (1 /100 )*(int(self.__sueldobasico))*int(self.__antiguedad)
        return sueldo

    def getantiguedad(self):
        return self.__antiguedad


