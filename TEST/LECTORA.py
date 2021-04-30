def ver2():
    array=[
            #DE   IZ  T|NT ID POS LIMITE
            #0   1   2   3        4
            [1, 'ε','S','A',    'NT'],
            [2, 'ε','A','0',    'T'],
            [3, 'ε','A','0 B 0','T;NT;T'],
            [4, 'ε','A','0 C 0','T;NT;T'],
            [5, 'ε','B','1',    'T'],
            [6, 'ε','B','1 D 1','T;NT;T'],
            [7, 'ε','C','2',    'T'],
            [8, 'ε','C','2 E 2','T;NT;T'],
            [9, 'ε','E','3',    'T'],
            [10, '0','0','ε',    'T'],
            [11,'1','1','ε',   'T'],
            [12,'2','2','ε',   'T'],
            [13,'3','3','ε',   'T']
            
        ]
    return array
def ver2M():
    array=[
            #DE   IZ  T|NT ID POS LIMITE
            #0   1   2   3        4
            [1, 'ε','S','A',    'NT'],
            #[2, 'ε','A','0',    'T'],
            [3, 'ε','A','0 B 0','T;NT;T'],
            [4, 'ε','A','0 C 0','T;NT;T'],
            [5, 'ε','B','1',    'T'],
            [6, 'ε','B','1 D 1','T;NT;T'],
            [7, 'ε','C','2',    'T'],
            [8, 'ε','C','2 E 2','T;NT;T'],
            [9, 'ε','E','3',    'T'],
            [10, '0','0','ε',    'T'],
            [11,'1','1','ε',   'T'],
            [12,'2','2','ε',   'T'],
            [13,'3','3','ε',   'T']
            
        ]
    return array
def funcion():
    #txt='02320'
    txt='02320'
    #produc=ver2()
    produc=ver2()
    A=[]
    for a in txt:
        A.append(a)

    #TESTEO DE PRODUCCIONES
    txtA=['0','2','3','2','0']#TXTARRAY
    txtAH=[]#TXT AYUDA
    pila=[]#PILA
    camino=[ ]#CAMINO
    produc2=ver2M()#PROUDCCIONES MODIFICADAS
    
            #buscar,arrayTxt,pila,ayudaTxt,camino,produccion,repetir,posicion 
           #(S    ,02320   ,[]  ,{}      ,()    ,[]         ,S      ,100)
    try:
        buscar('S'    ,A      ,['#']   ,[]      ,[]    ,produc     ,False    ,0)#INICIO
    except:
        print("OCURRIO UN ERROR ")
    #buscar('S'    ,txtA      ,pila   ,txtAH      ,camino    ,produc2     ,'N'    ,9)
def buscar(search,arrayTxt,pila,ayudarTxt,camino,producciones,repite,posicion):
    
    txt=''
    n=posicion

    if n<len(producciones):

        derecha=producciones[n][3].split(' ')
        izquierda=producciones[n][4].split(';')
        if search==producciones[n][2]:
            print('PRODUC',search,arrayTxt,pila,ayudarTxt,camino,repite,posicion)
            for num in range(len(producciones)):
                if num%2!=0:
                    txt=txt+str(producciones[num][0])+':'+str(producciones[num][2])+'->'+str(producciones[num][3])+'=:= '
                else:
                    txt=txt+str(producciones[num][0])+':'+str(producciones[num][2])+'->'+str(producciones[num][3])+'=:= '
                    print(txt)
                    txt=''

            if producciones[n][3]=='ε':

                if len(pila)==0:
                    print('ES==ε, pila vacia')
                else:
                    if len(arrayTxt)!=0:
                        if pila[0]==arrayTxt[0]:                 
                            pila.pop(0)
                            ayudarTxt.insert(0,arrayTxt.pop(0))
                            if len(pila)==0:

                                if len(arrayTxt)==0:
                                    print('ES==ε; pila llena,txt lleno; txt=pila; pila vacia, txt vacio')
                                    print(search,arrayTxt,pila,ayudarTxt,camino,repite,posicion)

                                else:
                                    print('ES==ε; pila llena,txt lleno; txt=pila; pila vacia, txt lleno')
                                    buscar('#',arrayTxt,pila,ayudarTxt,camino,producciones,True,len(producciones)-2)
                            else:

                                if len(arrayTxt)==0:
                                    print('ES==ε; pila llena,txt lleno; txt=pila; pila llena, txt vacio')      
                                else:
                                    print('ES==ε; pila llena,txt lleno; txt=pila; pila llena, txt lleno')
                                    buscar(pila[0],arrayTxt,pila,ayudarTxt,camino,producciones,repite,0)
                        else:
                            print('ES==ε; pila llena,txt lleno; txt!=pila')
                            buscar('#',arrayTxt,pila,ayudarTxt,camino,producciones,True,len(producciones)-2)
                    else:
                        print('ES==ε; pila llena,txt vacio; txt!=pila')

            else:
                print('ES!=ε')
                pila.pop(0)
                for num in derecha:
                    pila.insert(0,num)
                camino.append(producciones[n][2]+' '+str(producciones[n][0]))
                buscar(pila[0],arrayTxt,pila,ayudarTxt,camino,producciones,repite,0)
        else:
            print('NEXT->')
            buscar(search,arrayTxt,pila,ayudarTxt,camino,producciones,repite,n+1)
        #print(search,arrayTxt,pila,ayudarTxt,camino,producciones,repite)
    else:
        print('FIN',search,arrayTxt,pila,ayudarTxt,camino,repite,posicion)
        for num in range(len(producciones)):
            if num%2!=0:
                txt=txt+str(producciones[num][0])+':'+str(producciones[num][2])+'->'+str(producciones[num][3])+'=:= '
            else:
                txt=txt+str(producciones[num][0])+':'+str(producciones[num][2])+'->'+str(producciones[num][3])+'=:= '
                print(txt)
                txt='' 
        if repite==True:
            street=camino[len(camino)-1].split(' ')
            for pId in range(len(producciones)):
                if producciones[pId][2]==street[0] and int(producciones[pId][0])==int(street[1]):  
                    print('FIN T: ELMINANDO',camino[len(camino)-1])
                    tamaño=len(ayudarTxt)
                    producciones.pop(pId)
                    for num in range(tamaño):
                        arrayTxt.insert(0,ayudarTxt.pop(0))
                    camino.clear()
                    pId=len(producciones)+2
                    buscar('S',arrayTxt,['#'],[],camino,producciones,False,0)
                    break
            
        else:
            if len(arrayTxt)==0 and len(pila)==0:
                print('FIN F; txt vacio pila vacia')

            else:
                print('FIN F; txt lleno pila llena')
                street=camino[len(camino)-1].split(' ')
                for pId in range(len(producciones)):
                    if producciones[pId][2]==street[0] and int(producciones[pId][0])==int(street[1]):  
                        print('FIN T: ELMINANDO',camino[len(camino)-1])
                        tamaño=len(ayudarTxt)
                        producciones.pop(pId)
                        for num in range(tamaño):
                            arrayTxt.insert(0,ayudarTxt.pop(0))
                        camino.clear()
                        pId=len(producciones)+2
                        buscar('S',arrayTxt,['#'],[],camino,producciones,False,0)
                        break
def test():
    a=[1,2,3,4]
    Kk=[]
    tamaño=len(a)
    print(a,Kk,1)
    for b in range(tamaño):
        Kk.append(a.pop(0))
    print(a,Kk,2)
    for b in range(tamaño):
        a.append(Kk.pop(0))
    print(a,Kk,3)
#test()
funcion()
