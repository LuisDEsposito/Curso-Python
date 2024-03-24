# Crea un programa que inicie con una lista de números enteros. 
# Luego, solicita al usuario un número entero y 
# un índice para reemplazar un elemento en la lista por el nuevo número ingresado en el índice ingresado. 
# Imprime la lista resultante.


lista_inicial = [99, 155, 200, 1000, 7983538, 2333, 6, 6, 2, 155]
número_usuario = int(input('Ingrese un número: '))
indice_modificar = int(input('Ahora ingrese el número del indice que desee cambiar por el número ingresado: '))

if indice_modificar > len(lista_inicial):
    print("Lo siento, el indice ingresado es mayor a los existentes.")
else:
    lista_inicial[indice_modificar] = número_usuario

print(lista_inicial)
