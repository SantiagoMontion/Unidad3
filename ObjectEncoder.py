from ClasePersonal import Personal
import json
from ClaseLista import Lista
from ClaseApoyo import Apoyo
from ClaseDocente import Docente
from ClaseInvestigador import Investigador
from ClaseDocenteInvestigador import DocenteInvestigador

class ObjectEncoder(object):

    def GuardarArchivo(self, personal, archivo):   
        with open(archivo, "w", encoding="UTF-8")as destino:
            json.dump(personal, destino, indent=4)
        destino.close()
        print("\nGuardado con exito!")

    def LeerArchivo(self, archivo):
        with open(archivo, encoding="UTF-8")as fuente:
            d=json.load(fuente)
            fuente.close()
            return d

    def Decodificador(self, d):
        if "__class__" not in d:
            return d 
        else:
            class_name = d["__class__"]
            class_=eval(class_name)
            if class_name == "Lista":
                personal = d["Personal"]
                Personal = class_()
                for i in range(len(personal)):
                    dv= personal[i]
                    class_name = dv.pop("__class__")
                    class_ = eval(class_name)
                    atributos = dv["__atributos__"]
                    V = class_(**atributos)
                    Personal.AgregarPersonal(V)
                return Personal