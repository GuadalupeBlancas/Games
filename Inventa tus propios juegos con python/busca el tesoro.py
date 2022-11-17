# sonar

import random
import sys

def dibujarTablero(tablero):
    # dibujar la estructura de datos del tablero

    lineah = '    '
    for i in range(1, 6):
        lineah += (' ' * 9) + str(i)

    # imprimir los números a lo largo del borde superior
    print(lineah)
    print('   ' + ('0123456789' * 6))
    print()

    #imprimir cada una de las 15 filas
    for i in range(15):
        # los numeros de una sola cifra deben ser precedidos por un espacio extra
        if i < 10:
            espacioExtra = ' '
        else:
            espacioExtra = ''
        print('%s%s %s %s' % (espacioExtra, i, obtenerFila(tablero, i), i))

    # imprimir los numeros a lo largo del borde ingerior
    print()
    print('   ' + ('0123456789' * 6))
    print(lineah)


def obtenerFila(tablero, fila):
    # devuelve una cadena con la estructura de datos de un tablero para una fila determinada
    filaTablero = ''
    for i in range(60):
        filaTablero += tablero[i][fila]
    return filaTablero

def obtenerNuevoTablero():
    # crear una nueva estructura de datos para un tablero de 60x15
    tablero = []
    for x in range(60):
        tablero.append([])
        for y in range(15):
# usar diferentes caracteres para el óceano para hacerlo más fácil de leer
            if random.randint(0, 1) == 0:
                tablero[x].append('~')
            else:
                tablero[x].append('`')
    return tablero

def obtenerCofresAleatorios(numCofres):
# crear una lista de estructura de datos cofre (lista de dos elemetntos con coordenadas x,y)
    cofres = []
    for i in range(numCofres):
        cofres.append([random.randint(0,59), random.randint(0,14)])
    return cofres

def esMovidaValida(x, y):
# devuelve true si las coordenadas pertenecen al tablero, false de lo contrario
    return x >= 0 and x <= 59 and y >= 0 and y <= 14

def realizarMovida(tablero, cofres, x, y):
# cambia la estructura de datos del tablero agregando un caracter de dispositivo sonar
# de la lista de cofres a medida que son encontrados. Devuelve False si la movida no es válida

    if not esMovidaValida(x,y):
        return False

    menorDistancia = 100

    for cx, cy in cofres:
        if abs(cx - x) > abs(cy - y):
            distancia = abs(cx - x)
        else:
            distancia = abs(cy - y)

        if distancia < menorDistancia:
            menorDistancia = distancia

    if menorDistancia == 0:
# xy está directamente en un cofre
        cofres.remove([x, y])
        return 'Has encontrado uno de los cofres del tesoro'
    else:
        if menorDistancia < 10:
            tablero[x][y] = str(menorDistancia)
            return 'Tesoro detectado a una distancia %s del dispisitov sonar' % (menorDistancia)
        else:
            tablero[x][y] = 'O'
            return 'El sonar no ha detectado nada. Todos los cofres estan fuera del alcance del dispositivo'

def ingresarMovidaJugador():
    # permite el jugador teclear su movida, devuelve una lista de dos elementos con coordenadas xy
    print('¿Dónde quieres dejar caer el siguiente dispositivo sonar? (0 - 59 0-14) (o teclea salir)')
    while True:
        movida = input()
        if movida.lower() == 'salir':
            print('Gracias por jugar')
            sys.exit()

        movida = movida.split()
        if len(movida) == 2 and movida[0].isdigit() and movida[1].isdigit() and esMovidaValida(int(movida[0]), int(movida[1])):
            return [int(movida[0]), int(movida[1])]
        print('Ingresa un número de 0 a 59, un espacio, y luego un número de 0 a 14')



def jugarDeNuevo():
# esta funcion devuelve true si es jugador quiere jugar de nuevo False sino
    print('¿Quieres jugar de nuevo?')
    return input().lower().startswith('s')


def mostrarInstrucciones():
    print('''Instrucciones:
          Eres el capital de simon, un buque cazador de tesoros. Tu mision actual 
          es encontrar los tres cofres con tesoros perdidos que se hallan ocultos en
          la parte del ocenano en que te encuentras y recogerlos. 
          Para jugar ingresa las coordenadas del punto del óceano en que quieres 
          colocar un dispositivo sonar. Este puede detectar cuál es la distancia al
          cofre más cercano
          Por ejemplo, la d de abajo indica donde se ha colocado el dispositivo, y los
          numeros 2 representan los sitios a una distancia 2 del dispositivo
          los numeros 4 representan los sitios a una distancia de 4 del dispositivo
          
          444444444
          4       4
          4 22222 4
          4 2   2 4
          4 2 d 2 4
          4 2   2 4
          4 22222 4
          4       4
          444444444 
          pulsa enter para continuar...''')
    input()

    print('''Por ejemplo aqui hay un cofre del tesoro (la c) ubicado a una distancia
          2 del dispositivo sonar (la d):
          
          22222
          c   2
          2 d 2
          2   2
          22222
          
          El punto donde el dispositivo fue encontrado se indicara con un 2
          
          Los cofres del tesoro no se mueven. Los dispositivos sonar pueden detectar
          cofres hasta una distancia 9. Si todos los cofres estan fuera del alcance,
          el punto se indicará con un 0
          
          Si el dispositivo es colocado directamente sobre el cofre del tesoro,
          has descubierto la ubicacion del cofre, y este será recogido. El dispositivo
          sonar permanecerá ahí
          
          Cuando recojas un cofre, todos los dispositivos sonar se actualizarán para
          localizar el próximo cofre hundido más cercano.
          Pulsa enter para continuar...''')
    input()
    print()


print('¡S O N A R!')
print()
print('¿Te gustaría ver las instrucciones? s/n')
if input().lower().startswith('s'):
    mostrarInstrucciones()

while True:
    # configuracion del juego
    dispositivosSonar = 16
    elTablero = obtenerNuevoTablero()
    losCofres = obtenerCofresAleatorios(3)
    dibujarTablero(elTablero)
    movidasPrevias = []

    while dispositivosSonar > 0:
        #comienzo de turno

        #mostrar el estado de los dispositivos sonar / cofres
        if dispositivosSonar > 1: extraSsonar = 's'
        else: extraSsonar = ''
        if len(losCofres) > 1: extraScofre = 's'
        else: extraScofre = ''
        print('Aún tienes %s dispositivos %s sonar. Falta encontrar %s cofres %s.' % (dispositivosSonar, extraSsonar, len(losCofres), extraScofre))

        x,y = ingresarMovidaJugador()
        movidasPrevias.append([x, y]) # debemos registrar todas las movidas para que los dispositivos extra sonar puedan ser actualizados

        resultadoMovida = realizarMovida(elTablero, losCofres, x, y)
        if resultadoMovida == False:
            continue
        else:
            if resultadoMovida == 'Has encontrado uno de los cofres del tesoro':
                # actualiza todos los soñar presentes en el mapa
                for x, y in movidasPrevias:
                    realizarMovida(elTablero, losCofres, x, y)
            dibujarTablero(elTablero)
            print(resultadoMovida)

        if len(losCofres) == 0:
            print('has encontrado todos los cofres del tesoro!')
            break

        dispositivosSonar -= 1

    if dispositivosSonar == 0:
        print('Nos hemos quedado sin dispositivos sonar, debemos regresar')
        print('Juego terminado')
        print('los cofres restantes estaban aquí: ')
        for x, y in losCofres:
            print('      %s, %s' % (x,y))

    if not jugarDeNuevo():
        break