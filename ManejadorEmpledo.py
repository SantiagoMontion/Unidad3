from datetime import date
from os import read
import numpy as np
from ClaseEmpleado import Empleado
import csv
from ClaseEmpPlanta import EmpleadoDePlanta
from ClaseEmpContratado import EmpleadoContratado
from ClaseEmpExterno import EmpleadoExterno

class ManejadorEmpleado:
    __arreglo=None
    __dimension=0
    __actual=0

    def __init__(self,dimension):
        self.__dimension=dimension
        self.__actual=0
        self.__arreglo=np.empty(self.__dimension,dtype=Empleado)


    def CargarEmpleado(self,E):
        if isinstance(E,Empleado):
            if self.__dimension==self.__actual:
                self.__dimension+=1
                self.__arreglo.resize(self.__dimension,refcheck=False)
            self.__arreglo[self.__actual]=E
            self.__actual+=1
            print("empleado listo")
            
            


    def LeerEmpleadosdeplanta(self):
        archivo=open("planta.csv")
        reader=csv.reader(archivo,delimiter=';')

        for fila in reader:
            E=EmpleadoDePlanta(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
            self.CargarEmpleado(E)

        archivo.close()
    
    def LeerEmpleadosContratado(self):
        archivo=open("contratados.csv")
        reader=csv.reader(archivo,delimiter=';')

        for fila in reader:
            E=EmpleadoContratado(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6])
            self.CargarEmpleado(E)

        archivo.close()


    def LeerEmpleadosExterno(self):
        archivo=open("externos.csv")
        reader=csv.reader(archivo,delimiter=';')

        for fila in reader:
            E=EmpleadoExterno(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8],fila[9])
            self.CargarEmpleado(E)

        archivo.close()



    def incrementarhoras(self,dni,cant):
        i=0

        while i<self.__dimension and self.__arreglo[i].getdni() != dni:
            i+=1

        if i<int(self.__dimension):
            if isinstance(self.__arreglo[i],EmpleadoContratado):
                self.__arreglo[i].acumularhoras(int(cant))
            else:
                print("\nEmpleado incorrecto. (DEBE SER EMPLEAO CONTRATADO)")

        else:
            print("\nDNI incorrecto. Empleado no registrado")


    def Totaltarea(self,tarea):
        acum=0
        bandera=False
        for i in range(self.__dimension):
            if isinstance(self.__arreglo[i],EmpleadoExterno):
                fecha=date.today()
                if self.__arreglo[i].gettarea() == tarea and self.__arreglo[i].comprobarfecha(fecha)==True:
                    acum+=self.__arreglo[i].montoapagar()
                    bandera=True

        if bandera:
            print("\nEl monto a pagar por la tarea {} es: $ {}".format(tarea,acum))
        else:
            print("\nTarea incorrecta.")


    def ayuda(self):
        print("-------AYUDA------")
        for i in range(self.__dimension):
            if isinstance(self.__arreglo[i],EmpleadoDePlanta):
                if self.__arreglo[i].getsueldobasico()<25000:
                    #nombre, dirección y DNI de los empleados
                    print("\nNombre: {}\nDireccion: {}\nDNI: {}".format(self.__arreglo[i].getnombre(),self.__arreglo[i].getdireccion(),self.__arreglo[i].getdni()))



    def MostrarSueldos(self):
        print("\n------Sueldos-------")
        for i in range(self.__dimension):
            print("\nNombre: {}\nTelefono: {}\nSueldo: {}".format(self.__arreglo[i].getnombre(),self.__arreglo[i].gettelefono(),self.__arreglo[i].getsueldo()))

            
            
            

            


    