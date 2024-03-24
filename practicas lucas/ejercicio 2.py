# Crea un programa que tome una cadena de texto como entrada del usuario.
# Luego, muestra por pantalla los primeros tres caracteres de la cadena, 
# seguidos por los tres últimos caracteres. 
# Además, concatena ambos subconjuntos y muestra el resultado.

cadena_de_texto = input("Ingrese una frase: ")
primeros_3 = cadena_de_texto[0:3]
ultimos_3 = cadena_de_texto[-3:]
concatenados = [primeros_3, ultimos_3]

print(primeros_3)
print(ultimos_3)
print(concatenados)