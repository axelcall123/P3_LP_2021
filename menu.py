import lector as lector
import gramatica_inf as gramatica_inf
import automata_pila as automata_pila
import tabla as tabla
gramatica=[]
def menu():
    print("""
	SELECCIONA UNA OPCION
	t1 - CARGAR ARCHIVO
	t2 - INFORMACION GRAMATICA
	t3 - GENERAR AUTOMATA
	t4 - REPORTE DE RECORRIDO
	t6 - REPORTE TABLA
	t5 - SALIR
	""")

while True:
	menu()
	opcionMenu = input('INSERTE UNA OPCION >>')
	if opcionMenu == '1':
		gramatica=lector.leer()
	elif opcionMenu == '2':
		for array in gramatica:
			gramatica_inf.info(array)
	elif opcionMenu == '3':
		for array in gramatica:
			automata_pila.automataHtml(array)
	elif opcionMenu == '4':
		print()
	elif opcionMenu == '5':
		for array in gramatica:
			tabla.table(array)
	elif opcionMenu == '6':
		break
	elif opcionMenu=='10':
		print()
	else:
		input('No has pulsado ninguna opción correcta...\npulsa una tecla para continuar')