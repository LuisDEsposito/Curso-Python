# Anotaciones de tipo o type hints

# def saludar_ciudad(nombre: str) -> str: #tira un error en la str ya que no hay declarado ningun return para poder devolver una str.
    # print(f"Bienvenido a {nombre.upper()}") # las anotaciones de tipo permiten ver que herramientas podemos usar según el tipo de dato que ingresamos.
    

# entrada = input("Ingrese la ciudad: ")
# saludar_ciudad(entrada)

# Forma un poco mas prolija: 
def saludar_ciudad(nombre: str) -> str:
    mensaje = f"Bienvenido a {nombre.upper()}"
    return mensaje

entrada = input("Ingrese la ciudad: ")
saludar_ciudad(entrada)
