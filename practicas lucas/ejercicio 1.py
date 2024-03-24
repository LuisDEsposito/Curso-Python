'''Escribe un programa que solicite al usuario dos números enteros. 
Luego, muestra por pantalla la suma, resta, 
multiplicación y división de esos dos números.'''

número_1 = int(input("Número 1: "))
número_2 = int(input("Número 2: "))
suma = número_1 + número_2
resta = número_1 - número_2
multiplicacion = número_1 * número_2
división = número_1 / número_2

print(f'''Los números ingresados fueron {número_1} y {número_2}.
La suma de estos números es {suma}, la resta de estos números es {resta};
si los multiplicas, el resultado es {multiplicacion} y si los divides, el resultado es {división}''')