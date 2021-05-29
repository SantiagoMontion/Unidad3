from ClasePersonal import Personal
class Nodo:
    __personal=None
    __sig=None


    def __init__(self,personal): 
        self.__personal=personal
        self.__sig=None


    def setsiguiente(self,sig):
        self.__sig=sig
        
        
    def getsig(self):
        return self.__sig


    def getpersonal(self):
        return self.__personal

        