from ClaseHelado import Helado

class ManejadorHelado:
    __lista=[]


    def __init__(self):
        self.__lista=[]



    def RegistrarHelado(self,gramos,sabores):
        
        if type(gramos)==int:
            H=Helado(gramos,sabores)
            self.__lista.append(H)



    def Maspedidos(self):
        listado=[]
        for i in range(len(self.__lista)):
            
            sabores=self.__lista[i].getsabores()
            for j in range(len(sabores)):
                listado.append(sabores[j].getnombre())
                
        top=[]
        anteriores=[]
        
        
        for i in range(len(listado)):
            if anteriores.count(listado[i])<1:
                top.append((listado[i],listado.count(listado[i])))
                anteriores.append(listado[i])
        
        top.sort(key=lambda x:x[1],reverse=True)
        print("\n---Top 5 Sabores mas pedidos---\n")
        i=0
        while i < (len(top)) and i<5:
            print("\n{}- {} con {} unidades".format(i+1,top[i][0].center(12),top[i][1]))
            i+=1
        input()


    def Estimargramos(self,sabor):
        total=0
        for i in range(len(self.__lista)):
            if sabor in self.__lista[i].getsabores():
                gramos=int(self.__lista[i].getgramos())
                cants=len(self.__lista[i].getsabores())
                print(cants)
                total=total+(gramos/cants)
        print("\nLa cantidad de gramos vendidos para el sabor {} es: {}".format(sabor.getnombre(),total))


        
                
    def SaboresvendidosxTam(self,tipo):
        listado=[]
        for i in range(len(self.__lista)):
            
            sabores=self.__lista[i].getsabores()
            for j in range(len(sabores)):
                if int(self.__lista[i].getgramos())==tipo:
                    listado.append(sabores[j].getnombre())
        
        for i in range(len(listado)):
            print("{}- {}\n".format(i+1,listado[i]))

        input()
        
                    

