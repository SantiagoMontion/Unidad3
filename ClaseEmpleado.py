class Empleado:
    __DNI=''
    __nombre=''
    __direccion=''
    __telefono=''


    def __init__(self,dni,nom,direc,tel):
        self.__DNI=dni
        self.__nombre=nom
        self.__direccion=direc
        self.__telefono=tel


    def getdireccion(self):
        return self.__direccion

    def getnombre(self):
        return self.__nombre

    def getdni(self):
        return self.__DNI

    def gettelefono(self):
        return self.__telefono
        
