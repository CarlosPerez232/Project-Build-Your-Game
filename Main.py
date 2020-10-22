import Palabras #Importamos la funcion Palabras que devuelve un string aleatorio para jugar
import Tablero #Importamos la funcion Tablero que despliega el tablero de juego
import os
import re

word = Palabras.palabras() #aqui debemos de poner Palabras.palabras()
secret_word = ['-']* len(word) #El string que mostraremos al user. Es un string del mismo tamaño que word
mistakes = 0 #Variable de control y que además nos va a permitir imprimir un tablero diferente
while True:
	os.system('clear')
	Tablero.tablero(mistakes,secret_word) #Llamamos a la funcion tablero con el numero de errores
					      #actuales y la palabra secreta actual.
	print('*'*70)
	while True:
		user_letter = str(input('Please type a letter:\n')) #Solicitamos un string y hacemos casteo a string
		user_letter = user_letter.lower() #usamos el metodo lower() para hacegurarnos que solo usamos minusculas
	
		if user_letter == '':
			print('Please enter one letter!')
			pass
		elif re.searchall(r'[A-Za-z]', user_letter) == None:
			print('Please enter a letter between a-z.\n')
			pass 

		else:
			break

	indexes = [letter for letter in range(len(word)) if word[letter] == user_letter] # Guarda el indice en el que la entrada del usuario coincide con el indice del string de la palabra
	if len(indexes) == 0: #Si la longitud de la lista indexes es 0 significa que el usuario no acerto
		mistakes += 1
		if mistakes == 7:
			os.system('clear')
			Tablero.tablero(mistakes, secret_word)
			break

	else:
		for index in indexes:
			secret_word[index] = user_letter
	indexes = []

	if ''.join(secret_word) == word:
		os.system('clear')
		Tablero.tablero(mistakes, secret_word)
		print('**********C O N G R A T S!**********\n------------- YOU WIN! -------------')
		break
