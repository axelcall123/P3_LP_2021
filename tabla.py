import ordenarP as ordenarP
def table(array):
    Nombre=array[0]
    NT=array[1]
    T=array[2]
    NTI=array[3]
    array_producciones=array[4]
    #print(array_producciones)
    #ordenar por prioridad de terminaels
    ordenarP.ordenar(array_producciones,NT)