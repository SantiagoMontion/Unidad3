class FechaHora:
    __dia=0
    __mes=0
    __anio=0



    def __init__(self,anio,mes,dia):
        if type(dia)==int and type(mes)==int and type(anio)==int:
            self.__dia=dia
            self.__mes=mes
            self.__anio=anio
            self.check()
        else:
            print("Datos Incorrectos\n")


    def Mostrar(self):
        print("FECHA {}/{}/{}".format(self.__dia,self.__mes,self.__anio))



    def check(self):


        if self.__anio<0:
            self.__anio=1
            self.__mes=1

        if self.__mes<0:
            self.__anio-=1
            self.__mes=1

        if self.__dia<0:
            self.__mes-=1
            self.__dia=1


#divisible por 4, y si es divisible por 100, debe ser divisible por 400
        if self.__anio%4==0 and self.__anio%100!=0:
            #Año bisiesto
            
            if self.__mes==2 and self.__dia>29:
                self.__dia=1
                self.__mes+=1
        elif self.__anio%100==0 and self.__anio%400 ==0:
            #Año bisiesto
            
            if self.__mes==2 and self.__dia>29:
                
                self.__dia=1
                self.__mes+=1

        else:
            if self.__mes>=12:
                self.__anio+=1
                self.__mes=1

            if self.__mes == 2 and self.__dia>28:
                self.__mes+=1
                self.__dia=1
                
            
            if (self.__mes == 4 or self.__mes==6 or self.__mes==9 or self.__mes==11) and (self.__dia>30):
                self.__dia=1
                self.__mes+=1
       
            
            elif (self.__mes==1 or self.__mes==3 or self.__mes==5 or self.__mes==7 or self.__mes==8 or self.__mes==10 or self.__mes==12) and (self.__dia>31):
                self.__dia=1
                self.__mes+=1
                if self.__mes>12:
                    self.__mes=1
                    self.__anio+=1


            


    def __gt__(self, F):
        mayor=False
        if int(self.__anio)>int(F.__anio):
            mayor=True
        
        else:
            mayor=False


        if int(self.__anio) == int(F.__anio):
            if int(self.__mes)>int(F.__mes): 
                mayor=True
            else:
                mayor=False


            if int(self.__mes)==int(F.__mes):
                if int(self.__dia)>int(F.__dia):
                    mayor=True
                else:
                    mayor=False

        return mayor


