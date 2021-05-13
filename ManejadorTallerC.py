from ClaseTallerCapacitacion import TallerCapacitacion
import numpy as np
import csv

class ManejadorTaller:
    __arreglo=None
    __actual=0
    __dimension=0


    def __init__(self):
        archivo=open("Talleres.csv")
        reader=csv.reader(archivo,delimiter=",")
        for fila in reader:
            if len(fila)==1:
                self.__dimension=int(fila[0])
                self.__arreglo=np.empty(self.__dimension,dtype=TallerCapacitacion)
                self.__actual=0

            else:
                T=TallerCapacitacion(fila[0],fila[1],fila[2],fila[3])
                self.__arreglo[self.__actual]=T
                self.__actual+=1



    def buscartaller(self,id):
        i=0
        while i<self.__dimension and int(self.__arreglo[i].getid()) != id:
            i+=1

        if i<self.__dimension:
            self.__arreglo[i].modificarcantidad()
            return self.__arreglo[i]









    

