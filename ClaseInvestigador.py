from ClasePersonal import Personal

class Investigador(Personal):
    __areainvestigacion=str
    __tipoinvestigacion=str
 

    def __init__(self, cuil, apellido, nombre, sueldobasico, antiguedad,areainvestigacion,tipoinvestigacion,carrera='',cargo='',catedra=''):
        super().__init__(cuil, apellido, nombre, sueldobasico, antiguedad,areainvestigacion,tipoinvestigacion,carrera,cargo,catedra)
        self.__areainvestigacion=areainvestigacion
        self.__tipoinvestigacion=tipoinvestigacion


    def getarea(self):
        return self.__areainvestigacion

    def gettipo(self):
        return self.__tipoinvestigacion


    def __lt__(self,O):
        menor=False
        if self.getnombre()<O.getnombre():
            menor=True
        
        return menor




    def mostrar(self):
        cadena="\nCUIL: "+self.getcuil()+"\nNombre: "+self.getnombre()+"\nApellido: "+self.getapellido()+"Sueldo: "+str(self.getsueldo())
        cadena+="\nAntiguedad: "+str(self.getantiguedad())+"\nArea Investigacion: "+self.__areainvestigacion+"\nTipo investigacion: "+self.__tipoinvestigacion
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
                            areainvestigacion=self.__areainvestigacion,
                            tipoinvestigacion=self.__tipoinvestigacion,
                           
                            )
            )
        return d