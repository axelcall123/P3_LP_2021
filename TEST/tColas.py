
import threading
import queue
from threading import Thread
import colas as colas

def funcion():
    cola=[]
    respuesta=[]
    txt=[]
    for a in range(3):
        respuesta.append(queue.Queue())
    for a in range(3):
        cola.append(threading.Thread(vecesxd(respuesta[a],chr(ord('A')+a))))  
    for a in range(len(cola)):
        cola[a].start()
        cola[a].join()
        txt.append(respuesta[a].get())
    print(txt)
    # que1 = queue.Queue()
    # hilo1=threading.Thread(vecesxd(que1,'A'))
    # hilo1.start()
    # hilo1.join()
    # retorno1=que1.get()
    # que2 = queue.Queue()
    # hilo2=threading.Thread(vecesxd(que2,'B'))
    # hilo2.start()
    # hilo2.join()
    # retorno2=que2.get()
    # que3 = queue.Queue()
    # hilo3=threading.Thread(vecesxd(que3,'C'))
    # hilo3.start()
    # hilo3.join()
    # retorno3=que3.get()
    # print(retorno1,retorno2,retorno3)
         
def vecesxd(salida,ID):
    #holas = queue.Queue()
        # que1 = queue.Queue()
        # que2 = queue.Queue()
        # que3 = queue.Queue()
        # hilo1=threading.Thread(veces(que1,'K'+ID))
        # hilo2=threading.Thread(veces(que2,'K'+ID))
        # hilo3=threading.Thread(veces(que3,'D'+ID))
        # hilo1.start()
        # hilo1.join()
        # retorno1=que1.get()
        # hilo2.start()
        # hilo2.join()
        # retorno2=que2.get()
        # hilo3.start()
        # hilo3.join()
        # retorno3=que3.get()
        # salida.put([retorno1,retorno2,retorno3])
    cola=[]
    respuesta=[]
    txt=[]
    for a in range(3):
        respuesta.append(queue.Queue())
    for a in range(3):
        cola.append(threading.Thread(veces(respuesta[a],chr(ord('K')+a)+ID)))
    for a in range(len(cola)):
        cola[a].start()
        cola[a].join()
        txt.append(respuesta[a].get())
    salida.put(txt)

def veces(salida,ID):
    for a in range(10):
        print(a,ID)
        salida.put(ID+str(a))

def ori():
    array=[
           #0   1   2   3  4 5
           #ID,    ,iz,de,rep,numero
            ['ε','S','A',1],
            ['ε','A','B',1],
            ['ε','A','a A a',2],
            ['ε','B','C',1],
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
    txt='abzba'
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
    #que = queue.Queue()
    hiloP=threading.Thread(target=colas.analizador,args=('B',1,['z', 'b', 'a'] , ['B', 'b', 'a'] , ['S 1', 'A 2', 'A 1', 'B 2'],produc))#INICIO
    #analizador('B',1,['z', 'b', 'a'] , ['B', 'b', 'a'] , ['S 1', 'A 2', 'A 1', 'B 2'],produc,0)
    #colas.analizador('B',1,['z', 'b', 'a'] , ['C', 'b', 'a'] , ['S 1', 'A 2', 'A 1', 'B 2'],produc)
    hiloP.start()
    hiloP.join()
    #retorno = que.get()
    #print(retorno,'END')
    #except:
    #print("DEMASIADAS ITERACIONES")
def analizador(search,ID,arrayTxt,pila,camino,producciones,posicion):
#def analizador(salida,search,ID,arrayTxt,pila,camino,producciones,posicion):    
    txt=''
    n=posicion
    if len(pila)>len(arrayTxt):
        return 1 
    else:
        if n<len(producciones):

            derecha=producciones[n][2].split(' ')
            #SIRVE PARA VER DONDE VOY XD
            if search==producciones[n][1] and ID==producciones[n][-1]:
                print('PRODUC',search,ID,arrayTxt,pila,camino,posicion)
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
                        return 2
                    else:
                        if len(arrayTxt)!=0:
                            print('holis')
                            if pila[0]==arrayTxt[0]:                 
                                pila.pop(0)
                                arrayTxt.pop(0)
                                if len(pila)==0:
                                    if len(arrayTxt)==0:
                                        print('ES==ε; pila llena,txt lleno; txt=pila; pila vacia, txt vacio***??')
                                        return 300

                                    else:
                                        print('ES==ε; pila llena,txt lleno; txt=pila; pila vacia, txt lleno')
                                        return 4
                                else:

                                    if len(arrayTxt)==0:
                                        print('ES==ε; pila llena,txt lleno; txt=pila; pila llena, txt vacio')
                                        return 5 
                                    else:
                                        print('ES==ε; pila llena,txt lleno; txt=pila; pila llena, txt lleno')
                                        #BUSCO EL ID HA DONDE MANDARLO XD
                                        #PARA CREA HILOS
                                        buscarID=[]
                                        for i in range(len(producciones)):
                                            if producciones[i][1]==pila[0]:
                                                buscarID.append(producciones[i][-1])
                                        #print(pila,': despues-----',arrayTxt)
                                        #HILOS Y COLAS
                                        # cola=[]
                                        # AQueue=[]
                                        # for i in buscarID:#RESPUESTAS
                                        #     AQueue.append(queue.Queue())
                                        # contador=0
                                        for i in buscarID:#HILOS
                                            # cola.append(threading.Thread(target=analizador,args=(AQueue[contador],pila[0],i,arrayTxt,pila,camino,producciones,0)))
                                            # analizador(pila[0],i,arrayTxt,pila,camino,producciones,0)
                                            print('RAMAS:?1',pila[0],i,arrayTxt,',',pila,',',camino,0)
                                            # contador+=1
                                        # salida.put(500)
                                        # Retornos=[]
                                        # # print(cola,'\n',AQueue)
                                        # for i in range(len(cola)):
                                        #     print(cola[i],AQueue[i],'????X1')
                                        #     cola[i].start()
                                        #     cola[i].join()
                                        #     Retornos.append(AQueue[i].get())
                                        # salida.put(Retornos)
                            else:
                                print('ES==ε; pila llena,txt lleno; txt!=pila')
                                return 7
                        else:
                            print('ES==ε; pila llena,txt vacio; txt!=pila')
                            return 8

                else:
                    print('ES!=ε')
                    #print(pila,': antes-------',arrayTxt)
                    pila.pop(0)
                    for num in reversed(range(len(derecha))):
                        pila.insert(0,derecha[num])
                    camino.append(producciones[n][1]+' '+str(producciones[n][-1]))
                    #BUSCO EL ID HA DONDE MANDARLO XD
                    #PARA CREA HILOS
                    buscarID=[]
                    for i in range(len(producciones)):
                        if producciones[i][1]==pila[0]:
                            buscarID.append(producciones[i][-1])
                    #print(pila,': despues-----',arrayTxt)
                    #HILOS Y COLAS
                    cola=[]
                    # AQueue=[]
                    # for i in buscarID:#RESPUESTAS
                    #     AQueue.append(queue.Queue())
                    # contador=0
                    for i in buscarID:#HILOS
                        # cola.append(threading.Thread(analizador(AQueue[contador],pila[0],i,arrayTxt,pila,camino,producciones,0)))
                        #analizador(pila[0],i,arrayTxt,pila,camino,producciones,0)
                        print('RAMAS:?2',pila[0],i,arrayTxt,',',pila,',',camino,0)
                        # contador+=1
                    # Retornos=[]
                    # for i in range(len(cola)):
                    #     print(cola[i],AQueue[i],'????X2')
                    #     cola[i].start()
                    #     cola[i].join()
                    #     Retornos.append(AQueue[i].get())

                    # salida.put(Retornos)
                    #print(Retornos,'::::')

            else:
                #print('NEXT->')
                analizador(search,ID,arrayTxt,pila,camino,producciones,n+1)
                #analizador(salida,search,ID,arrayTxt,pila,camino,producciones,n+1)
        else:
            print('FIN',search,ID,arrayTxt,pila,camino,posicion)
            return 9

funcionx2()

