from ClaseSabor import Sabor
class Helado:
    __gramos=0
    __Sabor=[]
   

    def __init__(self,gramos,sabores=None):
        self.__gramos=gramos
        self.__Sabor=[]
        if sabores!=None:
            self.AgregarSabor(sabores)
            self.__cantidad=len(sabores)
        


    def AgregarSabor(self,sabores):
        for i in range(len(sabores)):
            self.__Sabor.append(sabores[i])


    def getsabores(self):
        return self.__Sabor

    def getgramos(self):
        return self.__gramos




