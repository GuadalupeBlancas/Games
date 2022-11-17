import random
import time

def mostrarIntroduccion():
    print('Estas en una cueva llena de dragones. Frente a ti')
    print('hay dos cuevas. En una de ellas, el dragon es generoso y')
    print('amigable y compartira sus tesoros contigo. El otro dragon')
    print('es codicioso y esta hambriento y te devorará inmediatamente.')
    print()

def elegirCueva():
    cueva = ''
    while cueva != 1 and cueva != 2:
        print('¿A cuál cueva quieres entrar 1 ó 2? ')
        cueva = input()

        return cueva

def explorarCueva(cuevaElegida):
    print('Te aproximas a la cueva...')
    time.sleep(2)
    print('Esta oscura y espeluznante...')
    time.sleep(2)
    print('¡Un dragón aparece subitamente frente a tí! Abre sus fauces...')
    print()
    time.sleep(2)

    cuevaAmigable = random.randint(1,2)

    if cuevaElegida == str(cuevaAmigable):
        print('Te regala su tesoro')
    else:
        print('Te engulle de un bocado')

jugar_de_nuevo = 'si'
while jugar_de_nuevo == 'si' or jugar_de_nuevo == 's':

    mostrarIntroduccion()

    numero_de_cueva = elegirCueva()

    explorarCueva(numero_de_cueva)

    print('¿Quieres jugar de nuevo si/no? ')
    jugar_de_nuevo = input()
