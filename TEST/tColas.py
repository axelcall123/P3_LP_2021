
import threading
import queue
from threading import Thread


# def stringFunction(value, out_queue):
#     my_str = "This is string no. " + value
#     out_queue.put(my_str)

# my_queue = queue.Queue()
# thread1 = threading.Thread(stringFunction("one", my_queue))
# thread1.start()
# thread1.join()

# func_value = my_queue.get()
# print(func_value)

def funcion():
    array=[]
    #array.append(threading.Thread(target=veces,args=('a',0)))
    #array.append(threading.Thread(target=veces,args=('b',0)))
    #array.append(threading.Thread(target=veces,args=('c',0)))
    #array.append(threading.Thread(target=veces,args=('d',0)))
    #for inicio in array:
    #    inicio.start()

    #for a in range(2):
    #    array.append(veces('a'+str(a)))


    # hilo1= threading.Thread(target=veces,args=('a',0))
    # hilo2= threading.Thread(target=veces,args=('b',0))
    # hilo1.start()
    # hilo2.start()


    #veces('A',20,True,2)
    #veces('B',20,False,0)
    que = queue.Queue()
    array.append(threading.Thread(target=veces,args=(que,'A',20,True,2)))
    array.append(threading.Thread(target=veces,args=(que,'B',20,False,0)))

    for inicio in array:
        inicio.start()
        inicio.join()
        retorno = que.get()
        print(str(retorno),'ES EL RETORN')
        if retorno=='siii':
            print('YES')
        
def veces(salida,letra,a,TF,vv):
    if TF==True:
        for num in range(vv):
            letra=letra+letra
            a=a*2
            TF=False
            veces(salida,letra,a,TF,0)
    else:
        for num in range(a):
            print(letra,str(num))
            if num==10:
                salida.put('siii')
def ori():
    array=[
           #0   1   2   3  4 5
           #ID,    ,iz,de,rep,numero
            ['ε','S','A',1],
            ['ε','A','B',1],
            ['ε','A','a A a',2],
            ['ε','B','C','NT',1],
            ['ε','B','b B b',2],
            ['ε','C','z C',1],
            ['ε','C','z',2],
            ['a','a','ε',0],
            ['b','b','ε',0],
            ['c','c','ε',0],
            ['z','z','ε',0]
        ]
    return array
def funcionx2():
    #txt='02320'
    txt='abzba'
    #produc=ver2()
    produc=ori()
    A=[]
    for a in txt:
        A.append(a)

    #TESTEO DE PRODUCCIONES
    txtA=['a','b','z','b','a']#TXTARRAY
    txtAH=[]#TXT AYUDA
    pila=[]#PILA
    camino=[ ]#CAMINO
    produc2=ori()#PROUDCCIONES MODIFICADAS
            #analizador,arrayTxt,pila,camino,produccion,repetir,posicion 
               #(S    ,02320   ,[]  ,()    ,[]         ,S      ,100)
    #try:
    analizador('S'    ,1,A      ,['#']   ,[]    ,produc     ,False    ,0)#INICIO
    #except:
    #print("DEMASIADAS ITERACIONES")

def analizador(search,ID,arrayTxt,pila,camino,producciones,repite,posicion):
    
    txt=''
    n=posicion

    if n<len(producciones):

        derecha=producciones[n][2].split(' ')
        if search==producciones[n][1] and ID==producciones[n][-1]:
            print('PRODUC',search,ID,arrayTxt,pila,camino,repite,posicion)
            for num in range(len(producciones)):
                if num%2!=0:
                    txt=txt+str(producciones[num][-1])+':'+str(producciones[num][1])+'->'+str(producciones[num][2])+'=:= '
                else:
                    txt=txt+str(producciones[num][-1])+':'+str(producciones[num][1])+'->'+str(producciones[num][2])+'=:= '
                    print(txt)
                    txt=''
            
            if producciones[n][2]=='ε':
                if len(pila)==0:
                    print('ES==ε, pila vacia')
                else:
                    if len(arrayTxt)!=0:
                        if pila[0]==arrayTxt[0]:                 
                            pila.pop(0)
                            arrayTxt.pop(0)
                            if len(pila)==0:
                                if len(arrayTxt)==0:
                                    print('ES==ε; pila llena,txt lleno; txt=pila; pila vacia, txt vacio')
                                    return 'S'
                                    #print(search,arrayTxt,pila,ayudarTxt,camino,repite,posicion)

                                else:
                                    print('ES==ε; pila llena,txt lleno; txt=pila; pila vacia, txt lleno')
                                    return 'F'
                                    #analizador('#',arrayTxt,pila,ayudarTxt,camino,producciones,True,len(producciones)-2)
                            else:

                                if len(arrayTxt)==0:
                                    print('ES==ε; pila llena,txt lleno; txt=pila; pila llena, txt vacio')
                                    return 'F'      
                                else:
                                    print('ES==ε; pila llena,txt lleno; txt=pila; pila llena, txt lleno')
                                    return 'HIJOLES'
                                    #analizador(pila[0],arrayTxt,pila,ayudarTxt,camino,producciones,repite,0)
                        else:
                            print('ES==ε; pila llena,txt lleno; txt!=pila')
                            return 'F'
                    else:
                        print('ES==ε; pila llena,txt vacio; txt!=pila')
                        return 'F'

            else:
                print('ES!=ε')
                pila.pop(0)
                for num in reversed(range(len(derecha))):
                    pila.insert(0,derecha[num])
                camino.append(producciones[n][1]+' '+str(producciones[n][-1]))
                buscarID=[]
                cola=[]
                que = queue.Queue()
                for i in range(len(producciones)):
                    if producciones[i][1]==pila[0]:
                        buscarID.append(producciones[i][-1])
                        
                for i in buscarID:
                    cola.append(threading.Thread(target=analizador,args=(pila[0],i,arrayTxt,pila,camino,producciones,repite,0)))
                    print('RAMAS:',pila[0],i,arrayTxt,pila,camino,repite,0)

                for i in cola:
                    i.start()
                    i.join()
        else:
            #print('NEXT->')
            analizador(search,ID,arrayTxt,pila,camino,producciones,repite,n+1)
            #print(search,arrayTxt,pila,ayudarTxt,camino,producciones,repite)
    else:
        print('FIN',search,ID,arrayTxt,pila,camino,repite,posicion)

funcionx2()