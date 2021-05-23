from ClaseVehiculo import Vehiculo
from datetime import datetime
class VehiculoUsado(Vehiculo):
    __marca=''
    __patente=''
    __anio=0
    __km=0


    def __init__(self, modelo, cantp, color, preciobase,marca,patente,anio,km):
        super().__init__(modelo, cantp, color, preciobase)
        self.__marca=marca
        self.__patente=patente
        self.__anio=anio
        self.__km=km



    def getmarca(self):
        return self.__marca

    def getpatente(self):
        return self.__patente


    def getanio(self):
        return self.__anio

    def getkm(self):
        return self.__km

    def ImporteDeVenta(self):
        anio=int(datetime.today().year)
        
        anios=anio-self.__anio

        importe=int(super().getprecio()) - ((1/100)*anios*int(super().getprecio()))

        if self.__km>100000:
            importe=int(super().getprecio()) - ((2/100)*anios*int(super().getprecio()))


        return importe



    def toJSON(self):
        d=dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                            modelo=self.getmodelo(),
                            preciobase = self.getprecio(),
                            color= self.getcolor(),
                            cantp= self.getcantp(),
                            marca= self.__marca,
                            km= self.__km,
                            anio= self.__anio,
                            patente= self.__patente
                            )
                
        )
        return d







