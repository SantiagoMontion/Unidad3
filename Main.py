import os
from Menu import Menu
from ObjectEncoder import ObjectEncoder
from ClaseLista import Lista

def opciones():
    print("\n-----Menu-----\n")
    print("\n1- Insertar a agentes a la colección.")
    print("\n2- Agregar agentes a la colección.")
    print("\n3- Mostrar que tipo de agente se encuentra en dicha posición.")
    print("\n4- Mostrar los agentes que se desempeñan como docentes-investigadores.")
    print("\n5- Mostrar la cantidad de agentes, segun area")
    print("\n6- Mostrar listado de todos los agentes, ordenado por apellido.")
    print("\n7- Mostrar listado segun categoría de investigación (I, II, III, IV o V).")
    print("\n8- Guardar en el archivo.")
    op=int(input("\nSeleccione una opcion: "))
    return op

def CargarLista():

    try:
        encoder=ObjectEncoder()
        dic=encoder.LeerArchivo("personal.json")
        personal=encoder.Decodificador(dic)
        return personal
    except:

        personal=Lista()
        return personal
        

    
    



if __name__=='__main__':
    M=Menu()
    lista=CargarLista()
    op=opciones()
    while op>=0 <=8:
        M.opcion(op,lista)
        op=opciones()
        os.system("cls")



