# ingresar dos funciones. sumar() que suma 2 numeros y devuelve 1 entero.
#  la segunda funcion se llama ingresar_numeros. que solicita el ingreso de los dos numero y devuelve ambos.

def sumar(numero_1, numero_2):
    suma = numero_1 + numero_2
    return suma


def ingresar_numeros():
    numero_1 = int(input("Ingrese un número: "))
    numero_2 = int(input("Ingrese otro número: "))
    return numero_1, numero_2



def main(): #esta función realiza el llamamiento de como queremos ejecutar las funciones anteriores.
    numero_1, numero_2 = ingresar_numeros() # desempaquetar
    suma = sumar(numero_1, numero_2)
    tupla = (numero_1, numero_2)
    print(f'El resultado de la suma es {suma}')
    print(f'Los números elegidos fueron: {tupla}')

main()




