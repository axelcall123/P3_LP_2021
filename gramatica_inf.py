import time
from graphviz import Digraph
def info(array):
    Nombre=array[0]
    NT=array[1]
    T=array[2]
    NTI=array[3]
    array_producciones=array[4]
    #print(array)
    unir=""
    txtProdu=""
    unirTnT="{"
    for array in array_producciones:
        if unir!=array[0]:#SI LA OPCION DIFERENTE DE: A-> ##
            unir=array[0]
            txtProdu=txtProdu+array[0]+"->"+array[1]+"\n"
        else:#SI NO:  |##
            for a in range(len(array[0])):#AGREGA EL TAMAÑO DE ESPACIOS DEL NT
                txtProdu=txtProdu+" "
            txtProdu=txtProdu+"  |"+array[1]+"\n"
    #NOMBRE: NOMBRE
    unirTnT="{"
    print('Nombre de la gramática', Nombre)
    for n in range(len(NT)):
        if n<len(NT)-1:
            unirTnT=unirTnT+NT[n]+","
        else:
            unirTnT=unirTnT+NT[n]+"}"
    print("No terminales =",unirTnT)

    #TERMINALES: TERMINALES
    unirTnT="{"
    for n in range(len(T)):
        if n<len(T)-1:
            unirTnT=unirTnT+T[n]+","
        else:
            unirTnT=unirTnT+T[n]+"}"
    print("terminales =",unirTnT)

    #NO TERMINALE INICIALES: NTI
    print("terminales inicial=",NTI[0])

    print(txtProdu)
    print('Tiempo de espera')
    elegir=''
    while True:
        if elegir=='si':
            return
        print("esperando____")
        time.sleep(5)
        elegir = input('QUIERE SALIR: si,no >>') # espera en segundos
    
