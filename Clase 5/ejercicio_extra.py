"""
EJERCICIO 1:
Escribe un programa en Python que 
solicite al usuario dos entradas de tipo 
entero, las cuales indican si el usuario
aprobó (1) o no aprobó (0) los exámenes
 A y B respectivamente.
El programa debe convertir estas 
entradas en valores booleanos y mostrarlas
en pantalla.
Además, debes explicar por escrito cómo
funciona la función bool() en Python
y por qué se utiliza en este código.
"""
# nota_examenA = int(input("ingrese 1 si aprobó o 0 si desaprobó: "))
# nota_examenB = int(input("ingrese 1 si aprobó o 0 si desaprobó: "))

# aprobado_A = bool(nota_examenA)
# aprobado_B = bool(nota_examenB)

# print(f"aprobacion examen A: ", aprobado_A)
# print(f"Aprobado examen B: ", aprobado_B)

# A partir de dos variables llamadas nombre y edad debes crear una
# variable que almacene si se cumplen todas las siguientes condiciones,
# y mostrar al usuario True o False:
# nombre sea diferente de cuatro asteriscos ****
# edad sea mayor que 5 y a su vez menor que 20
# Que la longitud de nombre sea mayor o igual a 4  pero a la vez menor que 8
# edad multiplicada por 3 sea mayor que 35
#  Debes ingresar los datos con input():
#  No debes usar funciones, condicionales, bucles o cualquier
# otra instrucción que no hayamos visto


nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
variable_1 = nombre != "****"
variable_2 = edad > 5 and edad < 20
variable_3 = len(nombre) >= 4 and len(nombre) < 8
variable_4 = edad*3 > 35

print("Su nombre es distinto a ****? ", variable_1)
print("Su edad es mayor a 5 y tambien menor a 20? ", variable_2)
print("Su nombre es mas largo que 4 digitos y mas chico que ocho digitos? ", variable_3)
print("Su edad multiplicada por tres, es mayor a treinta y cinco? ", variable_4)
variable_final = variable_1 and variable_2 and variable_3 and variable_4
print("Se cumplen todas las condiciones?  ", variable_final)











