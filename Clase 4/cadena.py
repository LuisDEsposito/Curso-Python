cadena = " esta es una prueba con Pithon  🔥🔥   "
print(cadena)
print("upper:", cadena.upper())
print("lower:", cadena.lower())
print("title:", cadena.title())

cadena = cadena.strip()
print(cadena)
print("capitalize:", cadena.capitalize())
cadena = cadena.capitalize()
print(cadena)
print("replace:", cadena.replace("pithon", "Python"))
print("find:", cadena.find("a"))
print("find:", cadena.find("A"))
print("isdigit:", "1234".isdigit())
print("isdigit:", "a1234".isdigit())
print("count", cadena.count("🔥"))
print("count", cadena.count("E") + cadena.count("e"))

print("  Esta es una Prueba".strip().upper().replace("E", "3"))
x = 232345  # entero <int>
print(x.is_integer())

cadena = "esta es una prueba de python"
lista = cadena.split("e")
print(lista)
print(len(lista))


lista_de_fruta = ["limon", "palta", "sandia"]
cadena_de_fruta = "-".join(lista_de_fruta)
print(lista_de_fruta)
print(cadena_de_fruta)

