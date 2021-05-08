
class Capitulo:
    __titulo=''
    __cantitdadPaginas=0

    def __init__(self,titulo,cantP):
        self.__titulo=titulo
        self.__cantitdadPaginas=cantP


    def getcantp(self):
        return self.__cantitdadPaginas

    def getitulocap(self):
        return self.__titulo



