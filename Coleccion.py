from os import name
from zope.interface import implementer
from Iinterface import interface
@implementer(interface)

class Coleccion:
    __lista=[]


    def __init__(self):
        self.__lista=[]


    def insertarelemento(self,obj,pos):
        try:
            self.__lista.insert(pos,obj)

        except:
            print("\nError al insertar, posicion no valida.")



    def agregarelemento(self,obj):
        self.__lista.append(obj)


    def mostrarelemento(self,pos):
        try:
            print(self.__lista[pos-1])

        except IndexError:
            print("\nError al insertar, posicion no valida.")

