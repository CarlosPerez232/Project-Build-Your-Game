import Palabras #Importamos la funcion Palabras que devuelve un string aleatorio para jugar
import Tablero #Importamos la funcion Tablero que despliega el tablero de juego

difficult = input('Which leve you wanna play?\[easy, medium, hard]')
difficult = difficult.lower() 
word = Palabras.palabras(difficult) #aqui debemos de poner Palabras.palabras()
secret_word = ['-']* len(word) #El string que mostraremos al user. Es un string del mismo tamaño que word
mistakes = 0 #Variable de control y que además nos va a permitir imprimir un tablero diferente
while True:

	Tablero.tablero(mistakes,secret_word) #Llamamos a la funcion tablero con el numero de errores
					      #actuales y la palabra secreta actual.
	print('*'*70)
	user_letter = str(input('Please type a letter:\n')) #Solicitamos un string y hacemos casteo a string
	user_letter = user_letter.lower() #usamos el metodo lower() para hacegurarnos que solo usamos minusculas
	
	indexes = [letter for letter in range(len(word)) if word[letter] == user_letter]
	if len(indexes) == 0:
		mistakes += 1
		if mistakes == 7:
			Tablero.tablero(mistakes, secret_word)
			break

	else:
		for index in indexes:
			secret_word[index] = user_letter
	indexes = []

	if ''.join(secret_word) == word:
		Tablero.tablero(mistakes, secret_word)
		print('**********C O N G R A T S!**********\n------------- YOU WIN! -------------')
		break
