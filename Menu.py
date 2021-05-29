from ObjectEncoder import ObjectEncoder
import os

class Menu:
    __switcher=None
    __Encoder=None

    def __init__(self):
        self.__switcher = { 
            1:self.opcion1,
            2:self.opcion2,
            3:self.opcion3,
            4:self.opcion4,
            5:self.opcion5,
            6:self.opcion6,
            7:self.opcion7,
            8:self.opcion8,
            0:self.salir
            }
        self.__Encoder=ObjectEncoder()
    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op,lista):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func(lista)




    def salir(self,lista):
        print('Salir')


    def opcion1(self,lista):
        pos=int(input("\nIngrese la posicion: "))
        P=lista.CargarPersonal()
        lista.InsertarPersonal(P,pos-1)
        




    def opcion2(self,lista):
        P=lista.CargarPersonal()
        lista.AgregarPersonal(P)
        
        
        

    def opcion3(self,lista):
        pos=int(input("\nIngrese la posicion: "))
        lista.MostrarSegunPosicion(pos-1)
        

    def opcion4(self,lista):
        carrera=input("Ingrese el nombre de una carrera: ")

        lista.MostrarDI(carrera)
        
        

    def opcion5(self,lista):
        area=input("\nIngrese un area de investigacion: ")
        lista.Mostrarporarea(area)
        

    def opcion6(self,lista):
        lista.MostrarListado()
        
    def opcion7(self,lista): 
        categoria=input("\nIngrese una categoria: (I, II, III, IV o V)")
        lista.MostrarporCategoria(categoria)
        
    def opcion8(self,lista):
        self.__Encoder.GuardarArchivo(lista.toJSON(),"personal.json")






        