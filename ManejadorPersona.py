from ClasePersona import Persona


class ManejadorPersona:
    __lista=[]


    def __init__(self):
        self.__lista=[]


    def cargarpersona(self,P):
        if isinstance(P,Persona):
            self.__lista.append(P)

