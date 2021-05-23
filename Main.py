from ClaseLista import Lista
from Menu import Menu
from ClaseVehiculoNuevo import VehiculoNuevo
from ClaseVehiculoUsado import VehiculoUsado
from ClaseObjectEncoder import ObjectEncoder
import os
def opciones():
    print("\n-----Menu-----\n")
    print("\n1- Insertar un vehículo.")
    print("\n2- Agregar un vehículo.")
    print("\n3- Mostrar vehiculo segun posicion.")
    print("\n4- Modificar precio segun patente.")
    print("\n5- Mostrar datos del vehiculo mas economico")
    print("\n6- Mostrar todos los vehiculos a la venta.")
    print("\n7- Guardar en el archivo.")
    op=int(input("\nSeleccione una opcion: "))
    return op

def CargarLista():

    try:
        encoder=ObjectEncoder()
        dic=encoder.LeerArchivo("vehiculos.json")
        vehiculos=encoder.Decodificador(dic)
        return vehiculos
    except:
        vehiculos=Lista()
        return vehiculos

    


if __name__=='__main__':
    M=Menu()
    lista=CargarLista()
    op=opciones()
    while op!=0 <=7:
        M.opcion(op,lista)
        op=opciones()
        os.system("cls")

    M.test(lista)




