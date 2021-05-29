from ClasePersonal import Personal
from ClaseApoyo import Apoyo
from ClaseDocente import Docente
from ClaseInvestigador import Investigador
from ClaseDocenteInvestigador import DocenteInvestigador
from zope.interface import implementer
from Iinterface import interface

from ClaseNodo import Nodo

@implementer(interface)
class Lista:
    __comienzo=None
    __actual=None
    __indice=0
    __tope=0


    def __init__(self):
        self.__comienzo=None
        self.__actual=None


    def CargarPersonal(self):
        cuil=input("\nIngrese su CUIL: ")
        apellido=input("\nIngrese su apellido: ")
        nombre=input("\nIngrese su nombre: ")
        sueldo=input("\nIngrese su sueldo: ")
        antiguedad=input("\nIngrese su antiguedad: ")

        tipo=input("\nIngrese su Tipo de cargo: (D= Docentes, I= investigadores, DI= docente investigador, A=personal de apoyo)").lower()

        if tipo == "d":
            carrera=input("\nIngrese la carrera: ")
            cargo=input("\nIngrese el cargo que ocupa: ")
            catedra=input("\nIngrese la catedra: ")
            P=Docente(cuil,apellido,nombre,sueldo,antiguedad,carrera,cargo,catedra)
        
        elif tipo == "i":
            areainv=input("\nIngrese el area de investigacion: ")
            tipoinv=input("\nIngrese el tipo de investigacion: ")
            P=Investigador(cuil,apellido,nombre,sueldo,antiguedad,areainv,tipoinv)

        elif tipo == "di":
            carrera=input("\nIngrese la carrera: ")
            cargo=input("\nIngrese el cargo que ocupa: ")
            catedra=input("\nIngrese la catedra: ")
            areainv=input("\nIngrese el area de investigacion: ")
            tipoinv=input("\nIngrese el tipo de investigacion: ")
            categoria=input("\nIngrese la categoria: ")
            importeextra=int(input("\nIngrese el importe extra: "))
            P=DocenteInvestigador(cuil,apellido,nombre,sueldo,antiguedad,carrera,cargo,catedra,categoria,importeextra,areainv,tipoinv)

        elif tipo == "A":
            categoria=input("\nIngrese la categoria: ")
            P=Apoyo(cuil,apellido,nombre,sueldo,antiguedad,categoria)

        return P

    def AgregarPersonal(self,personal):
        if isinstance(personal,Personal):
            nodo=Nodo(personal)
            nodo.setsiguiente(self.__comienzo)
            self.__comienzo=nodo
            self.__actual=nodo
            self.__tope+=1
            print("\nPersonal agregado con exito!")


    def InsertarPersonal(self,personal,pos):
        com=self.__comienzo
        i=0
        nodo=Nodo(personal)
        while i < pos and com != None:
            com=com.getsig()
            i+=1

        if com == None:
            print("\nERROR no se encuentra nada en dicha posicion")
            

        else:
            nodo.setsiguiente(com.getsig())
            com.setsiguiente(nodo)
            self.__tope +=1
            print("\nPersonal insertado con exito!")



    def MostrarSegunPosicion(self,pos):
        com=self.__comienzo
        i=0
        while i <= self.__tope and com != None and i!=pos:
            com=com.getsig()
            i+=1

        if i <= self.__tope and com !=None:
                if type(com.getpersonal()) == Apoyo:
                    print("En esta posicion se encuentra un personal de apoyo")
                elif type(com.getpersonal()) == Docente:
                    print("En esta posicion se encuentra un Docente")
                elif type(com.getpersonal()) == Investigador:
                    print("En esta posicion se encuentra un Investigador")
                elif type(com.getpersonal()) == DocenteInvestigador:
                    print("En esta posicion se encuentra un Docente-Investigador")

        else:
            print("\n Posicion incorrecta.")

        

    def MostrarDI(self,carrera):
        actual = self.__comienzo  
        i = None  
          
        while(actual != None):  
            i = actual.getsig()
                  
            while(i != None):  
                 
                if actual.getpersonal().getnombre() > i.getpersonal().getnombre():
                    temp = actual.getpersonal
                    actual.getpersonal = i.getpersonal
                    i.getpersonal = temp
                    
                i = i.getsig()
            actual = actual.getsig()


        for i in self:
            if type(i)==DocenteInvestigador and i.getcarrera() == carrera:

                print(i.mostrar())


    def Mostrarporarea(self,area):
        contdi=0
        conti=0
        for i in self:
            if type(i) == DocenteInvestigador:
                if i.getarea() == area:
                    contdi+=1

            elif type(i)== Investigador:
                if i.getarea() == area:
                    conti+=1

        print("\nLa cantidad de DocenteInvestigadores de esta area es: {}\nLa cantidad de Investigadores es: {}".format(contdi,conti))


    def MostrarListado(self):
        actual = self.__comienzo  
        i = None  
          
        while(actual != None):  
            i = actual.getsig()
                  
            while(i != None):  
                     
                if(actual.getpersonal().getapellido() > i.getpersonal().getapellido()):  
                    temp = actual.getpersonal
                    actual.getpersonal = i.getpersonal
                    i.getpersonal = temp
                    
                i = i.getsig()
            actual = actual.getsig()

        for i in self:
            cadena=''
            tipo=type(i)
            if tipo == Apoyo:
                cadena="Personal de apoyo"
            elif tipo == Docente:
                cadena="Docente"
            elif tipo == Investigador:
                cadena="Investigador"
            elif tipo == DocenteInvestigador:
                cadena="Docente-Investigador"

            print("\nNombre: {}\nApellido: {}\nTipo de agente: {}\nSueldo: {}".format(i.getnombre(),i.getapellido(),cadena,i.getsueldo()))
            


    def __iter__(self):
        return self

    def __len__(self):
        return self.__tope

    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration

        else:
            if self.__actual!=None:
                self.__indice+=1
            
                personal=self.__actual.getpersonal()
                if self.__actual.getsig!=None:
                    self.__actual=self.__actual.getsig()
                    return personal



    def MostrarporCategoria(self,categoria):
        total=0   
        for i in self:
            if type(i) == DocenteInvestigador and i.getcategoria() == categoria:
                print("\nApellido: {}\nNombre: {}\nImporte extra: {}".format(i.getapellido(),i.getnombre(),i.getimporteextra()))
                total+=int(i.getimporteextra())

        print("\nTotal de dinero que la Secretaría de Investigación debe solicitar al Ministerio: {}".format(total))

        
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            Personal=[p.toJSON() for p in self]

        )
        return d 
