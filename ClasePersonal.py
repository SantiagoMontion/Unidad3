class Personal:
    __cuil=''
    __apellido=''
    __nombre=''
    __sueldobasico=0
    __antiguedad=0


    def __init__(self,cuil,apellido,nombre,sueldobasico,antiguedad,areainv='',tipoinv='',carrera='',cargo='',catedra=''):
        self.__cuil=cuil
        self.__apellido=apellido
        self.__nombre=nombre
        self.__sueldobasico=int(sueldobasico)
        self.__antiguedad=int(antiguedad)


    def getcuil(self):
        return self.__cuil

    def getapellido(self):
        return self.__apellido

    def getnombre(self):
        return self.__nombre

    def getsueldo(self):
        sueldo=self.__sueldobasico+((self.__antiguedad/100)*self.__sueldobasico)
        return sueldo

    def getantiguedad(self):
        return self.__antiguedad
