"""GUESS THE NUMBER"""

import random
from colorama import init, Fore, Style
init()

# Número aleatorio
def generar_numero_secreto():
    return random.randint(1, 100)

# Turno de la jugadora
def turno_jugadora(numero_secreto, lista_jugadora):
    intento_jugadora = int(input(f"{Fore.MAGENTA}Intenta adivinar el número secreto. Ingresa un número del 1 al 100: {Style.RESET_ALL}"))
    print()
    lista_jugadora.append(intento_jugadora)
    if intento_jugadora < numero_secreto:
        print(f'{Fore.RED}El número secreto es mayor{Style.RESET_ALL}')
        print()
    elif intento_jugadora > numero_secreto:
        print(f'{Fore.RED}El número secreto es menor{Style.RESET_ALL}')
        print()
    elif intento_jugadora == numero_secreto:
        print(f'{Fore.GREEN}¡Adivinaste!{Style.RESET_ALL}')
        print()
        return True
    return False

# Turno de la computadora
def turno_ordenador(numero_secreto, lista_ordenador):
    intento_ordenador = random.randint(1, 100)
    lista_ordenador.append(intento_ordenador)
    print(f"{Fore.BLUE+Style.BRIGHT}La computadora dice que el número secreto es: {intento_ordenador}{Style.RESET_ALL}")
    print()
    if intento_ordenador < numero_secreto:
        print(f'{Fore.RED}El número secreto es mayor{Style.RESET_ALL}')
        print()
    elif intento_ordenador > numero_secreto:
        print(f'{Fore.RED}El número secreto es menor{Style.RESET_ALL}')
        print()
    elif intento_ordenador == numero_secreto:
        print(f'{Fore.GREEN}¡La computadora adivinó!{Style.RESET_ALL}')
        print()
        return True
    return False

# Volver a jugar
def nuevo_juego():
    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n)")
    print()
    return jugar_de_nuevo.lower() == 's'

# Lógica del juego
def juego():
    while True:
        print(f"{Fore.GREEN}********************************************************{Style.RESET_ALL}")
        print(f"{Fore.GREEN}*             ¡Bienvenida a Guess the Number!          *{Style.RESET_ALL}")
        print(f"{Fore.GREEN}********************************************************{Style.RESET_ALL}")
        print()
        numero_secreto = generar_numero_secreto()
        print(f"{Fore.YELLOW}Número secreto generado. ¡Comienza el juego!{Style.RESET_ALL}")
        print()
        lista_jugadora = []
        lista_ordenador = []
        while True:
            if turno_jugadora(numero_secreto, lista_jugadora):
                print(f'{Fore.YELLOW}Intentos de la jugadora: {lista_jugadora}{Style.RESET_ALL}')
                print(f'{Fore.YELLOW}Intentos de la computadora: {lista_ordenador}{Style.RESET_ALL}')
                print()
                break
            if turno_ordenador(numero_secreto, lista_ordenador):
                print(f'{Fore.YELLOW}Intentos de la jugadora: {lista_jugadora}{Style.RESET_ALL}')
                print(f'{Fore.YELLOW}Intentos de la computadora: {lista_ordenador}{Style.RESET_ALL}')
                print()
                break
        if not nuevo_juego():
            print(f"{Fore.YELLOW}¡Adios!{Style.RESET_ALL}")
            break

if __name__ == "__main__":
    juego()