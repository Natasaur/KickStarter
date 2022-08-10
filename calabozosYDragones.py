# Este juego, el jugador está en una tierra llena de dragones. 
# Todos los dragones viven en cuevas junto a sus grandes montones de tesoros
# encontrados. Algunos dragones son amigables, y compartirán sus tesoros contigo.
# Otros son codiciosos y hambrientos, y se comerán a cualquiera que entre a su
# cueva. El jugador se encuentra frente a dos cuevas, una con un dragón amigable
# y la otra con un dragón hambriento. El jugador tiene que elegir entre las dos.
# Abre una nueva ventana del editor de archivos haciendo clic en el menú 
# File (Archivo) ► New Window (Nueva Ventana). En la ventana vacía que aparece 
# escribe el código fuente y guárdalo como dragón.py. Luego ejecuta el programa
# pulsando F5.

import random
import time

def mostrarIntroduccion():
    print('Estas en una tierra llena de dragones. Frente a ti')
    time.sleep(2)
    print('hay dos cuevas. En una de ellas, el dragon es generoso y')
    time.sleep(2)
    print('amigable y compartira su tesoro contigo. El otro dragon')
    time.sleep(2)
    print('es codicioso y esta hambriento, y te devorara inmediatamente.')
    time.sleep(2)
    print()

def elegirCueva():
    cueva = 0
    while cueva !=1 and cueva !=2:
        print('¿A que cueva vas a entrar? ¿1 o 2?')
        cueva = int(input())

    return cueva

def explorarCueva(cuevaElegida):
    print('Te aproximas a la cueva...')
    time.sleep(2)
    print('Es oscura y espeluznante...')
    time.sleep(2)
    print('¡Un gran dragon aparece subitamente ante ti! Abre sus fauces y...')
    print()
    time.sleep(3)

    cuevaAmigable = random.randint(1,2)

    if cuevaElegida == cuevaAmigable:
        print('¡Te ha regalado un tesoro!')
    else:
        print('¡Te engulle de un bocado!')

# print('¿Quieres jugar de nuevo?')
# jugarDeNuevo = input('Escribe "Si" o "No"')
jugarDeNuevo = 'Si'

while jugarDeNuevo == 'Si':
    #2break
    if jugarDeNuevo == 'Si':
        mostrarIntroduccion()
        numCueva = elegirCueva()
        explorarCueva(numCueva)
        print('¿Quieres jugar de nuevo?')
        print('Escribe "Si" o "No"')
        jugarDeNuevo = input()
    

