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
grap()
#DOUCMENTACION
"""
#FELCHAS
https://graphviz.org/doc/info/shapes.html
#EJEMPLOS
https://graphviz.readthedocs.io/en/stable/examples.html#fsm-py
#NODOS
https://graphviz.org/doc/info/attrs.html
"""
