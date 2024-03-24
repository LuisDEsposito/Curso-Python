"""En una lista encontraremos diferentes operaciones lógicas. 
Calcular mentalmente el resultado de cada expresión y almacenarlo en 
una nueva lista la cual contendrá únicamente valores lógicos True y False. 
"""

expresiones = [
not False,
not 3 == 5,
33/3 == 11 and 5 > 2,
True or False,
True*5 == 2.5*2 or 123 >= 23,
12 > 7 and True < False
]

expresion_1 = expresiones[0]
expresion_2 = expresiones[1]
expresion_3 = expresiones[2]
expresion_4 = expresiones[3]
expresion_5 = expresiones[4]
expresion_6 = expresiones[5]

diccionario = {
"expresion_1" : expresion_1,
"expresion_2" : expresion_2,
"expresion_3" : expresion_3,
"expresion_4" : expresion_4,
"expresion_5" : expresion_5,
"expresion_6" : expresion_6
}

print(diccionario)


