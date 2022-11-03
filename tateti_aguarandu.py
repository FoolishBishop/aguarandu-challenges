# made by Sara Ltaif :)
# pls use it emulating terminal in output console to clean it
# most of the code is in Spanish btw


import os
import sys

nick_p1 = "Jugador 1"
nick_p2 = "Jugador 2"
wins_p1 = 0
wins_p2 = 0
draw = 0


# funciones de limpieza de consola y deteccion de errores

def clear():
    input("Presione ENTER para continuar\n>>> ")
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def instant_clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


# evitar errores con el input, usar siempre
def anti_error(text):
    espacio = "-----------"

    while True:
        try:
            valor = int(input(text))
            break
        except ValueError:
            print(f"{espacio}\n Lo siento! Usted coloco un valor el cual no es un numero")
            clear()
    return valor


# SOLO PARA TURNOS!!!
def anti_error_special_turns(text):
    espacio = "-----------"

    while True:
        try:
            valor = int(input(text))
            return valor
        except ValueError:
            print(f"{espacio}\n Lo siento! Usted coloco un valor el cual no es un numero, intente de nuevo")


# funciones para mostrar las graficas

# sub de dibujo_real
def dibujo(positions):
    positions = list(positions)
    espacio = "---------"
    line_1 = "1 | 2 | 3"
    line_2 = "4 | 5 | 6"
    line_3 = "7 | 8 | 9"
    print(f"{positions[0]} | {positions[1]} | {positions[2]}     {line_1}\n{espacio}     {espacio}")
    print(f"{positions[3]} | {positions[4]} | {positions[5]}     {line_2}\n{espacio}     {espacio}")
    print(f"{positions[6]} | {positions[7]} | {positions[8]}     {line_3}")


def dibujo_real(player_1, player_2):
    positions = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    for numeros in player_1:
        positions[numeros - 1] = "X"

    for numeros in player_2:
        positions[numeros - 1] = "O"
    dibujo(positions)


# funciones para verificar quien gano


# sub de checking_results
def comprobar_gano(lista_jugador):
    lista_jugador = list(lista_jugador)
    combinaciones = [[1, 2, 3], [1, 4, 7], [1, 5, 9], [2, 5, 8], [3, 6, 9], [3, 5, 7], [4, 5, 6], [7, 8, 9]]
    boolean = False

    for posible in combinaciones:
        if set(posible).issubset(set(lista_jugador)):
            boolean = True
    return boolean


# sub de checking_results
def comprobar_empate(player_1, player_2):
    ambas_listas = player_1 + player_2
    empate = False

    for number in range(1, 10):
        if number in ambas_listas:
            empate = True
        else:
            return False
    return empate


def checking_results(player_1, player_2):
    global nick_p1, nick_p2, wins_p1, wins_p2, draw

    if comprobar_gano(player_1):
        instant_clear()
        dibujo_real(player_1, player_2)
        input(f"**************\nGano {nick_p1}!\n**************\n Presione ENTER para continuar.\n>>> !")
        wins_p1 += 1
        menu()
    elif comprobar_gano(player_2):
        instant_clear()
        dibujo_real(player_1, player_2)
        input(f"**************\nGano {nick_p2}!\n**************\n Presione ENTER para continuar.\n>>> ")
        wins_p2 += 1
        menu()
    elif comprobar_empate(player_1, player_2):
        instant_clear()
        dibujo_real(player_1, player_2)
        input("Hubo un empate!\n Presione ENTER para continuar.\n>>> ")
        draw += 1
        menu()


# funciones para el funcionamiento de turnos


def turnos_player_1(player_1, player_2):
    global nick_p1
    ambos_jugadores_posiciones = player_1 + player_2

    while True:
        instant_clear()
        dibujo_real(player_1, player_2)
        intento_p1 = anti_error_special_turns(f"Turno de {nick_p1}.\n>>> ")
        if intento_p1 not in ambos_jugadores_posiciones:
            player_1.append(intento_p1)
            dibujo_real(player_1, player_2)
            checking_results(player_1, player_2)
            break
        else:
            print("Lo siento! el valor dado ya fue usado. Intente de nuevo")
            clear()
    return turnos_player_2(player_1, player_2)


def turnos_player_2(player_1, player_2):
    global nick_p2
    ambos_jugadores_posiciones = player_1 + player_2

    while True:
        instant_clear()
        dibujo_real(player_1, player_2)
        intento_p2 = anti_error_special_turns(f"Turno de {nick_p2}.\n>>> ")
        if intento_p2 not in ambos_jugadores_posiciones:
            player_2.append(intento_p2)
            dibujo_real(player_1, player_2)
            checking_results(player_1, player_2)
            break
        else:
            print("Lo siento! el valor dado ya fue usado. Intente de nuevo")
            clear()
    return turnos_player_1(player_1, player_2)


# funciones para el menu

def change_names():
    instant_clear()
    global nick_p1, nick_p2

    while True:
        new_name_p1 = str(input("Ingrese el nuevo nombre del jugador 1:\n>>> "))
        if new_name_p1 == nick_p2:
            print("Lo siento! ese nombre ya lo esta usando el jugador 2. Intente de nuevo")
        elif new_name_p1 == nick_p1:
            print("Al parecer no queria cambiar el nombre!")
            break
        else:
            print(f"El nuevo nombre del jugador 1 sera {new_name_p1}.")
            nick_p1 = new_name_p1
            break

    while True:
        new_name_p2 = str(input("Ingrese el nuevo nombre del jugador 2:\n>>> "))
        if new_name_p2 == nick_p1:
            print("Lo siento! ese nombre ya lo esta usando el jugador 1. Intente de nuevo")
        elif new_name_p2 == nick_p2:
            print("Al parecer no queria cambiar el nombre!")
            break
        else:
            print(f"El nuevo nombre del jugador 2 sera {new_name_p2}.")
            nick_p2 = new_name_p2
            break
    clear()
    menu()


def view_stats():
    global nick_p1, nick_p2, wins_p1, wins_p2, draw
    instant_clear()
    print(f"Ganadas por {nick_p1}: {wins_p1}\nGanadas por {nick_p2}: {wins_p2}\nEmpates: {draw}")
    input("Presione ENTER para continuar")
    menu()


# funcion para decidir que hacer a base del input
def actuator(respuesta):
    global nick_p1, nick_p2
    espacio = "-----------"

    if respuesta == 0:
        print(espacio)
        print("Adios!")
        sys.exit()
    elif respuesta == 1:
        turnos_player_1([], [])
    elif respuesta == 2:
        change_names()
    elif respuesta == 3:
        view_stats()
    else:
        print(f"{espacio}\n Lo siento! Usted coloco un numero incorrecto.")
        clear()
        menu()


# el menu
def menu():
    instant_clear()
    actuator(anti_error("Que desea hacer?\n Salir: 0\n Nueva partida: 1\n Cambiar el nombre de los jugadores: 2\n "
                        "Estadisticas: 3\n>>> "))


bienvenida_instrucciones = "Bienvenido al juego del TaTeTi, para seleccionar lo que quiere hacer presione uno de los " \
                           "numeros dados. "
print(bienvenida_instrucciones)
menu()
