from ClasePersonal import Personal

class Docente(Personal):
    __carrera=''
    __cargo=''
    __catedra=''

    def __init__(self, cuil, apellido, nombre, sueldobasico, antiguedad,carrera,cargo,catedra,areainv='',tipoinv=''):
        super().__init__(cuil, apellido, nombre, sueldobasico, antiguedad,areainv,tipoinv,carrera,cargo,catedra)
        self.__carrera=carrera
        self.__cargo=cargo
        self.__catedra=catedra


    def getcarrera(self):
        return self.__carrera

    def getcargo(self):
        return self.__cargo

    def getcatedra(self):
        return self.__catedra

    def Calcularsueldo(self):
        sueldo=int(self.getsueldo())
        if self.__cargo=='simple':
            sueldo+=(10/100)*sueldo

        elif self.__cargo =="semiexclusivo":
            sueldo+=(20/100)*sueldo

        elif self.__cargo =="exclusivo":
            sueldo+=(50/100)*sueldo

        return sueldo


    def __lt__(self,O):
        menor=False
        if self.getnombre()<O.getnombre():
            menor=True
        
        return menor




    def mostrar(self):
        cadena="\nCUIL: "+self.getcuil()+"\nNombre: "+self.getnombre()+"\nApellido: "+self.getapellido()+"Sueldo: "+str(self.Calcularsueldo())
        cadena+="\nAntiguedad: "+str(self.getantiguedad())+"\nCarrera: "+self.__carrera+"\nCargo: "+self.__cargo+"\nCatedra: "+self.__catedra
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
                            carrera=self.__carrera,
                            cargo=self.__cargo,
                            catedra=self.__catedra,
                            
                            )
            )
        return d