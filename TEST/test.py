from graphviz import Digraph
def grap():
    lb1="""<
    <TABLE BORDER="0" CELLBORDER="0.1">
    <TR><TD><font color="red">Ω</font></TD></TR>
    <TR><TD><font color="black">2</font></TD></TR>
    <TR><TD><font color="black">3</font></TD></TR>
    <TR><TD><font color="black">4</font></TD></TR>
    <TR><TD><font color="black">5</font></TD></TR>
    <TR><TD><font color="black">6</font></TD></TR>
    </TABLE>
    >"""
    lb2="""<
    <TABLE BORDER="0" CELLBORDER="0.1">
    <TR><TD><font color="black">a</font></TD></TR>
    <TR><TD><font color="black">b</font></TD></TR>
    <TR><TD><font color="black">c</font></TD></TR>
    <TR><TD><font color="black">a</font></TD></TR>
    <TR><TD><font color="black">b</font></TD></TR>
    <TR><TD><font color="black">c</font></TD></TR>
    </TABLE>
    >"""
    dot = Digraph(comment='SI',format='png')
    dot.graph_attr['rankdir'] = 'LR'
    dot.node('I', 'I',fillcolor='yellow',style='filled')
    dot.node('P', 'P')
    dot.node('Q', 'Q',fixedsize="true",width="1.5",height="1.5")
    dot.node('F', 'F',peripheries="2")
    dot.edge('I', 'P',label='1')
    dot.edge('P', 'Q',label='2')
    dot.edge('Q', 'F',label='3')
    dot.edge('Q:n','Q:n',label=lb1,color="red")
    dot.edge('Q:s','Q:s',label=lb2,color="black",constraint="false")#Q:s sirve para que vaya abajo | n,s,e,o
    
    print(dot.source) 
    dot.render('PDF/test', view=True)
#TESTEO---------------------
#DERECHA,IZQUIERDA,T_NT,POSICION,LIMITE



def asd():
    NT=['S','A','B','C']
    T=['a','b','z','d']
    #recurisvo(0,'S','0')  

    arrayT=[]
    producciones=ver2()

    txt='02320'
    txtA=[]
    txtV=[]
    for t in txt:
        txtA.append(t)

    
    #recursivox2('S',txtA,[],txtV,producciones,0,-1)

def funcion():
    array=['3', '2', '0']
    arrayH=['2', '0']
    print(array,arrayH)
    tamaño=len(arrayH)
    for num in range(tamaño):
        array.insert(0, arrayH.pop(0))
    print(array,arrayH)
 
def recurisvo(a,pIzquierda,txt):
    producciones=ver()
    pLEFT=producciones[a][1].split(' ')
    pRigth=producciones[a][2].split(';')
    #print(a,len(producciones))
    print(a,pIzquierda,txt,producciones[a])
    if a<len(producciones)-1:
        if producciones[a][0]==pIzquierda:#SI IGUAL PRODUCCIO IZQUIERDA
            print('ENTRO')
            if pLEFT[0]==txt and pRigth[0]=='T':#BUSCA SI PIzquierda[0]==txt TERMINAL
                print('SI ES EL TERMINAL, SACAR:',producciones[a][1])
            elif pLEFT[0]==txt and pRigth[0]=='NT':#BUSCA SI PIzquierda[0]==txt NTERMINAL
                print('SI E EL NTERMINAL, HACER....',producciones[a][1])
            elif pRigth[0]=='NT':#SUSTITUYE EL OTRO TERMINAL S por A SI ES UN NT
                print('SUSTITUYENDO POR NTERMINAL...',producciones[a][1])
                recurisvo(a,pLEFT[0],txt)
            else:#PASAR A LA SIGUIENTE PRODUCCION
                print('SIGUIENTE PRODUCCION: misma',a)
                if pRigth[0]=='NT':
                    recurisvo(a+1,pLEFT[0],txt)
                else:
                    recurisvo(a+1,pIzquierda,txt)

        else:
            print('SIGUIENTE PRODUCCION:',a)
            if pRigth[0]=='NT':
                recurisvo(a+1,pLEFT[0],txt)
            else:
                recurisvo(a+1,pIzquierda,txt)

    else:
        print('FIN: NO SE ENCONTRO NADA IGUAL')
                #DOCUMENTACION EN UN IMG
                #original   ,[0,2,3,2,0]     ,S->A->B->C,posicion ,S->,[[1 D 1 0,[T NT T T]]]
def recursivox2(busqueda,txtArray,pila,txtAyuda,producciones,n,ID):
    if len(txtArray)==0:
        print('SIPI')
        return
    elif n<len(producciones)-1:
        sustitucion=producciones[n][2].split(' ')
        if busqueda==producciones[n][1]:#BUSCO EN LA POSICION A[1]
            if producciones[n][2]!='ε':#PUDO SUSTITUIR LA PRUDCCIONES
                print('E:',busqueda,txtArray,pila,txtAyuda,producciones[n],n,ID)
                if len(pila)!=0:
                    pila.pop(0)
                for num in range(len(sustitucion)):
                    pila.insert(0,sustitucion[num])
                busqueda=pila[0]
                recursivox2(busqueda,txtArray,pila,txtAyuda,producciones,0,n)
            else:#PUEDO ELMINAR ALGUNAS PROUDCCIONES
                print('!E:IGUAL',busqueda,txtArray,pila,txtAyuda,producciones[n],n,ID)
                if txtArray[0]==pila[0]:
                    txtAyuda.insert(0,txtArray.pop(0))
                    pila.pop(0)
                    if len(pila)==0:#ELMINAR PROUDCCION POR DAR  VACIO VUELVO A COMENZAR
                        print('P VACIA')
                        producciones.pop(ID)#***************************************************DELETE
                        print('/*/*/*/*/*/*/*/*',producciones)
                        nuevo=producciones
                        tamaño=len(txtAyuda)
                        for num in range(tamaño):
                           txtArray.insert(0,txtAyuda.pop(0))
                        recursivox2('S',txtArray,[],txtAyuda,nuevo,0,-1)
                    else:#BUSCO EN A[1]
                        print('NO VACIA')
                        #BUSCO B,
                        busqueda=pila[0]

                        print(busqueda,txtArray,pila,txtAyuda,producciones[n],n,ID)
                        recursivox2(busqueda,txtArray,pila,txtAyuda,producciones,0,-1)
                        return
                else:#SI NO ES IGUAL ELMINA ESA PROUDCCION Y VUELVO A COMENZAR
                    print('!E:DIF 8426',busqueda,txtArray,pila,txtAyuda,producciones[n],n,ID)
                    if ID!=-1:
                        producciones.pop(ID)#***************************************************DELETE
                    print('/*/*/*/*/*/*/*/*',producciones)
                    nuevo=producciones
                    tamaño=len(txtAyuda)
                    for num in range(tamaño):#ERROR POR EL CUAL SE QUEDA SIN EL NUMERO U ALGO ASIJLSDA FJSKDALFJSDKL FJDSLKFJSKLADJFKSDFJSDKLFJSDKLFJKLÑ
                        txtArray.insert(0,txtAyuda.pop(0))
                    print('S',txtArray,[],txtAyuda,nuevo,0,-1)
                    recursivox2('S',txtArray,[],txtAyuda,nuevo,0,-1)
                    

        else:
            #print('NEXT->')
            print('NEXT->: ',busqueda,txtArray,pila,txtAyuda,producciones[n],n,ID)
            recursivox2(busqueda,txtArray,pila,txtAyuda,producciones,n+1,ID)
    else:
        print('FIN->: ',busqueda,txtArray,pila,txtAyuda,producciones,n,ID)
        for a in range(len(producciones)):#BUSCAR PARA ELMINAR PRODUCCION QUE NO ENCUENTRO CARACTER POR HABERLO ELMINADO
            if producciones[a][0]=='ε':
                derecha=producciones[a][2].split(' ')
                for b in range(len(derecha)):
                    if busqueda==derecha[b]:
                        producciones.pop(a)#ELMINO PRODUCCION NO TERMINAL
                        nuevo=producciones
                        tamaño=len(txtAyuda)
                        for num in range(tamaño):#ERROR POR EL CUAL SE QUEDA SIN EL NUMERO U ALGO ASIJLSDA FJSKDALFJSDKL FJDSLKFJSKLADJFKSDFJSDKLFJSDKLFJKLÑ
                            txtArray.insert(0,txtAyuda.pop(0))
                        print('S:ELMINAR EN LA POSICION XD',a,b,txtArray,[],txtAyuda,nuevo,0,-1)
                        #return
                        recursivox2('S',txtArray,[],txtAyuda,nuevo,0,-1)

                        
        #print('OJO:',busqueda,txtArray,pila,txtAyuda,n,ID)
        #
asd()
#funcion()
#DOUCMENTACION
"""
#FELCHAS
https://graphviz.org/doc/info/shapes.html
#EJEMPLOS
https://graphviz.readthedocs.io/en/stable/examples.html#fsm-py
#NODOS
https://graphviz.org/doc/info/attrs.html
"""
