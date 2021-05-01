import ordenarP as ordenarP
import transacciones as transacciones
import pasos as pasos
import pasosx2 as pasosx2
def table(array,palabra,TF):
    Nombre=array[0]
    NT=array[1]
    T=array[2]
    NTI=array[3]
    array_producciones=array[4]
    #print(array_producciones)
    #ordenar por prioridad de terminaels
    array_U=ordenarP.ordenar(array_producciones,NT,T)#ARRAY [S A NT]
    array_D=transacciones.transacciones(T,array_producciones,NTI)#ARRAY[ep,S,A,1]
    #print(array_U,'*******1')
    #print(array_D,'*******2')
    array_F=[]
    array_F2=[]
    Ids=1
    for Aa in array_U:
        for Ab in array_D:
            if Ab[0]=='ε' and Aa[0]==Ab[1] and Aa[1]==Ab[2]:
                array_F.append([Ids,Ab[0],Ab[1],Ab[2],Aa[2]])
                array_F2.append([Ids,Ab[0],Ab[1],Ab[2],Aa[2]])
        Ids+=1

    for Ab in array_D:
        if Ab[2]=='ε':
            array_F.append([Ids,Ab[0],Ab[1],Ab[2],'T'])
            array_F2.append([Ids,Ab[0],Ab[1],Ab[2],'T'])
            Ids+=1
    A=[]
    for a in palabra:
        A.append(a)
    #print(array_F)
    if TF==False:  
        pasos.buscar('S'    ,A      ,['#']   ,[]      ,[]    ,array_F     ,False    ,0)#INICIO
    else:
        pasosx2.buscar('S'    ,A      ,['#']   ,[]      ,[]    ,array_F     ,False    ,0,array_F2)#INICIO
    
    #print(array_F)

