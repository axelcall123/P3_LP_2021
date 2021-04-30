import threading
import queue
from threading import Thread
def analizador(search,ID,arrayTxt,pila,camino,producciones):
    if len(pila)<=len(arrayTxt):
        for n in range(len(producciones)):
            txt=''
            derecha=producciones[n][2].split(' ')
            #SIRVE PARA VER DONDE VOY XD
            if search==producciones[n][1] and ID==producciones[n][-1]:
                print('PRODUC',search,ID,arrayTxt,pila,camino,n)
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
                                        #HILOS Y COLAS
                                        cola=[]
                                        # AQueue=[]
                                        # for i in buscarID:#RESPUESTAS
                                        #     AQueue.append(queue.Queue())
                                        # contador=0
                                        for i in buscarID:#HILOS
                                            cola.append(threading.Thread(target=analizador,args=(pila[0],i,arrayTxt,pila,camino,producciones)))
                                            # analizador(pila[0],i,arrayTxt,pila,camino,producciones)
                                            print('RAMAS:?1',pila[0],i,arrayTxt,',',pila,',',camino)
                                            # contador+=1
                                        # salida.put(500)
                                        # Retornos=[]
                                        # # print(cola,'\n',AQueue)
                                        for ids in range(len(cola)):
                                        #     print(cola[i],AQueue[i],'????X1')
                                            cola[ids].start()
                                            cola[ids].join()
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
                    #HILOS Y COLAS
                    cola=[]
                    # AQueue=[]
                    # for i in buscarID:#RESPUESTAS
                    #     AQueue.append(queue.Queue())
                    # contador=0
                    for i in buscarID:#HILOS
                        cola.append(threading.Thread(target=analizador,args=(pila[0],i,arrayTxt,pila,camino,producciones)))
                        #  analizador(pila[0],i,arrayTxt,pila,camino,producciones)
                        print('RAMAS:?2',pila[0],i,arrayTxt,',',pila,',',camino,0)
                        # contador+=1
                    # Retornos=[]
                    for numeros in range(len(cola)):
                    #     print(cola[i],AQueue[i],'????X2')
                        cola[numeros].start()
                    #     print(numeros,'****=')
                        cola[numeros].join()
                    #     Retornos.append(AQueue[i].get())
                    # salida.put(Retornos)
                    #print(Retornos,'::::')