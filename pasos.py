
import webbrowser
import io
def producir(producciones,arrayTxt):
    # for i in producciones:
    #     print(i)
    # print(arrayTxt)
    #print(producciones[0][2],'S')
    analizador(producciones[0][2],arrayTxt,['#'],producciones,0)

def buscar(search,arrayTxt,pila,ayudarTxt,camino,producciones,repite,posicion):
    
    txt=''
    n=posicion

    if n<len(producciones):

        derecha=producciones[n][3].split(' ')
        izquierda=producciones[n][4].split(';')
        if search==producciones[n][2]:

            if producciones[n][3]=='ε':

                if len(pila)==0:
                    #print('ES==ε, pila vacia')
                    return
                else:
                    if len(arrayTxt)!=0:
                        if pila[0]==arrayTxt[0]:                 
                            pila.pop(0)
                            ayudarTxt.insert(0,arrayTxt.pop(0))
                            if len(pila)==0:

                                if len(arrayTxt)==0:
                                    producir(producciones,ayudarTxt)
                                else:
                                    buscar('#',arrayTxt,pila,ayudarTxt,camino,producciones,True,len(producciones)-2)
                            else:

                                if len(arrayTxt)==0:
                                    return      
                                else:
                                    buscar(pila[0],arrayTxt,pila,ayudarTxt,camino,producciones,repite,0)
                        else:
                            buscar('#',arrayTxt,pila,ayudarTxt,camino,producciones,True,len(producciones)-2)
                    else:
                        return

            else:
                pila.pop(0)
                for num in derecha:
                    pila.insert(0,num)
                camino.append(producciones[n][2]+' '+str(producciones[n][0]))
                buscar(pila[0],arrayTxt,pila,ayudarTxt,camino,producciones,repite,0)
        else:
            buscar(search,arrayTxt,pila,ayudarTxt,camino,producciones,repite,n+1)
    else:
        if repite==True:
            street=camino[len(camino)-1].split(' ')
            for pId in range(len(producciones)):
                if producciones[pId][2]==street[0] and int(producciones[pId][0])==int(street[1]):  
                    #print('FIN T: ELMINANDO',camino[len(camino)-1])
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
                #print('FIN F; txt vacio pila vacia')
                return producciones
            else:
                #print('FIN F; txt lleno pila llena')
                street=camino[len(camino)-1].split(' ')
                for pId in range(len(producciones)):
                    if producciones[pId][2]==street[0] and int(producciones[pId][0])==int(street[1]):  
                        #print('FIN T: ELMINANDO',camino[len(camino)-1])
                        tamaño=len(ayudarTxt)
                        producciones.pop(pId)
                        for num in range(tamaño):
                            arrayTxt.insert(0,ayudarTxt.pop(0))
                        camino.clear()
                        pId=len(producciones)+2
                        buscar('S',arrayTxt,['#'],[],camino,producciones,False,0)
                        break

textoHtml=[]

def analizador(search,arrayTxt,pila,producciones,posicion):
    txt=''
    n=posicion
    if n<len(producciones):
        derecha=producciones[n][3].split(' ')
        if search==producciones[n][2]:
            #print('PRODUC',search,arrayTxt,pila,posicion)
            if producciones[n][3]=='ε':
                if len(pila)==0:
                    print('ES==ε, pila vacia')
                else:
                    if len(arrayTxt)!=0:
                        if pila[0]==arrayTxt[0]:
                            #print('DOS')                 
                            pila.pop(0)
                            arrayTxt.pop(0)
                            if len(pila)==0:
                                if len(arrayTxt)==0:
                                    print('ES==ε; pila llena,txt lleno; txt=pila; pila vacia, txt vacio***??')
                                    # pilaTXT=''
                                    # for txt in pila:
                                    #     pilaTXT=pilaTXT+txt
                                    # pilaTXT=pilaTXT+'Ω'
                                    # entradaTxt=''
                                    # for txt in arrayTxt:
                                    #     entradaTxt=entradaTxt+txt
                                    # transiciones='q,'+str(producciones[n][1])+','+str(producciones[n][2])+',q,'+str(producciones[n][3].replace(' ',''))
                                    # textoHtml.append([pilaTXT,entradaTxt,transiciones])
                                    html(textoHtml)
                                else:
                                    print('ES==ε; pila llena,txt lleno; txt=pila; pila vacia, txt lleno')
                                    return 4
                            else:

                                if len(arrayTxt)==0:
                                    print('ES==ε; pila llena,txt lleno; txt=pila; pila llena, txt vacio')
                                    return 5 
                                else:
                                    #print('ES==ε; pila llena,txt lleno; txt=pila; pila llena, txt lleno')
                                    # cola.append(threading.Thread(target=analizador,args=(AQueue[contador],pila[0],i,arrayTxt,pila,camino,producciones,0)))
                                    pilaTXT=''
                                    for txt in pila:
                                        pilaTXT=pilaTXT+txt
                                    pilaTXT=pilaTXT+'Ω'
                                    entradaTxt=''
                                    for txt in arrayTxt:
                                        entradaTxt=entradaTxt+txt
                                    transiciones='q,'+str(producciones[n][1])+','+str(producciones[n][2])+',q,'+str(producciones[n][3].replace(' ',''))
                                    textoHtml.append([pilaTXT,entradaTxt,transiciones])
                                    analizador(pila[0],arrayTxt,pila,producciones,0)
            else:
                #print('ES!=ε')
                #print(pila,': antes-------',arrayTxt)
                pila.pop(0)
                for num in reversed(range(len(derecha))):
                    pila.insert(0,derecha[num])
                # cola.append(threading.Thread(analizador(AQueue[contador],pila[0],i,arrayTxt,pila,camino,producciones,0)))
                pilaTXT=''
                for txt in pila:
                    pilaTXT=pilaTXT+txt
                pilaTXT=pilaTXT+'Ω'
                entradaTxt=''
                for txt in arrayTxt:
                    entradaTxt=entradaTxt+txt
                transiciones='q,'+str(producciones[n][1])+','+str(producciones[n][2])+',q,'+str(producciones[n][3].replace(' ',''))
                textoHtml.append([pilaTXT,entradaTxt,transiciones])
                analizador(pila[0],arrayTxt,pila,producciones,0)
                
        else:
            analizador(search,arrayTxt,pila,producciones,n+1)

def html(array):
    f = open('Tabla.html','w',newline='',encoding="utf-8")
    texto=''
    texto=texto+'<tr>'+'<th scope="row">0</th>'+'<td></td>'+'<td>'+array[0][1]+'</td>'+'<td>(i, ε, ε;p,Ω)</td>'+'</tr>'
    texto=texto+'<tr>'+'<th scope="row">1</th>'+'<td>Ω</td>'+'<td>'+array[0][1]+'</td>'+'<td>(p, ε, ε;q,'+array[0][0].replace('Ω','')+')</td>'+'</tr>'
    id=2
    for txt in array:
        texto=texto+'<tr>'+'<th scope="row">'+str(id)+'</th>'+'<td>'+txt[0]+'</td>'+'<td>'+txt[1]+'</td>'+'<td>'+txt[2]+'</td>'+'</tr>'
        id+=1
    texto=texto+'<tr>'+'<th scope="row">'+str(id)+'</th>'+'<td>Ω</td>'+'<td>ε</td>'+'<td>(q,Ω,ε;f,ε)</td>'+'</tr>'
    texto=texto+'<tr>'+'<th scope="row">'+str(id+1)+'</th>'+'<td>ε</td>'+'<td>ε</td>'+'<td>f</td>'+'</tr>'
    principal= """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <link rel="stylesheet" href="css/cssAut.css">
    <link rel="stylesheet" href="boos/bootstrap.css">

    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Abril+Fatface&family=Glegoo&display=swap" rel="stylesheet">
    <title>Document</title>
</head>

<body class="cont">
    <table class="table table-striped">
        <thead>
          <tr>
            <th scope="col">Iteracion</th>
            <th scope="col">Pila</th>
            <th scope="col">Entrada</th>
            <th scope="col">Transaccion</th>
          </tr>
        </thead>
        <tbody>
  """
    fin="""
        </tbody>
      </table>
</body>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>
</html>
  """
    cuerpo=texto
    #print(cuerpo)
    f.write(principal)#inicio
    f.write(cuerpo)#medio
    f.write(fin)#final
    f.close()#cerar
    webbrowser.open_new_tab('Tabla.html')