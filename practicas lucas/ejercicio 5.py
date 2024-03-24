"""Crea un programa que solicite al usuario ingresar nombres separados por comas. 
Luego, crea un conjunto con los nombres ingresados y 
muestra por pantalla la cantidad de nombres únicos en el conjunto."""

entrada_nombres = (input('Ingrese varios nombres(separados por comas): '))
conjunto_nombres = entrada_nombres.split(",")

print(entrada_nombres)

