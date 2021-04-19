from tkinter import filedialog
from tkinter import *
import analizador as analizador
def leer():
    root = Tk()#
    root =  filedialog.askopenfilename(initialdir = "/AXEL/DOCUMENTOS/U/GITHUB/P3_LP_2021",title = "Select file",filetypes = (("lfp files","*.glc"),("all files","*.*")))
    archivo=open(root, 'r', encoding="utf-8")
    unir=''
    for linea in archivo.readlines():#LEE LINEA POR LINEA
        unir=unir+linea

    gramatica=unir.split("*")
    array_salida=[]
    for array in gramatica:
        #print(array,"evaluar")
        #array_entrada=analizador.analizador(array)
        array_entrada=analizador.analizador(array)
        if array_entrada!=None:
            array_salida.append(array_entrada)
    return array_salida