N_Terminales=[]
Terminales=[]
N_Terminales_I=[]
def analizador(texto):
    unir=''
    state=-1
    conteoG=1
    contTxt=0
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
                print("Nombre de la gramática tipo 2",unir)
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
                print(N_Terminales,Terminales,N_Terminales_I)
                #print(unir,"TXT")    
                de_or(unir)

def de_or(texto):#[[[S],[aB cS]],[]]
    unir=""
    iz=""#PROUCCION IZQUIERDA
    de=""#PRODUCCION DERECHA
    txtProdu=""
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
                array_producciones.append([iz,de])
                iz=""
                de=""
                state=0

    # print(array_producciones)
    # lineas=texto.split('\n')
    # for a in range(len(lineas)):
    #         if lineas[a]=='':
    #             lineas.pop(a)
    #             a=a-1

        
    
    # for lin in lineas:#[A,1 B]
    #     produccion=lin.split("->")
    #     array_producciones.append(produccion)

    for array in array_producciones:
        if unir!=array[0]:#SI LA OPCION DIFERENTE DE: A-> ##
            unir=array[0]
            txtProdu=txtProdu+array[0]+"->"+array[1]+"\n"
        else:#SI NO:  |##
            for a in range(len(array[0])):#AGREGA EL TAMAÑO DE ESPACIOS DEL NT
                txtProdu=txtProdu+" "
            txtProdu=txtProdu+"  |"+array[1]+"\n"

    print(txtProdu)

