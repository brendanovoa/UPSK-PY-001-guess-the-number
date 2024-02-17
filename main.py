import random

# Número aleatorio
numero = random.randint(1, 100)
print(numero)
print("Número secreto generado. ¡Comienza el juego!")

lista_jugadora = []
lista_ordenador = []

# Bucle para intentar adivinar el número
while True:
    # Turno de la usuaria
    jugadora = int(input("Intenta adivinar el número secreto. Ingresa un número del 1 al 100: "))
    lista_jugadora.append(jugadora)

    if jugadora < numero:
        print('El número secreto es mayor')
    elif jugadora > numero:
        print('El número secreto es menor')
    elif jugadora == numero:
        print('¡Adivinaste!')
        print(f'Intentos de la jugadora: {lista_jugadora}')
        print(f'Intentos de la computadora: {lista_ordenador}')
        break

    # Turno de la computadora
    ordenador = random.randint(1, 100)
    lista_ordenador.append(ordenador)
    print(f"La computadora dice que el número secreto es: {ordenador}")

    if ordenador < numero:
        print('El número secreto es mayor')
    elif ordenador > numero:
        print('El número secreto es menor')
    elif ordenador == numero:
        print('¡La computadora adivinó!')
        print(f'Intentos de la jugadora: {lista_jugadora}')
        print(f'Intentos de la computadora: {lista_ordenador}')
        break

# print("¿Quieres jugar de nuevo?")