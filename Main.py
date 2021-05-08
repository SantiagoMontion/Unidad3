from Menu import Menu

def opciones():
    print("\n-----Menu-----\n")

    print("\n1- Mostrar datos del libro.")
    print("\n2- Buscar palabra en libro.")
    print("\n0- Salir.")
    op=int(input("\nSeleccione una opcion: "))
    return op


if __name__ == '__main__':
    M=Menu()
    op=opciones()
    


    while op!=0:
        M.opcion(op)
        op=opciones()
        
    M.test()
    


   
