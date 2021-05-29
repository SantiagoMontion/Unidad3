from ClaseDocente import Docente
from ClaseInvestigador import Investigador

class DocenteInvestigador(Docente, Investigador):
    __categoria = str
    __importeextra = int

    def __init__(self,cuil,apellido,nombre,sueldo,antiguedad,carrera,cargo,catedra,categoria,importeextra,areainv,tipoinv):
        self.__categoria = categoria
        self.__importeextra = importeextra
        super().__init__(cuil,apellido,nombre,sueldo,antiguedad,carrera,cargo,catedra,areainv,tipoinv)


    def getcategoria(self):
        return self.__categoria

    def getimporteextra(self):
        return self.__importeextra


    def CalcularSueldo(self):
        sueldo=Docente.Calcularsueldo(self)+self.__importeextra
        return sueldo #11550 + 50 =11600



    def mostrar(self):
        cadena="\nCUIL: "+self.getcuil()+"\nNombre: "+self.getnombre()+"\nApellido: "+self.getapellido()+"\nSueldo: "+str(self.CalcularSueldo())
        cadena+="\nAntiguedad: "+str(self.getantiguedad())+"\nCarrera: "+self.getcarrera()+"\nCargo: "+self.getcargo()
        cadena+="\nCatedra: "+self.getcatedra()+"\nCategoria: "+self.getcategoria()+"\nArea Investigacion: "+self.getarea()
        cadena+="\nTipo Investigacion: "+self.gettipo()+"\nImporte extra: "+str(self.getimporteextra())
        return cadena



    def toJSON(self):
        d=dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                            cuil=self.getcuil(),
                            apellido=self.getapellido(),
                            nombre=self.getnombre(),
                            sueldo=self.getsueldo(), 
                            antiguedad=self.getantiguedad(),
                            carrera=self.getcarrera(),
                            cargo=self.getcargo(),
                            catedra=self.getcatedra(),
                            categoria=self.__categoria,
                            importeextra=self.__importeextra,
                            areainv=self.getarea(),
                            tipoinv=self.gettipo()
                            )
            )
        return d
