'''numero = 0 
while numero <= 5:
    print("El numero es igual a", numero)
    numero += 1'''

# while True:
    # print("♾️ Esto es un bucle infinito")
    

#while False:
    # print("♾️ Esto es un bucle infinito")



'''while True:
  entrada = input('escriba salir ')
  if entrada == 'salir':
        print('Lo conseguiste wey')
        break'''

'''
contador = 0

while contador < 6:
    contador += 1
    if contador == 3:
        continue
    print(contador)

x = 0
while x > 5:
    x += 1
    if x == 3:
        pass
    print(x)'''

print("LISTAS")
lista = [1, 2, 3, 4, 5, 6]

for elemento in lista:
    print(elemento)

print("TUPLAS")
conjunto = (1, 2, 3, 4, 5, 6)

for elemento in conjunto:
    print(elemento)

print("CONJUNTOS")
conjunto = {1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 7}

for elemento in conjunto:
    print(elemento)

print("DICCIONARIOS")
diccionario = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f"}

print("*** CLAVES v1")
for clave in diccionario:
    print(clave)

print("*** CLAVES v2")
for clave in diccionario.keys():
    print(clave)

print("*** VALORES")
for valor in diccionario.values():
    print(valor)

print("*** CLAVES Y VALORES")
for clave, valor in diccionario.items():
    print(f"Clave: {clave}, Valor: {valor}")

print("CADENAS")
cadena = "Las cadenas..."

for caracter in cadena:
    print(caracter, end="\n")



for n in range(10):
    print(f"n vale {n}")

print()
for n in range(1, 5):
    print(f"n vale {n}")

print()
for n in range(3, 10, 2):
    print(f"n vale {n}")




    


