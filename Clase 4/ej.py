"""Transformala en:

Gordon lanzó su curva...
- Strawberry ha fallado por un pie! -gritó Joe Castiglione.
- Dos pies le corrigió Troop.
- Strawberry menea la cabeza como disgustado... -agrega el comentarista.
"""
cadena_original = "gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado... -agrega el comentarista"
relato_ok = cadena_original.split("&")
relato_ok[0] = relato_ok[0].capitalize() + "..." 
relato_ok[1] = relato_ok[1].capitalize().replace("joe castiglione", "Joe Castiglione")
relato_ok[2] = relato_ok[2].capitalize().split("-") # type: ignore
relato_ok[3] = relato_ok[3].capitalize()
# print(relato_ok)


my_set_1 = set([1, 2, 3])
my_set_2 = set([3, 4, 5])
my_new_set = my_set_1.union(my_set_2)
print(my_new_set)


my_set_1 = set([1, 2, 3])
my_set_2 = set([3, 4, 5])
my_new_set = my_set_1.intersection(my_set_2)
print(my_new_set)


my_set_1 = set([1, 2, 3])
my_set_2 = set([3, 4, 5])
my_new_set = my_set_1.difference(my_set_2)
print(my_new_set)




