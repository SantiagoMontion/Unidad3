from ClasePersonal import Personal

class Apoyo(Personal):
    __categoria=''


    def __init__(self, cuil, apellido, nombre, sueldobasico, antiguedad,categoria):
        super().__init__(cuil, apellido, nombre, sueldobasico, antiguedad)
        self.__categoria=categoria


    def getcategoria(self):
        return self.__categoria


    def CalcularSueldo(self):

        sueldo=self.getsueldo()
        if self.__categoria >=1 and self.__categoria <=10:
            sueldo+=(10/100)*sueldo

        elif self.__categoria>=21 and self.__categoria<=22:
            sueldo+=(20/100)*sueldo

        elif self.__categoria>=11 and self.__categoria<=20:
            sueldo+=(30/100)*sueldo


    def __lt__(self,O):
        menor=False
        if self.getnombre()<O.getnombre():
            menor=True
        
        return menor

    def mostrar(self):
        cadena="\nCUIL: "+self.getcuil()+"\nNombre: "+self.getnombre()+"\nApellido: "+self.getapellido()+"Sueldo: "+str(self.CalcularSueldo())
        cadena+="\nAntiguedad: "+str(self.getantiguedad())+"\nCategoria: "+self.__categoria
        return cadena


    def toJSON(self):
        d=dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                            cuil=self.getcuil(),
                            apellido=self.getapellido(),
                            nombre=self.getnombre(),
                            sueldobasico=self.getsueldo(), 
                            antiguedad=self.getantiguedad(),
                            categoria=self.__categoria,
                            )
            )
        return d