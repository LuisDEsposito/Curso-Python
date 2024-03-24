#Clase 9, diapositiva 20
# Paso por referencia.

def doblar_valores(numeros):
    for i,n in enumerate(numeros): 
        numeros[i] *= 2

lista_random = [1, 2, 3, 4, 5, 6]
doblar_valores(lista_random)

print(lista_random)