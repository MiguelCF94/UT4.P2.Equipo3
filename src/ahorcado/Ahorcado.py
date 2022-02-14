# -- coding: utf-8 --
MUNECO = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']


def bienvenida():
    print('*' * 37)
    print('* Bienvenido al juego del ahorcado *')
    print('*' * 37)



def inicializar_juego():
    palabra = input('Introduzca la palabra a adivinar ').lower()
    tablero = ['_'] * len(palabra)
    return tablero, palabra, []



def mostrar_escenario(errores):
    print(MUNECO[errores])



def mostrar_tablero(tablero, letras_erroneas):
    for casilla in tablero:
        print(casilla, end=' ')
    print()
    print()
    if len(letras_erroneas) > 0:
        print('Letras erróneas:', *letras_erroneas)
        print()



def pedir_letra(tablero, letras_erroneas):
    valida = False
    while not valida:
        letra = input('Introduce una letra: ').lower()
        valida = ('a' <= letra <= 'z' or letra=='ñ') and len(letra) == 1  # es una letra
        if not valida:
            print('Error, no puede ser un símbolo ni un número.')
        else:
            valida = letra not in tablero + letras_erroneas
            if not valida:
                print('Letra repetida, ¿Por qué no intenta otra nueva?')

    return letra


def procesar_letra(letra, palabra, tablero, letras_erroneas):
    if letra in palabra:
        print('Has acertado una letra.')
        actualizar_tablero(letra, palabra, tablero)
    else:
        print('Has fallado.')
        letras_erroneas.append(letra)


def actualizar_tablero(letra, palabra, tablero):
    for indice, letra_palabra in enumerate(palabra):
        if letra == letra_palabra:
            tablero[indice] = letra


def comprobar_palabra(tablero):
    return '_' not in tablero


# bucle principal de juego
def jugar_al_ahorcado():
    try:
        tablero, palabra, letras_erroneas = inicializar_juego()  # paso 1
        while len(letras_erroneas) < len(MUNECO):  # pasos 7 y 8
            mostrar_escenario(len(letras_erroneas))  # paso 2
            mostrar_tablero(tablero, letras_erroneas)  
            if len(letras_erroneas)<len(MUNECO)-1:
                letra = pedir_letra(tablero, letras_erroneas)  # paso 4
                procesar_letra(letra, palabra, tablero, letras_erroneas)  # paso 5
                if comprobar_palabra(tablero):  # paso 6
                    print('¡Enhorabuena, lo has logrado!')
                    break
            else:
                print(f'¡Lo siento! ¡Has perdido! La palabra a adivinar era {palabra}.')
                break;
    
        
    except IndexError:
        print()    


def jugar_otra_vez():
    return input('Deseas jugar otra vez (introduce s para sí o cualquier otra cosa para no): ')




if __name__ == '__main__':


    bienvenida()
    while True:
        jugar_al_ahorcado()
        if jugar_otra_vez() != 's': break

