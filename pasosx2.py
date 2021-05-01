
import webbrowser
import io
from graphviz import Digraph
def producir(producciones,arrayTxt,ARRAY):
    # for i in producciones:
    #     print(i)
    # print(arrayTxt)
    #print(producciones[0][2],'S')
    analizador(producciones[0][2],arrayTxt,['#'],producciones,0,ARRAY)

def buscar(search,arrayTxt,pila,ayudarTxt,camino,producciones,repite,posicion,A):
    
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
                                    producir(producciones,ayudarTxt,A)
                                else:
                                    buscar('#',arrayTxt,pila,ayudarTxt,camino,producciones,True,len(producciones)-2,A)
                            else:

                                if len(arrayTxt)==0:
                                    return      
                                else:
                                    buscar(pila[0],arrayTxt,pila,ayudarTxt,camino,producciones,repite,0,A)
                        else:
                            buscar('#',arrayTxt,pila,ayudarTxt,camino,producciones,True,len(producciones)-2,A)
                    else:
                        return

            else:
                pila.pop(0)
                for num in derecha:
                    pila.insert(0,num)
                camino.append(producciones[n][2]+' '+str(producciones[n][0]))
                buscar(pila[0],arrayTxt,pila,ayudarTxt,camino,producciones,repite,0,A)
        else:
            buscar(search,arrayTxt,pila,ayudarTxt,camino,producciones,repite,n+1,A)
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
                    buscar('S',arrayTxt,['#'],[],camino,producciones,False,0,A)
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
                        buscar('S',arrayTxt,['#'],[],camino,producciones,False,0,A)
                        break

textoHtml=[]

def analizador(search,arrayTxt,pila,producciones,posicion,A):
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
                                    #print('ES==ε; pila llena,txt lleno; txt=pila; pila vacia, txt vacio***??')
                                    # pilaTXT=''
                                    # for txt in pila:
                                    #     pilaTXT=pilaTXT+txt
                                    # pilaTXT=pilaTXT+'Ω'
                                    # entradaTxt=''
                                    # for txt in arrayTxt:
                                    #     entradaTxt=entradaTxt+txt
                                    # transiciones='q,'+str(producciones[n][1])+','+str(producciones[n][2])+',q,'+str(producciones[n][3].replace(' ',''))
                                    # textoHtml.append([pilaTXT,entradaTxt,transiciones])
                                    graph(textoHtml,A)
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
                                    #transiciones='q,'+str(producciones[n][1])+','+str(producciones[n][2])+',q,'+str(producciones[n][3].replace(' ',''))
                                    textoHtml.append([pilaTXT,entradaTxt,producciones[n][0]])
                                    analizador(pila[0],arrayTxt,pila,producciones,0,A)
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
                #transiciones='q,'+str(producciones[n][1])+','+str(producciones[n][2])+',q,'+str(producciones[n][3].replace(' ',''))
                textoHtml.append([pilaTXT,entradaTxt,producciones[n][0]])
                analizador(pila[0],arrayTxt,pila,producciones,0,A)
                
        else:
            analizador(search,arrayTxt,pila,producciones,n+1,A)

def graph(array,producciones):
    #graph2(array,producciones)
    #graph3(array,producciones)
    #print(array)
    #print(producciones)
    numero=2
    texto1='ε,ε;Ω'
    texto2='ε,ε;'+producciones[0][2]
    texto3='ε,Ω;ε'
    for uno in array:
        txtU="""<<TABLE BORDER="0" CELLBORDER="0.1">"""
        txtD="""<<TABLE BORDER="0" CELLBORDER="0.1">"""
        for dos in producciones:
            if dos[1]=='ε':
                if uno[2]==dos[0]:#COLOR ROJO
                    txtU=txtU+"""<TR><TD><font color="red">"""+dos[1]+","+dos[2]+";"+dos[3].replace(' ','')+"""</font></TD></TR>"""
                else:
                    txtU=txtU+"""<TR><TD><font color="black">"""+dos[1]+","+dos[2]+";"+dos[3].replace(' ','')+"""</font></TD></TR>"""
            else:
                if uno[2]==dos[0]:#COLOR ROJO
                    txtD=txtD+"""<TR><TD><font color="red">"""+dos[1]+","+dos[2]+";"+dos[3].replace(' ','')+"""</font></TD></TR>"""
                else:
                    txtD=txtD+"""<TR><TD><font color="black">"""+dos[1]+","+dos[2]+";"+dos[3].replace(' ','')+"""</font></TD></TR>"""
        txtU=txtU+"</TABLE>>"
        txtD=txtD+"</TABLE>>"

        dot1 = Digraph(comment='SI',format='png')
        dot1.graph_attr['rankdir'] = 'LR'
        dot1.node('I', 'I')
        dot1.node('P', 'P')
        dot1.node('Q', 'Q',fixedsize="true",width="1.5",height="1.5",fillcolor='yellow',style='filled')
        dot1.node('F', 'F',peripheries="2")
        dot1.edge('I', 'P',label=texto1)
        dot1.edge('P', 'Q',label=texto2)
        dot1.edge('Q', 'F',label=texto3)
        dot1.edge('Q:n','Q:n',label=txtU,color="black")
        dot1.edge('Q:s','Q:s',label=txtD,color="black",constraint="false")
        dot1.render('IMG/a'+str(numero))
        numero+=1

    #graph3(array,producciones,numero)
    #graph4(array,producciones,numero)
    html(array,producciones)


def graph2(array,producciones):
    texto1="""<font color="black">ε,ε;Ω</font>"""
    texto2='ε,ε;'+producciones[0][2]
    texto3='ε,Ω;ε'
    txtU="""<<TABLE BORDER="0" CELLBORDER="0.1">"""
    txtD="""<<TABLE BORDER="0" CELLBORDER="0.1">"""
    for dos in producciones:
        if dos[1]=='ε':
            txtU=txtU+"""<TR><TD><font color="black">"""+dos[1]+","+dos[2]+";"+dos[3].replace(' ','')+"""</font></TD></TR>"""
        else:
            txtD=txtD+"""<TR><TD><font color="black">"""+dos[1]+","+dos[2]+";"+dos[3].replace(' ','')+"""</font></TD></TR>"""
    txtU=txtU+"</TABLE>>"
    txtD=txtD+"</TABLE>>"

    dot2 = Digraph(comment='SI',format='png')
    dot2.graph_attr['rankdir'] = 'LR'
    dot2.node('I', 'I',fillcolor='yellow',style='filled')
    dot2.node('P', 'P')
    dot2.node('Q', 'Q',fixedsize="true",width="1.5",height="1.5")
    dot2.node('F', 'F',peripheries="2")
    dot2.edge('I', 'P',label=texto1)
    dot2.edge('P', 'Q',label=texto2)
    dot2.edge('Q', 'F',label=texto3)
    dot2.edge('Q:n','Q:n',label=txtU,color="black")
    dot2.edge('Q:s','Q:s',label=txtD,color="black",constraint="false")
    dot2.render('IMG/a0')

def graph3(array,producciones):
    #print(array)
    #print(producciones)
    texto1="""ε,ε;Ω"""
    texto2="""<font color="black">ε,ε;"""+producciones[0][2]+"""</font>"""
    texto3='ε,Ω;ε'
    numero=2
    txtU="""<<TABLE BORDER="0" CELLBORDER="0.1">"""
    txtD="""<<TABLE BORDER="0" CELLBORDER="0.1">"""
    for dos in producciones:
        if dos[1]=='ε':
            txtU=txtU+"""<TR><TD><font color="black">"""+dos[1]+","+dos[2]+";"+dos[3].replace(' ','')+"""</font></TD></TR>"""
        else:
            txtD=txtD+"""<TR><TD><font color="black">"""+dos[1]+","+dos[2]+";"+dos[3].replace(' ','')+"""</font></TD></TR>"""
    txtU=txtU+"</TABLE>>"
    txtD=txtD+"</TABLE>>"

    dot3 = Digraph(comment='SI',format='png')
    dot3.graph_attr['rankdir'] = 'LR'
    dot3.node('I', 'I')
    dot3.node('P', 'P',fillcolor='yellow',style='filled')
    dot3.node('Q', 'Q',fixedsize="true",width="1.5",height="1.5")
    dot3.node('F', 'F',peripheries="2")
    dot3.edge('I', 'P',label=texto1)
    dot3.edge('P', 'Q',label=texto2)
    dot3.edge('Q', 'F',label=texto3)
    dot3.edge('Q:n','Q:n',label=txtU,color="black")
    dot3.edge('Q:s','Q:s',label=txtD,color="black",constraint="false")
    dot3.render('IMG/a'+str(1))

def graph4(array,producciones,numero):

    #print(array)
    #print(producciones)
    texto1="""ε,ε;Ω"""
    texto2="""ε,ε;"""+producciones[0][2]+""""""
    texto3="""<font color="black">ε,Ω;ε</font>"""
    numero=2
    txtU="""<<TABLE BORDER="0" CELLBORDER="0.1">"""
    txtD="""<<TABLE BORDER="0" CELLBORDER="0.1">"""
    for dos in producciones:
        if dos[1]=='ε':
            txtU=txtU+"""<TR><TD><font color="black">"""+dos[1]+","+dos[2]+";"+dos[3].replace(' ','')+"""</font></TD></TR>"""
        else:
            txtD=txtD+"""<TR><TD><font color="black">"""+dos[1]+","+dos[2]+";"+dos[3].replace(' ','')+"""</font></TD></TR>"""
    txtU=txtU+"</TABLE>>"
    txtD=txtD+"</TABLE>>"

    dot4 = Digraph(comment='SI',format='png')
    dot4.graph_attr['rankdir'] = 'LR'
    dot4.node('I', 'I')
    dot4.node('P', 'P')
    dot4.node('Q', 'Q',fixedsize="true",width="1.5",height="1.5",fillcolor='yellow',style='filled')
    dot4.node('F', 'F',peripheries="2")
    dot4.edge('I', 'P',label=texto1)
    dot4.edge('P', 'Q',label=texto2)
    dot4.edge('Q', 'F',label=texto3)
    dot4.edge('Q:n','Q:n',label=txtU,color="black")
    dot4.edge('Q:s','Q:s',label=txtD,color="black",constraint="false")
    dot4.render('IMG/a'+str(numero))

def html(array,producciones):
    f = open('muestra.html','w',newline='',encoding="utf-8")
    num=2
    texto=''
    for txt in array:
        texto=texto+"""<body class="cont"><div class="container"><div class="row"><div class="col-md-6"><p class="Titulo">ITERACION:""" +str(num)+"""</p>"""
        texto=texto+"""<table class="table table-dark"><tbody><tr><th scope="row">Pila</th><td>"""+txt[0]+"""</tr><tr><th scope="row">Entrada</th><td>"""+txt[1]+"""</td></tr></tbody></table></div><div class="col-md-6">"""
        texto=texto+"""<img src="IMG/a"""+str(num)+""".png" class="img-fluid"></div></div></div></div>  """
        num+=1
    principal= """
<!DOCTYPE html>
<html lang="es">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<link rel="stylesheet" href="css/cssAut.css">
<link rel="stylesheet" href="boos/bootstrap.css">

<link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Abril+Fatface&family=Glegoo&display=swap" rel="stylesheet">

<title>Document</title>
</head>

  """
    fin=""" 
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
    webbrowser.open_new_tab('muestra.html')