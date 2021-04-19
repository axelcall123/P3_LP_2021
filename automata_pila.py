import transacciones as transacciones
from graphviz import Digraph
import webbrowser#pag
import io
def automataHtml(array):
    Titulo=array[0]
    NT=array[1]
    T=array[2]
    NTI=array[3]
    array_producciones=array[4]
    array_T=transacciones.transacciones(T,array_producciones,NTI)

    txtTitulo='Nombre: '+Titulo
    txtTerminales='Terminales={'
    txtAlfabeto='Alfabeto de pila={'
    txtEstados='Estados={i,p,q,f}'
    txtEstadoI='Estado inicial={'+NTI[0]+'}'
    txtEstadoA='Estado de aceptación={f}'
    #TERMINALES
    for n in range(len(T)):
        if n<len(T)-1:
            txtTerminales=txtTerminales+T[n]+','
        else:
            txtTerminales=txtTerminales+T[n]+'}'
    #ALFABETO DE PILA NO TERMINALES
    for n in range(len(T)):
        if n<len(T)-1:
            txtAlfabeto=txtAlfabeto+T[n]+','
        else:
            txtAlfabeto=txtAlfabeto+T[n]+','
    #ALFABETO DE PILA TERMINALES
    for n in range(len(NT)):
        if n<len(NT)-1:
            txtAlfabeto=txtAlfabeto+NT[n]+','
        else:
            txtAlfabeto=txtAlfabeto+NT[n]+',Ω}'
    #print(txtTitulo,txtTerminales,txtAlfabeto,txtEstados,txtEstadoI,txtEstadoA)
    estado_i='ε,ε;Ω'
    estado_p='ε,ε;'+NTI[0]
    estado_q1=''
    estado_q2=''
    estado_f='ε,Ω;ε'
    
    tableI='<<TABLE BORDER="0" CELLBORDER="0.1">'
    tableF='</TABLE>>'
    trIB='<TR><TD><font color="black">'
    trFB='</font></TD></TR>'
    estado_q1=estado_q1+tableI
    estado_q2=estado_q2+tableI
    for n in range(len(array_T)):
        if n<len(array_producciones):#DIVIDIR DE TERMINAELS|NO TERMINALES
            estado_q1=estado_q1+trIB+array_T[n][0]+','+array_T[n][1]+';'+array_T[n][2]+trFB.replace(' ','')
        else:
            estado_q2=estado_q2+trIB+array_T[n][0]+','+array_T[n][1]+';'+array_T[n][2]+trFB

    estado_q1=estado_q1+tableF
    estado_q2=estado_q2+tableF
    graph(estado_q1,estado_q2,estado_i,estado_p,estado_f)
    html(txtTitulo,txtTerminales,txtAlfabeto,txtEstados,txtEstadoI,txtEstadoA)
    #print(estado_q1,estado_q2)
    #print('Tamaño',len(array_producciones))
    #print(array_T)

def graph(q1,q2,ei,ep,ef):#arriba, abajo, estado inicial,estado p, estado final
    dot = Digraph(comment='SI',format='png')
    dot.graph_attr['rankdir'] = 'LR'
    dot.node('I', 'i')
    dot.node('P', 'p')
    dot.node('Q', 'q')
    dot.node('F', 'f')
    dot.edge('I', 'P',label=ei)
    dot.edge('P', 'Q',label=ep)
    dot.edge('Q', 'F',label=ef)
    dot.edge('Q:n','Q:n',label=q1)
    dot.edge('Q:s','Q:s',label=q2)#Q:s sirve para que vaya abajo | n,s,e,o
    
    #print(dot.source) 
    dot.render('IMG/automata')

def html(titulo,term,alfabet,estado,estadoI,estadoA):
    f = open('Automata.html','w',newline='',encoding="utf-8")
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
    <body class="cont">
        <div class="container">
            <div class="row">
                <div class="col-md-6">
  """
    fin="""
                </div>
                <div class="col-md-6">
                    <img src="IMG/automata.png" class="img-fluid">
                </div>
            </div>  
        </div>  
    </body>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>
</html>
  """
    cuerpo="""<p class="Titulo">"""+titulo+"""</p> <p class="txt">"""+term+"""</p> <p class="txt">"""+alfabet+"""</p> <p class="txt">"""+estado+"""</p> <p class="txt">"""+estadoI+"""</p> <p class="txt">"""+estadoA+"""</p>"""
    #print(cuerpo)
    f.write(principal)#inicio
    f.write(cuerpo)#medio
    f.write(fin)#final
    f.close()#cerar
    webbrowser.open_new_tab('Automata.html')