import random


#Ingresa una dificultad para seleccionar una categoría de palabras
palabras_categoria = {'easy':['mamey','carro','perro'],'medium':['portaaviones','aracnido','turbulencia'],'hard':['onomatopeya','civilizacion','canasta']}
def palabras():
    while True:
	dificultad = input('Write the difficult: easy, medium or hard!')
        if dificultad == 'easy':
            x = palabras_categoria['easy'][random.randrange(0,3)]
            return x
            break
        elif dificultad == 'medium':
            x = palabras_categoria['medium'][random.randrange(0,3)]
            return x
            break
        elif dificultad == 'hard':
            x = palabras_categoria['hard'][random.randrange(0,3)]
            return x
            break
        else:
            print("Must be easy, medium or hard")


