# made by Sara Ltaif :)
# pls use it emulating terminal in output console to clean it
# most of the code is in Spanish btw

import os
import sys


# Limpiar la consola
def clear():
    input("Presione ENTER para continuar. ")
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


# Evitar errores con el input, usar siempre
def anti_error(text):
    espacio = "-----------"
    try:
        valor = int(input(text))
        return valor
    except ValueError:
        print(f"{espacio}\n Lo siento! Usted coloco un valor el cual no es un numero")
        clear()
        menu()


# Devuelve boolean, comprueba si existe o no
def checker_triangles(a, b, c):
    if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
        return True
    else:
        return False


# La funcion checker_triangles pero se ve en la consola
def interface():
    espacio = "-----------"
    side_a = anti_error("Introduzca el lado A: ")
    side_b = anti_error("Introduzca el lado B: ")
    side_c = anti_error("Introduzca el lado C: ")
    if checker_triangles(side_a, side_b, side_c):
        print(f"{espacio}\n El triangulo con los lados {side_a}, {side_b} y {side_c} existe."
              f" \n {espacio}")
        clear()
        menu()
    else:
        print(espacio)
        print(f"{espacio}\n Lastimosamente, el triangulo con los lados {side_a}, {side_b} y"
              f" {side_c} NO existe.  \n {espacio}")
        clear()
        menu()


# Decide que hacer a base de lo que se escribio en menu()
def actuator(respuesta):
    espacio = "-----------"
    if respuesta == 0:
        print(espacio)
        print("Adios!")
        sys.exit()
    elif respuesta == 1:
        print(espacio)
        interface()
    else:
        print(f"{espacio}\n Lo siento! Usted coloco un numero incorrecto.")
        clear()
        menu()


# Pregunta al usuario que desea hacer, llamar a esta funcion para iniciar el programa
def menu():
    espacio = "-----------"
    print(espacio)
    print("Que desea hacer?")
    print("Salir del programa: 0 \n Usar la calculadora: 1")
    actuator(anti_error("> "))


bienvenida = "Bienvenido a la calculadora mas epica que no calcula"
print(bienvenida)
menu()
