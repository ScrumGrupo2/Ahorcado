
import DarIncongnita

import MeterGuiones
import ImprimirEspaciado
import MeterLetra
import Control_LetraEnPalabra
import Hangman
import MenuPartida
import time
import Limpiar


def play():

	jugando = True
	Intentos = 5
	jugando= [True,Intentos]

	while jugando[0]:
		
		jugando = playMatch(jugando[1])
		
	

	pass




def playMatch(Intentos):

	incognitaSolucion = DarIncongnita.DarIncognitaDesdeArchivo()
	incognitaGuion = ""
	incognitaGuion = MeterGuiones.MeterGuiones(incognitaSolucion)



	Gano = False
	Perdio = False
	Intentos = Intentos




	while not(Gano) and not(Perdio):

		Limpiar.Limpiar()
		
		Hangman.hangman(Intentos, incognitaGuion)
		
				

		if Intentos == 0:
				Perdio= True

		if not Perdio:


			letraMenu = MenuPartida.MenuPartida()
			
			if letraMenu[0]:
				letra = letraMenu[1]

				if Control_LetraEnPalabra.Control_LetraEnPalabra(letra,incognitaSolucion):
				
					incognitaGuion = MeterLetra.MeterLetra(incognitaGuion,letra, Control_LetraEnPalabra.Control_LetraEnPalabra(letra,incognitaSolucion))
				else:
					Intentos = Intentos-1

				print("")
				

			
				if incognitaGuion.count("_")==0:
					Gano = True
					



			else:
				Perdio=True

			
			

	time.sleep(1)




	if Gano:

		mensaje_gano()
		input()

		return [True,Intentos]
	elif Perdio:
		mensaje_predio2()

		print("La respuesta FUE: ",incognitaSolucion)
		return [False,0]
		



def mensaje_gano():
	print("╔══════════════════════════════════════════════════════════╗")
	print("║                                                          ║")
	print("║       ===>Por Fin te salio algo en la vida :P <===       ║")
	print("║                                                          ║")
	print("╚══════════════════════════════════════════════════════════╝")



def mensaje_predio():
	print("-------------------------------------------------------")
	print("-     Perdiste y si no jugas otra vez sos un ...      -")
	print("-------------------------------------------------------")
def mensaje_predio2():
	for i in range(3):
		print("-------------------------------------------------------")
		print("-     Perdiste y si no jugas otra vez sos un ...      -")
		print("-------------------------------------------------------")
		time.sleep(0.9)
		Limpiar.Limpiar()
		print("")
		print("-     Perdiste y si no jugas otra vez sos un ...      -")
		
		time.sleep(0.9)
		Limpiar.Limpiar()
