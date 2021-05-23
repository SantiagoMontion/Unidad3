from ClaseVehiculoNuevo import VehiculoNuevo
from ClaseVehiculoUsado import VehiculoUsado
from zope.interface import implementer
from Iinterface import interface
from ClaseVehiculo import Vehiculo
from ClaseNodo import Nodo

@implementer(interface)
class Lista:
    __comienzo=None
    __actual=None
    __indice=0
    __tope=0


    def __init__(self):
        self.__comienzo=None
        self.__actual=None

    def agregarvehiculo(self,vehiculo):
        if isinstance(vehiculo,Vehiculo):
            nodo=Nodo(vehiculo)
            nodo.setsiguiente(self.__comienzo)
            self.__comienzo=nodo
            self.__actual=nodo
            self.__tope+=1
            print("\nVehiculo agregado con exito!")


    def instertarvehiculo(self,vehiculo,pos):
        com=self.__comienzo
        i=0
        nodo=Nodo(vehiculo)
        while i < pos and com != None:
            com=com.getsig()
            i+=1

        if com == None:
            print("\nERROR no se encuentra nada en dicha posicion")
            

        else:
            nodo.setsiguiente(com.getsig())
            com.setsiguiente(nodo)
            self.__tope +=1
            print("\nVehiculo insertado con exito!")

        
    def mostrarporpos(self,pos):
        if pos<self.__tope:
            i=0
            com=self.__comienzo
            while i!=pos and com !=None and pos<=self.__tope:
                com=com.getsig()
                i+=1

            if i == pos:
                if type(com.getvehiculo()) == VehiculoUsado:
                    print("En esta posicion se encuentra un AutoUsado")
                elif type(com.getvehiculo()) == VehiculoNuevo:
                    print("En esta posicion se encuentra un AutoNuevo")

        else:
            print("\n Posicion incorrecta.")
            
                

    def Mostrar(self):
        aux = self.__comienzo
        print("\n------LISTADO-------")
        while aux!=None:
            print("\nModelo: {}\nCant Puertas: {}\nImporte: ${}\n".format(aux.getvehiculo().getmodelo(),aux.getvehiculo().getcantp(),aux.getvehiculo().ImporteDeVenta()))
            aux = aux.getsig()



    def modificarpreciobase(self,patente):
        try:
            i=0
            com=self.__comienzo
            while i< self.__tope and com !=None and patente!= com.getvehiculo().getpatente():
                com=com.getsig()
                i+=1

            if i<self.__tope:
                nuevo=int(input("\nIngrese el nuevo precio: "))
                com.getvehiculo().modificarpreciobase(nuevo)
                print("\nModificado con exito! nuevo precio base: {}\nPrecio Venta: {}".format(com.getvehiculo().getprecio(),com.getvehiculo().ImporteDeVenta()))
 
        except:
            pass


    def maseconomico(self):
        try:
            i=0
            com=self.__comienzo
            min=99999999
        #Mostrar todos los datos, incluido el importe de venta, del vehículo más económico.
            while i< self.__tope and com!=None:
                if int(com.getvehiculo().getprecio())<min:
                    min=int(com.getvehiculo().getprecio())
                i+=1

            print("\nEl vehiculo mas economico es:\n")
            print(com.getvehiculo())
            if isinstance(com.getvehiculo(), VehiculoNuevo):
                print("\nMarca: {}\nVersion: {}\nImportedeventa: {}\n".format(com.getvehiculo().getmarca(),com.getvehiculo().getversion(),com.getvehiculo().ImporteDeVenta()))

            elif isinstance(com.getvehiculo(),VehiculoUsado):
                print("\nMarca: {}\nPatente: {}\nAño: {}\nKm: {}\nImportedeventa: {}\n".format(com.getvehiculo().getmarca(),com.getvehiculo().getpatente(),com.getvehiculo().getanio(),com.getvehiculo().getkm(),com.getvehiculo().ImporteDeVenta()))

        except:
            print("\nError, lista vacia.")






    def __iter__(self):
        return self

    def __len__(self):
        return self.__tope

    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration

        else:
            self.__indice+=1
            vehiculo=self.__actual.getvehiculo()
            self.__actual=self.__actual.getsig()
            return vehiculo


    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            Vehiculos=[v.toJSON() for v in self]

        )
        return d 


