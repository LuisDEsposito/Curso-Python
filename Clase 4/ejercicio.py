"""
A partir de la siguiente cadena:
"gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado... -agrega el comentarista"

Transformala en:

Gordon lanzó su curva...
- Strawberry ha fallado por un pie! -gritó Joe Castiglione.
- Dos pies le corrigió Troop.
- Strawberry menea la cabeza como disgustado... -agrega el comentarista.
"""

cadena_original = "gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado... -agrega el comentarista"
lista_texto = cadena_original.split("&")
lista_texto[0] = lista_texto[0].capitalize() + "..."
lista_texto[1] = "- " + lista_texto[1].capitalize().replace("joe castiglione", "Joe Castiglione")
print(lista_texto)
