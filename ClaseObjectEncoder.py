import json
from ClaseLista import Lista
from ClaseVehiculoNuevo import VehiculoNuevo
from ClaseVehiculoUsado import VehiculoUsado

class ObjectEncoder(object):

    def GuardarArchivo(self, vehiculos, archivo):   
        with open(archivo, "w", encoding="UTF-8")as destino:
            json.dump(vehiculos, destino, indent=4)
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
                vehiculos = d["Vehiculos"]
                Vehiculos = class_()
                for i in range(len(vehiculos)):
                    dv= vehiculos[i]
                    class_name = dv.pop("__class__")
                    class_ = eval(class_name)
                    atributos = dv["__atributos__"]
                    V = class_(**atributos)
                    Vehiculos.agregarvehiculo(V)
                return Vehiculos