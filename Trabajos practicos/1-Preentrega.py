def registrar_usuario():
    email = input("Email: ")
    password = input("Password: ")
    formulario = {"email": email, "password": password}
    usuarios_pagina.append(formulario)
    print(usuarios_pagina)
    prueba: list[str] = []
    prueba += "asdf"
    #formulario["email"] = email
    #formulario["password"] = password
    #formulario = dict.fromkeys(formulario.keys(), [])
    

def login():
    print("logeando")

# Base de datos usuarios.

usuarios_pagina: list[dict] = []


while True:
    print()
    print("1. Registrars usuario")
    print("2. Loggin")
    print("3. Salir del programa")
    opción = input("Ingrese una opción: ")
    if opción == '1':
        registrar_usuario()
    elif opción == '2':
        login()
    elif opción == '3':
        print("Hasta pronto, gracias por utilizar nuestros servicios.")
        break
    else:
        print("Opción inválida")



 

