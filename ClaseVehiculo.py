
class Vehiculo:
    __modelo=''
    __cantp=0
    __color=''
    __preciobase=0

    def __init__(self,modelo,cantp,color,preciobase):
        self.__modelo=modelo
        self.__cantp=cantp
        self.__color=color
        self.__preciobase=preciobase



    def getmodelo(self):
        return self.__modelo

    def modificarpreciobase(self,nuevo):
        self.__preciobase=nuevo

    def getcantp(self):
        return self.__cantp

    def getcolor(self):
        return self.__color

    def getprecio(self):
        return self.__preciobase

    def toJSON(self):
        d=dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                            modelo=self.getmodelo(),
                            preciobase=self.getprecio(),
                            color=self.getcolor(),
                            cantp=self.getcantp(), 
                            )
            )
        return d


    def __str__(self):
        return "-Modelo: {} \n-Precio Base: {} \n-Color: {} \n-Puertas: {}".format(self.__modelo, self.__preciobase, self.__color, self.__cantp)
        



    