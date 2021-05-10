from ClaseSabor import Sabor
import csv

class ManejadorSabor:
    __lista=[]


    def __init__(self):
        self.__lista=[]


    def CargarSabores(self):
        archivo=open("sabores.csv")
        reader=csv.reader(archivo,delimiter=",")

        for fila in reader:
            if fila[0].isdigit()==True:
                S=Sabor(fila[0], fila[1], fila[2])
                self.__lista.append(S)

        archivo.close()



    def Muestra(self,):
        for i in range(len(self.__lista)):
            print("{}- {}  Descripcion: {}".format(self.__lista[i].getnum(),self.__lista[i].getnombre(),self.__lista[i].getdesc()))
        

    def retornasabor(self,s):      
        if type(s)==int:
            return self.__lista[s]
