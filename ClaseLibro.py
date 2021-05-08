from ClaseCapitulo import Capitulo


class Libro:
    __idLibro=0
    __titulo=''
    __autor=''
    __editorial=''
    __isbn=0
    __cantidadCapitulos=0
    __Capitulo=[]

    
    def __init__(self,id,titulo,autor,edit,isbn,cantcap):
        self.__idLibro=id
        self.__titulo=titulo
        self.__autor=autor
        self.__editorial=edit
        self.__isbn=isbn
        self.__cantidadCapitulos=cantcap  
        self.__Capitulo=[]


    def cargarcapitulo(self, capitulo):
        if type(capitulo) == Capitulo:
            self.__Capitulo.append(capitulo)


    def __del__(self):
        print("\nBorrando Libro...")
        del self.__Capitulo

    def getid(self):
        return int(self.__idLibro)

    def getitulo(self):
        return self.__titulo

    def getcantcapitulos(self):
        return int(self.__cantidadCapitulos)

    def getcapitulo(self,j):
        return self.__Capitulo[j].getitulocap()

    def getpag(self):
        total=0
        for i in range(len(self.__Capitulo)):
            total+=int(self.__Capitulo[i].getcantp())

        return total

    def getautor(self):
        return self.__autor


  



