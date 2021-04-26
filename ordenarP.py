def ordenar(producciones,Nt,T):
    print()
    #ORDENAR SI LOS NO TERMINALES>
    #ORDENAR PRIMERO TERMINAELS NO TERMINALES EN S->B| a B en   S->a B|B
    array_salida=[]
    mayor=0#SABER QUIEN ES MAYOR
    if len(Nt)>len(T):
        mayor=len(Nt)
    else:
        mayor=len(T)
    
    for nU in range(len(Nt)):#nU=numero uno; nD=n dos
        produTemp=[]
        posicion=1
        for nD in range(len(producciones)):#ORDENA POR ORDEN DE NO TERMINALES
            if producciones[nD][0]==Nt[nU]:
                for nT in range(len(Nt)):
                    numero=0
                    derecha=producciones[nD][1].split(' ')#SEPARA POR a,W,a
                    #VEO SI ES TERMINAL O NO TERMINAL LA PRIMERA LETRA
                    if derecha[0]==Nt[nT]:#IF a==NT
                        numero=-1
                        break
                    else:#IF a==Terminal
                        numero=1
                        #nT=len(Nt)+1
                    #DONDE 1=TErminal;-1?No terminal     
                               #S                    ,a W a              ,0|1    ,posicion
                ter_Nter=''
                derecha=producciones[nD][1].split(' ')

                
                for b in range(len(derecha)):#PARA OBTENER EL a A a-> T NT T
                    for a in range(mayor):
                        if len(Nt)>a:#IF NO LLEGA AL LIMITE DEL NUMERO
                            if Nt[a]==derecha[b]:#PARA NO AGREGAR; FINAL
                                if len(derecha)-1>b:
                                    ter_Nter=ter_Nter+'NT'+';'
                                else:
                                    ter_Nter=ter_Nter+'NT' 
                                break
                        if len(T)>a:#IF NO LLEGA AL LIMITE DEL NUMEOR
                            if T[a]==derecha[b]:
                                if len(derecha)-1>b:#PARA NO AGREGAR; FINAL
                                    ter_Nter=ter_Nter+'T'+';'
                                else:
                                    ter_Nter=ter_Nter+'T'
                                break
                              
                #print(producciones[nD][1],ter_Nter)
                                #S                   ,a A a              ,veces, posicion, T NT T
                produTemp.append([producciones[nD][0],producciones[nD][1],numero,posicion,ter_Nter])
                posicion+=1
        #ORDNAR DE TERMINALES>NO TERMINALES
        array_uno=[]#AYUDA1
        array_dos=[]##AYUDA2
        for a in range(len(produTemp)):
            for b in range(len(produTemp)):
                if b+1<len(produTemp):##PARA MIRAR ANTES DEQUE CREO UN ERROR AL TOMAR LA ULTIMA MATRIZ
                    if produTemp[b][2]>produTemp[b+1][2]:#MIRANDO->ARRAY->Pos_NUMERO->numero
                         continue
                    else:
                        array_uno=produTemp[b]
                        array_dos=produTemp[b+1]
                        produTemp[b]=array_dos
                        produTemp[b+1]=array_uno

        for a in produTemp:#A,a A a,vesces que se repite
            if produTemp!=None:
                                    #A   ,a A a,T NT T,Tamaño     , posicion
                array_salida.append([a[0],a[1],a[4],len(produTemp),a[3]])

    print(array_salida)