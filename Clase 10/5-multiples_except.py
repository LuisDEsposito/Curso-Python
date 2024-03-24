# Atrapar errores en except.
# a partir del codigo ✅ Si el usuario presionar "intro" sin ingresar nada, entonces mostrar el
# mismo mensaje que el del except KeyboardInterrupt

# try:
#     numero = input("Número: ")
#     resultado = 6 / int(numero)
#     print(resultado)
# except ValueError:
#     print("No se puede dividir entre un entero y una cadena")
# except ZeroDivisionError:
#     print("No se puede dividir por cero")
# except KeyboardInterrupt:
#     print("\nAcabas de salir del programa")
# except Exception as mensaje:
#     print("Ha ocurrido un error:", type(mensaje))

try:
    numero = input("Número: ")
    if not numero:     # if numero == "":
        raise KeyboardInterrupt
    resultado = 6 / int(numero)
    print(resultado)
except ValueError:
    print("No se puede dividir entre un entero y una cadena")
except ZeroDivisionError:
    print("No se puede dividir por cero")
except KeyboardInterrupt:
    print("\nAcabas de salir del programa")
except Exception as mensaje:
    print("Ha ocurrido un error:", type(mensaje))

"""
Tomando la solución del ejercicio pasado, en lugar de devolver None al dividir entre cero,
tienes que capturar una excepción que muestre por pantalla el mensaje:
"No se puede dividir por cero" Además, capturar otros posibles errores.
def dividir(a, b):
    if b == 0:
        return None
    else:
        return a / b
resultado = dividir(10, 0)
print(resultado)
"""

def ingresar_numeros() -> tuple[float, float]:
    while True:
        try:
            numero_1 = float(input("Número 1: "))
            numero_2 = float(input("Número 2: "))
        except ValueError:
            print("Debes ingresar un número, no otros caracteres")
            continue
        except KeyboardInterrupt:
            print("Sales del programa\n")
            exit()
        except Exception as error:
            print(type(error))
        return numero_1, numero_2
def main():
    numero_1, numero_2 = ingresar_numeros()
    division = (numero_1/numero_2)
    if division is False:
        print("No se pudo realizar la división.")
    else:
        print(f"El resultado de la división es {division}")

main()