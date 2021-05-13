from ClaseInscripcion import Inscripcion
import numpy as np
class ManejadorInscripcion:
    __arreglo=None
    __dimension=0
    __actual=0


    def __init__(self,dimension=1):
        self.__dimension=dimension
        self.__actual=0
        self.__arreglo=np.empty(self.__dimension,dtype=Inscripcion)



    def inscribir(self,I):
        if isinstance(I,Inscripcion):
            if self.__dimension==self.__actual:
                self.__dimension+=1
                self.__arreglo.resize(self.__dimension,refcheck=False)
            self.__arreglo[self.__actual]=I
            self.__actual+=1
            
            print("\nUsted esta inscripto! ")
                


    def Consultar(self,dni):
        i=0
        while i<self.__dimension and self.__arreglo[i].getpersona().getdni()!=dni:
            i+=1

        if i<self.__dimension:
            t=self.__arreglo[i].gettaller()
            if self.__arreglo[self.__actual-1].getpago() == False:
                adeuda=t.getmontoinsc()
            else:
                adeuda=0
            print("\n---Persona Inscripta---\nTaller: {}\nMonto que adeuda: {}".format(t.getnombretaller(),adeuda))


    def Listar(self,id):
        
        print("\nInscriptos: ")
        for i in range(int(self.__dimension)):
            if self.__arreglo[i].gettaller().getid()==id:
                print("\nAlumno:{} \nDni: {}".format(self.__arreglo[i].getpersona().getnombre().ljust(20),self.__arreglo[i].getpersona().getdni()))
        



    def registrarpago(self,dni):
        i=0
        while i<self.__dimension and self.__arreglo[i].getpersona().getdni()!=dni:
            i+=1

        if i<self.__dimension:
            self.__arreglo[i].pagar()
            print("\nPago realizado con exito!")



    def GuardarArchivo(self):
        cadena=[]

        for i in range(self.__dimension):
            cadena.append(self.__arreglo[i].getpersona().getdni())
            cadena.append(",")
            cadena.append(self.__arreglo[i].gettaller().getid())
            cadena.append(",")
            cadena.append(self.__arreglo[i].getfecha())
            cadena.append(",")
            cadena.append(self.__arreglo[i].getpago())
            cadena.append("\n")

            archivo=open("Inscripciones.csv","w")
        for j in range(len(cadena)):
            archivo.write(str(cadena[j]))
        archivo.close()

        print("\nDatos Guardados con exito!")
