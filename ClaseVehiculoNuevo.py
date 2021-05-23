from ClaseVehiculo import Vehiculo

class VehiculoNuevo(Vehiculo):
    __marca="BMW"
    __version=''

    def __init__(self, modelo, cantp, color, preciobase,version):
        super().__init__(modelo, cantp, color, preciobase)
        self.__version=version



    @classmethod
    def getmarca(cls):
        return cls.__marca


    def getversion(self):
        return self.__version


    def ImporteDeVenta(self):
        importe=0
        

        if self.__version=="full":
            importe=int(super().getprecio())+(12/100)*int(super().getprecio())

        else:
            importe=int(super().getprecio())+(10/100)*int(super().getprecio())

        return importe


    def toJSON(self):
        d=dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                            modelo=self.getmodelo(),
                            preciobase=self.getprecio(),
                            color=self.getcolor(),
                            cantp=self.getcantp(), 
                            version=self.__version
                            )
            )
        return d