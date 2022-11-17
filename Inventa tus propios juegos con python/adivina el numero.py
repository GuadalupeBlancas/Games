# Juego adivina el número
import random

intentos = 0

print('Hola, como te llamas')
nombre = input()

numero = random.randint(1,20)
print('Bueno '+nombre+' estoy pensando en un número entre 1 y 20')

while intentos < 6:
    print('Intenta adivinar')
    estimacion = input()
    estimacion = int(estimacion)

    intentos = intentos + 1

    if estimacion < numero:
        print('Tu estimación es muy baja')

    if estimacion > numero:
        print('Tu estimacion es muy alta')

    if estimacion == numero:
        break

if estimacion == numero:
    intentos = str(intentos)
    print('Buen trabajo ' +nombre+ 'Haz adivinado en '+intentos+ ' intentos')

if estimacion != numero:
    numero = str(numero)
    print('pues no, el numero que estaba pensando era '+numero)