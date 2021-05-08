
class ViajeroFrecuente:
    __NumViajero=0
    __DNI=''
    __Nombre=''
    __Apellido=''
    __MillasAcum=0


    def __init__(self,num,dni,nombre,apellido,millas):
        self.__NumViajero=num
        self.__DNI=dni
        self.__Nombre=nombre
        self.__Apellido=apellido
        self.__MillasAcum=int(millas)

    def CantMillasAcum(self):
        return self.__MillasAcum

    def AcumularMillas(self,millas):
        self.__MillasAcum+=int(millas)
        print("Millas Acumuladas Exitosamente!\n")

    def CanjearMillas(self,millas):
        if millas<=self.__MillasAcum:
            self.__MillasAcum-=int(millas)
            print("Millas Canjeadas Exitosamente!\n")
        else:
            print("Error en la operacion, no dispone de tantas millas acumuladas")
