from ClaseLibro import Libro
from ClaseCapitulo import Capitulo
import csv


class ManejadorLibro:
    __lista=[]

    def __init__(self):
        self.__lista=[]


    def CargarLibros(self):
        archivo=open("libros.csv")
        lista=[]
        reader=csv.reader(archivo,delimiter=",")
        i=0
        for fila in reader:
            if len(fila)>2:
                L=Libro(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])
        
                
            if len(fila)==2:
                L.cargarcapitulo(Capitulo(fila[0],fila[1]))
                i+=1

            if i >= L.getcantcapitulos():
                i=0
                cant=0
                self.__lista.append(L)


        archivo.close()



    def Muestraporid(self,id):
        i=0
        while i<len(self.__lista) and self.__lista[i].getid() != id:
            i+=1

        if i<len(self.__lista):
            print("\nTitulo: {}\n".format(self.__lista[i].getitulo()))
            print("Capitulos:\n")
            for j in range(int(self.__lista[i].getcantcapitulos())):
                print("{}- {}\n".format(j+1,self.__lista[i].getcapitulo(j)))
                
                
            print("\nCantidad total de paginas: {}".format(self.__lista[i].getpag()))
        else:
            print("\nError-La id ingresada no se encuentra registrada.")



    def BuscarPalabracapitulos(self,palabra,i):
        j=0
        cant=self.__lista[i].getcantcapitulos()
        
        while j< cant and palabra not in self.__lista[i].getcapitulo(j):
            j+=1

        if j<cant:
            return True

        else:
            return False




    def BuscarPalabra(self,palabra):
        bandera=False
        for i in range(len(self.__lista)):
            if palabra in self.__lista[i].getitulo():
                self.Mostrar(i)
                bandera=True

        
            else:
                for j in range(self.__lista[i].getcantcapitulos()):
                    if palabra in self.__lista[i].getcapitulo(j):
                        self.Mostrar(i)
                        bandera=True
                        
        if bandera==False:
            print("\nLa palabra ingresada no se encontro.")
            




    def Mostrar(self,i):
        print("\nTitulo: {}\nAutor: {}\n".format(self.__lista[i].getitulo(),self.__lista[i].getautor()))
        
