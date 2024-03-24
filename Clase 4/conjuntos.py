conjunto = {1,2,3,4,5,6,7,8,-10}
conjuntoa = {12, 13, 3, 5, 5, 6}
conjunto_2 = "Copy: ", conjunto.copy()
print(conjunto_2)
conjunto_3 = "Isdisjoint: ", conjunto.isdisjoint(conjuntoa)
print(conjunto_3)
conjunto_4 = "Issubset: ", conjunto.issubset(conjuntoa)
print(conjunto_4)
conjunto_5 = "Union: ", conjunto.union(conjuntoa)
print(conjunto_5)
conjunto_6 = "Difference: ", conjunto.difference(conjuntoa)
print(conjunto_6)
