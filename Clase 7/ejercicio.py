
"""
Escribe un programa que genere un número aleatorio entre 1 y 20,
y le pida al usuario que adivine el número. Si el usuario adivina el número,
el programa debe imprimir "¡Adivinaste el número!"
y terminar. Si el usuario no adivina el número,
el programa debe imprimir "El número es mayor"
o "El número es menor", dependiendo de si el número generado
 es mayor o menor que el número ingresado por el usuario.
El programa debe permitir al usuario intentar adivinar
el número 5 veces.
"""

import random

número_aleatorio = random.randint(1, 6)
print(número_aleatorio)
intentos_máximos = 3
intentos_actuales = 0

while True:
    entrada = int(input("Adivina el número entre 1 y 6 ✨: "))
    intentos_actuales += 1
    if entrada == número_aleatorio:
        print("Adivinaste el número! 🔥")
        break
    else:
        if entrada < número_aleatorio:
            print("El número es mayor")
        else:
            print("El número es menor")
    if intentos_actuales == intentos_máximos:
        print("Se acabaron tus intentos...")
        break


