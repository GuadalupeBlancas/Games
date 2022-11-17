import random
IMAGENES_AHORCADO = ['''

    +---+
    |    |
         |
         |
         |
         |
=========''', '''

    +---+
    |   |
    o   |
        |
        |
        |
=========''', '''

    +---+
    |   |
    o   |
    |   |
        |
        |
=========''', '''

    +---+
    |   |
    o   |
   /|   |
        |
        |
=========''', '''

    +---+
    |   |
    o   |
   /|\  |
        |
        |
=========''', '''

    +---+
    |   |
    o   |
   /|\  |
   /    |
        |
=========''', '''

    +---+
    |   |
    o   |
   /|\  |
   / \  |
        |
=========''']
palabras = 'hormiga babuino tejon murcielago oso'.split()

def obtenerPalabraAlAzar(listaDePalabras):

    indiceDePalabras = random.randint(0, len(listaDePalabras) - 1)
    return listaDePalabras[indiceDePalabras]

def mostrarTablero(IMAGENES_AHORCADO,letrasIncorrectas, letrasCorrectas, palabraSecreta):
    print(IMAGENES_AHORCADO[len(letrasIncorrectas)])
    print()

    print('Letras incorrectas:', end=' ')
    for letra in letrasIncorrectas:
        print(letra, end='')
    print()

    espaciosVacios = '_' * len(palabraSecreta)

    for i in range(len(palabraSecreta)):
        if palabraSecreta[i] in letrasCorrectas:
            espaciosVacios = espaciosVacios[:i] + palabraSecreta[i] + espaciosVacios[i+1:]

    for letra in espaciosVacios:
        print(letra, end='')
    print()

def obtenerIntento(letrasProbadas):
# devielve la letra ingresada por el jugador. verifica que el jugador ha ingresado solo una letra y no otra cosa
    while True:
        print('Adivina una letra.')
        intento = input()
        intento = intento.lower()
        if len(intento) != 1:
            print('Por favor introduce una letra.')
        elif intento in letrasProbadas:
            print('Ya has probado esta letra, ingresa otra')
        elif intento not in 'abcdefghijklmnñopqrstuvwxyz':
            print('Por favor ingresa una letra')
        else:
            return intento

def jugarDeNuevo():
    # devuelve True si quiere jugar y False si no
    print('¿Quieres jugar de nuevo? s/n')
    return input().lower().startswith('s')


print('A H O R C A D O')
letrasIncorrectas = ''
letrasCorrectas = ''
palabraSecreta = obtenerPalabraAlAzar(palabras)
juegoTerminado = False

while True:
    mostrarTablero(IMAGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)

    #permite al jugador escribir una letra
    intento = obtenerIntento(letrasIncorrectas + letrasCorrectas)

    if intento in palabraSecreta:
        letrasCorrectas = letrasCorrectas + intento

        # verifica si el jugador ha ganado
        encontradoTodasLasLetras = True
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letrasCorrectas:
                encontradoTodasLasLetras = False
                break
        if encontradoTodasLasLetras:
            print('Si, la palabra secreta es '+ palabraSecreta+ ', has ganado')
            juegoTerminado = True
    else:
        letrasIncorrectas = letrasIncorrectas + intento

#comprobar si el jugador ha agotado sus intentos y perdido
        if len(letrasIncorrectas) == len(IMAGENES_AHORCADO) - 1:
            mostrarTablero(IMAGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)
            print('Te has quedado sin intentos\n después de '+str(len(letrasIncorrectas))+ ' intentos fallidos y ' + str(len(letrasCorrectas)) + ' aciertos, la palabra era '+ palabraSecreta)
            juegoTerminado = True

# Preguntar si el jugador quiere volver a jugar (pero solo sí el juego ha terminado)
    if juegoTerminado:
        if jugarDeNuevo():
            letrasIncorrectas = ''
            letrasCorrectas = ''
            juegoTerminado = False
            palabraSecreta = obtenerPalabraAlAzar(palabras)
        else:
            break
