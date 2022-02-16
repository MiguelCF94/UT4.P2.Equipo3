# -- coding: utf-8 --
from time import sleep

#Array del dibujo del ahorcado
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

#Lista para comprobar las tildes
tildes=['á','é','í','ó','ú']

#Método que da la bienvenida al jugador
def bienvenida():
    print('*' * 37)
    print('* Bienvenido al juego del ahorcado *')
    print('*' * 37)


#Método que pide la palabra al jugador uno a adivinar
#Prepara la cadena que muestra la longitud de la palabra
#e inicializa un array vacio
def inicializarJuego():
    palabra = input('Jugador 1, introduzca la palabra que el segundo jugador tendrá que adivinar ').lower()
    tablero = ['_'] * len(palabra)
    return tablero, palabra, []


#Método para mostrar la posicion del muñeco del ahorcado dependiendo de los errores
def mostrarEscenario(errores):
    print(MUNECO[errores])


#Método que muestra la cadena con guiones bajos con la longitud de la palabra
#y muestra las letras erroneas
def mostrarTablero(tablero, letrasErroneas):
    for casilla in tablero:
        print(casilla, end=' ')
    print()
    print()
    if len(letrasErroneas) > 0:
        print('Letras erróneas:', *letrasErroneas)
        print()


#Lógica de pedir una letra al segundo jugador que comprueba si es una única letra
#si no es asi, avisa al jugador 2 que ha hecho mal.
#Si la letra ya se uso anteriormente que ya es repetida.

def pedirLetra(tablero, letrasErroneas):
    valida = False
    while not valida:
        letra = input('Introduce una letra: ').lower()
        valida = ('a' <= letra <= 'z' or letra=='ñ' or letra in tildes)and len(letra) == 1  # es una letra
        if not valida:
            if len(letra)>1:
                print('Error, no se puede introducir más de un caracter')
            else:
                print('Error, no puede ser un símbolo ni un número.')
        else:
            valida = letra not in tablero + letrasErroneas
            if not valida:
                print('Letra repetida, ¿Por qué no intenta otra letra distinta?')

    return letra

#Método que procesa la letra introducida, si ha sido acertada se llama al método
#de actualizar el tablero cambiando el guión bajo por la letra si es correcta.
#Si la letra es erronea se añade a la lista de letras erroneas.
def procesarLetra(letra, palabra, tablero, letrasErroneas):
    if letra in palabra:
        print('Has acertado una letra.')
        actualizarTablero(letra, palabra, tablero)
    else:
        print('Has fallado.')
        letrasErroneas.append(letra)

#Método que actualiza el tablero cambiando el guión bajo por la palabra acertada
def actualizarTablero(letra, palabra, tablero):
    for indice, letra_palabra in enumerate(palabra):
        if letra == letra_palabra:
            tablero[indice] = letra

#Método que controla si se ha adivinado la palabra
#(si no existen guiones bajos ha sido adivinada)
def comprobarPalabra(tablero):
    return '_' not in tablero


# Bucle principal de juego
def jugar():
    try:
        tablero, palabra, letrasErroneas = inicializarJuego()  
        while len(letrasErroneas) < len(MUNECO): 
            mostrarEscenario(len(letrasErroneas))  
            mostrarTablero(tablero, letrasErroneas)  
            if len(letrasErroneas)<len(MUNECO)-1:
                letra = pedirLetra(tablero, letrasErroneas)  
                procesarLetra(letra, palabra, tablero, letrasErroneas)  
                if comprobarPalabra(tablero):  
                    print('¡Enhorabuena, lo has logrado!')
                    break
            else:
                print(f'¡Lo siento! ¡Has perdido! La palabra a adivinar era {palabra}.')
                break;
    
        
    except IndexError:
        print()    

#Método para poder repetir la partida cuantas veces se quiera
def repetir():
    print()
    return input('Deseas jugar otra vez (introduce s para sí o cualquier otra cosa para no): ').lower()




if __name__ == '__main__':
    bienvenida()
    sleep(2)
    while True:
        jugar()
        if repetir() != 's': break


