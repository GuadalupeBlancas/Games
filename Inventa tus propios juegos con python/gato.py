# TA te ti

import random

def dibujarTablero(tablero):
# esta funcion dibuja el tablero recibido como argumento
# 'tablero' es una lista de 10 cadenas representando la pizarra (ignora el indice 0)
    #print(' | |')
    print(' ' + tablero[7] + '|' + tablero[8] + '|' + tablero[9])
    #print(' | |')
    print('--------')
    #print(' | |')
    print(' ' + tablero[4] + '|' + tablero[5] + '|' + tablero[6])
    #print(' | |')
    print('________')
    #print(' | |')
    print(' ' + tablero[1] + '|' + tablero[2] + '|' + tablero[3])
    #print(' | |')
    #print('________')

# NOTA: si se agregan las lineas que estan comentadas hace un tablero por cada
    # fila de posiciones

def ingresaLetraJugador():
# permite ingresar al jugador la letra que quiere ser
# devuelve una lista con las letras de los jugadores como primer elemento, y de la computadora como segudno
    letra = ''
    while not (letra == 'X' or letra == 'O'):
        print('¿deseas ser X o O?')
        letra = input().upper()
# el primer elemento de la lista es la letra del jugador
# el segundo elemento es la computadora
    if letra == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def quienComienza():
# elije al azar que jugador comienza
    if random.randint(0, 1) == 0:
        return 'La computadora'
    else:
        return 'El jugador'

def jugarDeNuevo():
# Devuelve True si el jugador quiere volver a jugar y False si no quiere
    print('¿Deseas volver a jugar? (si/no)')
    return input().lower().startswith('s')

def hacerJugada(tablero, letra, jugada):
    tablero[jugada] = letra

def esGanador(ta, le):
# dado un tablero y una letra del jugador devuelve True si gana
# reemplazamos tablero por ta y letra por le
    return ((ta[7] == le and ta[8] == le and ta[9] == le) or # horizontal superior
    (ta[4] == le and ta[5] == le and ta[6] == le) or # horizontal medio
    (ta[1] == le and ta[2] == le and ta[3] == le) or # horizontal inferior
    (ta[7] == le and ta[4] == le and ta[1] == le) or # horizontal izquierda
    (ta[8] == le and ta[5] == le and ta[2] == le) or # horizontal medio
    (ta[9] == le and ta[6] == le and ta[3] == le) or # horizontal derecha
    (ta[7] == le and ta[5] == le and ta[3] == le) or # diagonal
    (ta[9] == le and ta[5] == le and ta[1] == le)) # diagonal

def obtenerDuplicadoTablero(tablero):
# duplica el tablero
    dupTablero = []

    for i in tablero:
        dupTablero.append(i)

    return dupTablero

def hayEspacioLibre(tablero, jugada):
# devuelve true si hay espacio libre para jugar en el tablero
    return tablero[jugada] == ' '

def obtenerJugadaJugador(tablero):
# permite al jugador escribir su jugada
    jugada = ' '
    while jugada not in '1 2 3 4 5 6 7 8 9'.split() or not hayEspacioLibre(tablero, int(jugada)):
        print('¿cuál es tu próxima jugada? (1-9)')
        jugada = input()
    return int(jugada)

def elegirAzarDeLista(tablero, listaJugada):
# devuelve una jugada válida en el tablero de la lista recibida
# devuelve None sino hay una jugada
    jugadasPosibles = []
    for i in listaJugada:
        if hayEspacioLibre(tablero, i):
            jugadasPosibles.append(i)

    if len(jugadasPosibles) != 0:
        return random.choice(jugadasPosibles)
    else:
        return None

def obtenerJugadaComputadora(tablero, letraComputadora):
# dado un tablero y letra dada la computadora determina que jugada efectuar
    if letraComputadora == 'X':
        letraJugador = 'O'
    else:
        letraJugador = 'X'

# algoritmo de inteligencia artificial para gato
# verifica si la IA puede ganar en la proxima jugada
    for i in range(1, 10):
        copia = obtenerDuplicadoTablero(tablero)
        if hayEspacioLibre(copia, i):
            hacerJugada(copia, letraComputadora, i)
            if esGanador(copia, letraComputadora):
                return i

# verifica si el jugador puede ganar en la proxima jugada y lo bloquea
    for i in range(1, 10):
        copia = obtenerDuplicadoTablero(tablero)
        if hayEspacioLibre(copia, i):
            hacerJugada(copia, letraJugador, i)
            if esGanador(copia, letraJugador):
                return i

    # intenta ocupar una de las esquinas de estar libre
    jugada = elegirAzarDeLista(tablero, [1, 3, 7, 9])
    if jugada != None:
        return jugada

    # de estar libre intenta ocupar el centro
    if hayEspacioLibre(tablero, 5):
        return 5

    # ocupa alguno de los lados
    return elegirAzarDeLista(tablero, [2, 4, 6, 8])

def tableroCompleto(tablero):
    # devuelve True si cada espacio del tablero fue ocupado
    for i in range(1,10):
        if hayEspacioLibre(tablero, i):
            return False
    return True


print('Bienvenido al juego del Gato')

while True:
    # resetear tablero
    elTablero = [' '] * 10
    letraJugador,  letraComputadora = ingresaLetraJugador()
    turno = quienComienza()
    print(turno + ' irá primero')
    juegoEnCurso = True

    while juegoEnCurso:
        if turno == 'El jugador':
            # Turno del jugador
            dibujarTablero(elTablero)
            jugada = obtenerJugadaJugador(elTablero)
            hacerJugada(elTablero, letraJugador, jugada)

            if esGanador(elTablero, letraJugador):
                dibujarTablero(elTablero)
                print('Felicidades has ganado')
                juegoEnCurso = False
            else:
                if tableroCompleto(elTablero):
                    dibujarTablero(elTablero)
                    print('Es empate')
                    break
                else:
                    turno = 'La computadora'

        else:
            # Turno de la computadora
            jugada = obtenerJugadaComputadora(elTablero, letraComputadora)
            hacerJugada(elTablero, letraComputadora, jugada)

            if esGanador(elTablero, letraComputadora):
                dibujarTablero(elTablero)
                print('La IA te ha vencido')
                juegoEnCurso = False
            else:
                if tableroCompleto(elTablero):
                    dibujarTablero(elTablero)
                    print('Es un empate')
                    break
                else:
                    turno = 'El jugador'

    if not jugarDeNuevo():
        break