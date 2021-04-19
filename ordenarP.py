def ordenar(producciones,Nt):
    print()
    #ORDENAR PRIMERO TERMINAELS NO TERMINALES EN S->B| a B en   S->a B|B
    array_salida=[]
    for nU in range(len(Nt)):#nU=numero uno; nD=n dos
        produTemp=[]
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
                               #S                  -> a W a
                produTemp.append([producciones[nD][0],producciones[nD][1],numero])
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
                array_salida.append([a[0],a[1],len(produTemp)])

    print(array_salida)