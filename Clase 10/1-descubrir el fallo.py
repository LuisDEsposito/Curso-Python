"""
En la función de nuestro ejercicio hay un fallo potencial,
averigua cuándo sucede y retorna el valor None en ese caso especial,
en cualquier otro caso devuelve el resultado normal de la función.

Pista: Valor indeterminado
"""

def dividir(a, b):
    if b == 0:
        return
    return a/b

resultado = dividir(100,10)
print(resultado)