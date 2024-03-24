"""
A partir del código:
try:
    x = float(input("Número 1: "))
    y = float(input("Número 2: "))
    division = round(x / y, 2)
except:
    print("Algo salió mal...")
else:   # es opcional, se ejecuta cuando no hay errores
    print(division)
finally:  # es opcional, siempre se ejecuta, haya o no errores
    print("Fin.")
Crear un bucle while True, y si algo salió mal, pedir otra vez los números al usuario.
Crear funciones según las buenas prácticas. No usar variables globale.
"""
while True:
    try:
        def entrada_numeros():
            x = float(input("Número 1: "))
            y = float(input("Número 2: "))
            division = round(x / y, 2)
            return division
    except:
        def error():
            print("Lo siento,hubo un error, por favor intente de nuevo.")
        continue
    else:   # es opcional, se ejecuta cuando no hay errores 
        def mensaje():
            print(f"El resultado de la división de los números es {entrada_numeros}")
        break
    finally:  # es opcional, siempre se ejecuta, haya o no errores
        print("Ah finalizado el proceso.")

