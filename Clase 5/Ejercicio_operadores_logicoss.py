"""
En una lista encontraremos diferentes operaciones relacionales, 
calcular mentalmente el resultado de cada expresión y 
almacenarlo en una nueva lista que contendrá únicamente valores lógicos True y False.

"""
expresiones = [
False == True,
10 >= 2*4,
33/3 == 11,
True > False,
True*5 == 2.5*2
]
expresión_0 = False == True
expresión_1 = 10 >= 2*4
expresión_2 = 33/3 == 11
expresión_3 = True > False
expresión_4 = True*5 == 2.5*2
tupla = (expresión_0, expresión_2, expresión_3, expresión_4)
print(tupla)
