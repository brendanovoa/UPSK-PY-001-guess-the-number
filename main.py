import random

# Número aleatorio
def generar_numero_secreto():
    return random.randint(1, 100)

# Turno de la jugadora
def turno_jugadora(numero_secreto, lista_jugadora):
    intento_jugadora = int(input("Intenta adivinar el número secreto. Ingresa un número del 1 al 100: "))
    lista_jugadora.append(intento_jugadora)
    if intento_jugadora < numero_secreto:
        print('El número secreto es mayor')
    elif intento_jugadora > numero_secreto:
        print('El número secreto es menor')
    elif intento_jugadora == numero_secreto:
        print('¡Adivinaste!')
        return True
    return False

# Turno de la computadora
def turno_ordenador(numero_secreto, lista_ordenador):
    intento_ordenador = random.randint(1, 100)
    lista_ordenador.append(intento_ordenador)
    print(f"La computadora dice que el número secreto es: {intento_ordenador}")
    if intento_ordenador < numero_secreto:
        print('El número secreto es mayor')
    elif intento_ordenador > numero_secreto:
        print('El número secreto es menor')
    elif intento_ordenador == numero_secreto:
        print('¡La computadora adivinó!')
        return True
    return False

def juego():
    numero_secreto = generar_numero_secreto()
    print("Número secreto generado. ¡Comienza el juego!")
    lista_jugadora = []
    lista_ordenador = []
    while True:
        if turno_jugadora(numero_secreto, lista_jugadora):
            print(f'Intentos de la jugadora: {lista_jugadora}')
            print(f'Intentos de la computadora: {lista_ordenador}')
            break
        if turno_ordenador(numero_secreto, lista_ordenador):
            print(f'Intentos de la jugadora: {lista_jugadora}')
            print(f'Intentos de la computadora: {lista_ordenador}')
            break
        # print("¿Quieres jugar de nuevo?")

if __name__ == "__main__":
    juego()