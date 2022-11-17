import random
def obtenerNumeroSecreto(digitosNum):
    # devuelve un numero de largo digitosNum, compuesto de digitos únicos al azar
    numeros = list(range(10))
    random.shuffle(numeros)
    numSecreto = ''
    for i in range(digitosNum):
        numSecreto += str(numeros[i])
    return numSecreto

def obtenerPista(conjetura, numSecreto):
    # devuelve una palabra con las pistas Paneccillos, pico y fermi en ella
    if conjetura == numSecreto:
        return 'Lo has adivinado'

    pista = []

    for i in range(len(conjetura)):
        if conjetura[i] == numSecreto[i]:
            pista.append('Fermi')
        elif conjetura[i] in numSecreto[i]:
            pista.append('Pico')
    if len(pista) == 0:
        return 'Panecillos'

    pista.sort()
    return ' '.join(pista)

def esSoloDigitos(num):
    # devuelve true si el numero se compone solo de digitos de lo contrario False
    if num == '':
        return False

    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False

    return True

def jugarDeNuevo():
    # Devuelve true si el jugador quiere jugar de nuevo False sino
    print('¿Deseas volver ajugar? s/n')
    return input().lower().startswith('s')

digitosNum = 3
MAXADIVINANZAS = 10

print('Estoy pensando en un número de %s digitos, adivina cual es' % (digitosNum))
print('Aquí hay algunas pistas: ')
print('Cuando digo:      Eso signofica: ')
print('Pico              Un digito es correcto pero en la posición incorrecta')
print('Fermi             Un digito es correcto y en la posicion corrrecta')
print('Panecillos        Ningún dígito es correcto')

while True:
    numSecreto = obtenerNumeroSecreto(digitosNum)
    print('He pensado en un numero tienes %s intentos para adivinarlo' % MAXADIVINANZAS)

    numIntentos = 1
    while numIntentos <= MAXADIVINANZAS:
        conjetura = ''
        while len(conjetura) != digitosNum or not esSoloDigitos(conjetura):
            print('Conjetura #%s: ' % (numIntentos))
            conjetura = input()

        pista = obtenerPista(conjetura, numSecreto)
        print(pista)
        numIntentos += 1

        if conjetura == numSecreto:
            break
        if numIntentos > MAXADIVINANZAS:
            print('Te has quedado sin intentos, el numero era %s' % (numSecreto))

    if not jugarDeNuevo():
        break