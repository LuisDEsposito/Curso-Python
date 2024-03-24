'''Escribir una función a la que se le pase una cadena del nombre de una ciudad <ciudad> y 
muestre por pantalla el saludo ¡hola bienvenidx a <nombre>!.'''

def saludar_ciudad(nombre):
    mensaje = print(f"Bienvenido a {nombre}")
    return mensaje

def ingresar_ciudad():
    entrada = input("Ingrese la ciudad: ")
    return entrada

entrada = ingresar_ciudad()
saludo = saludar_ciudad(entrada)

