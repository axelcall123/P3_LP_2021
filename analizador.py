
def analizador(texto):
    N_Terminales=[]
    Terminales=[]
    N_Terminales_I=[]
    unir=''
    state=-1
    conteoG=1
    contTxt=0
    Nombre_gramatica=""
    for txt in texto:
        contTxt+=1      
        if state==-1:
            if txt=="\n":
                state=-1
            elif txt!="\n":
                unir=unir+txt
                state=0

        elif state==0:#ESPACIO POR ERROR
            if txt!="\n":
                unir=unir+txt
            else:
                Nombre_gramatica=unir
                unir=""
                state=1
        elif state==1:
            if txt=="\n":
                state=1
            if txt!="," and txt!=";" and txt!="\n":
                unir=unir+txt
                state=2
        elif state==2:
            if txt!="," and txt!=";" and txt!="\n":
                unir=unir+txt
            elif txt==",":
                if conteoG==1:
                    N_Terminales.append(unir)
                elif conteoG==2:
                    Terminales.append(unir)
                elif conteoG==3:
                    N_Terminales_I.append(unir)
                unir=""
                state=2
            elif txt==";":
                if conteoG==1:#AGREGAR NT,T,NTI
                    N_Terminales.append(unir)
                elif conteoG==2:
                    Terminales.append(unir)
                elif conteoG==3:
                    N_Terminales_I.append(unir)
                unir=""
                conteoG+=1
                state=2
            elif txt=="\n":
                if conteoG==1:#AGREGAR NT,T,NTI
                    N_Terminales.append(unir)
                elif conteoG==2:
                    Terminales.append(unir)
                elif conteoG==3:
                    N_Terminales_I.append(unir)
                unir=""
                state=3
        elif state==3:
            if contTxt<len(texto):
                unir=unir+txt
            else:
                #print(N_Terminales,Terminales,N_Terminales_I)
                #print(unir,"TXT")    
                return de_or(unir,Nombre_gramatica,N_Terminales,Terminales,N_Terminales_I)
                

def de_or(texto,Nombre,NT,T,NTI):#[[[S],[aB cS]],[]]
    iz=""#PROUCCION IZQUIERDA
    de=""#PRODUCCION DERECHA
    cont=0#llego al final del txt
    state=0
    array_producciones=[]
    for txt in texto:
        if state==0:#saltos
            if txt=="\n":
                state=0
            else:
                iz=iz+txt 
                state=1

        elif state==1:#-
            if txt!="-":
                iz=iz+txt
            elif txt=="-":
                state=2

        elif state==2:#
            if txt==" ":
                state=2
            elif txt==">":
                state=3

        elif state==3:
            if txt!="\n":
                de=de+txt
            elif txt=="\n":
                array_producciones.append([iz.replace(' ',''),de])#PRODUCCION IZQUIERDA Y DERECHA
                iz=""
                de=""
                state=0

            if cont==len(texto)-1:
                array_producciones.append([iz.replace(' ',''),de])
        cont+=1
    
    contT=0#CONETO DE TERMINALES
    contNt=0#CONETO DE NO TERMINALES
    regular=True#SI ES UNA EXPRESION NO REGULAR
    for a in range(len(array_producciones)):#LINEAS DE PRODUCCION [S,0 A]
        T_NT=array_producciones[a][1].split(' ')#[0,A]
        for b in range(len(T_NT)):#SEPARA T, NT
            for c in range(len(T)):#CUENTA LOS TERMINALES
                if T[c]==T_NT[b]:
                    contT+=1
            for c in range(len(NT)):#CUETNA LOS NO TERMINALES
                if NT[c]==T_NT[b]:
                    contNt+=1
        if contT>1 or contNt>1:#NO REGULAR
            regular=False
            break
        #print(array_producciones[a][1],"=  T:",contT,"NT:",contNt)
        contT=0
        contNt=0

            #print('pro',T_NT[b])
            
    #NO SIRVE AHORA
    # lineas=texto.split('\n')  
    # for lin in lineas:#[A,1 B]
    #     produccion=lin.split("->")
    #     array_producciones.append(produccion)d
    
    #imprime los S->a
    #print(array_producciones)
        #[nombre,no_terminales,terminales,no_terminal_ini,producciones]
    array_salida=[]
    if regular==False:
        array_salida.append(Nombre)
        array_salida.append(NT)
        array_salida.append(T)
        array_salida.append(NTI)
        array_salida.append(array_producciones)
        return array_salida
    else:
        print('ES UNA EXPRESION REGULAR:', Nombre)
        return

