# Que se impriman las opciones de:

# Jugar

# Salir

# Y que el jugador pueda ingresar una opción.

# Luego que:
# Si se eligió uno, que avance a una función Play() //Por ahora no haga nada la funcion esa o solo imprima "jugando"..
# Si se eligió salir, que se termine la ejecución del programa.
import Play
import Limpiar
import time 

def imprimir_menu():

	print("╔══════════════════════════════╗")
	print("║          1-Jugar             ║")
	print("║          2-Salir             ║")
	print("╚══════════════════════════════╝")
	

def despedir():
	print("Hasta luego. . .")
	Limpiar.Limpiar()

	for i in range(3):
		print(" ( ¨ ¨ )┐")
		print("└(  O  ) ")
		time.sleep(1)
		Limpiar.Limpiar()
		print(" ( ¨ ¨ )┘")
		print("┌( \=/ ) ")
		time.sleep(1)
		Limpiar.Limpiar()

	input("")


def MenuPrincipal():

	imprimir_menu()

	opcion=input("")


	while (opcion !='1' and opcion != '2'):
		print("Por Favor eliga opción 1 o 2")
		
		opcion=input("")
	
	
	if (opcion=='1'):
		Play.play()

	elif (opcion=='2'):
		despedir()
		




