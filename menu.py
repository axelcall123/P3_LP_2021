import lector as lector
import gramatica_inf as gramatica_inf
import automata_pila as automata_pila
import tabla as tabla
gramatica=[]
def menu():
    print("""
	SELECCIONA UNA OPCION1
	t1 - CARGAR ARCHIVO
	t2 - INFORMACION GRAMATICA
	t3 - GENERAR AUTOMATA
	t4 - REPORTE DE RECORRIDO
	t5 - REPORTE TABLA
	t6 - SALIR
	""")

while True:
	menu()
	opcionMenu = input('INSERTE UNA OPCION >>')
	if opcionMenu == '1':
		gramatica=lector.leer()
	elif opcionMenu == '2':
		elegir = input('ELIGE LA POSICION DEL AUTOMATA >>')
		if int(elegir)-1<len(gramatica):
			gramatica_inf.info(gramatica[int(elegir)-1])
		else:
			print('SE EXCEDIO DEL LIMTE :"C')
	elif opcionMenu == '3':
		elegir = input('ELIGE LA POSICION DEL AUTOMATA >>')
		if int(elegir)-1<len(gramatica):
			automata_pila.automataHtml(gramatica[int(elegir)-1])
		else:
			print('SE EXCEDIO DEL LIMTE :"C')
	elif opcionMenu == '4':
		elegir = input('ELIGE LA POSICION DEL AUTOMATA >>')
		if int(elegir)-1<len(gramatica):
			palabra = input('ESCRIBA LA PALABRA EVALUADA >>')
			tabla.table(gramatica[int(elegir)-1],palabra,True)
		else:
			print('SE EXCEDIO DEL LIMTE :"C')
	elif opcionMenu == '5':
		elegir = input('ELIGE LA POSICION DEL AUTOMATA >>')
		if int(elegir)-1<len(gramatica):
			palabra = input('ESCRIBA LA PALABRA EVALUADA >>')
			tabla.table(gramatica[int(elegir)-1],palabra,False)
		else:
			print('SE EXCEDIO DEL LIMTE :"C')
	elif opcionMenu == '6':
		break
	elif opcionMenu=='10':
		print()
	else:
		input('No has pulsado ninguna opción correcta...\npulsa una tecla para continuar')