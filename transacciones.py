def transacciones(T,array,NTI):
    #Transacciones Producciones NT
    arrayAB=[]
    for produ in array:
        #texto=produ[1].replace(' ','')
        arrayAB.append([['q','ε',produ[0]],['q',produ[1]]])
    for term in T:
        arrayAB.append([['q',term,term],['q','ε']])
    tabla=[]
    #id=1
    for array in arrayAB:
        #tabla.append([array[0][1],array[0][2],array[1][1],id])
        tabla.append([array[0][1],array[0][2],array[1][1]])
        #id+=1
    return tabla