def entrada_numeros_a_dividir():
    while True:
            try:
                dividendo = float(input("Número 1: "))
                divisor = float(input("Número 2: "))
                if divisor == 0:
                      raise
            except:
                print("Lo siento,hubo un error, por favor intente de nuevo.")
                continue
            else:            
                break
    return dividendo, divisor

def división(dividendo: float, divisor: float)-> float | bool:
      try:
          división = dividendo/divisor
      except:
            print("No se puede dividir por cero")
            return False
      return división

def mostrar(numero: float)->None:
     print(f"El resultado de la operacion es {numero:.5f}")
     

def main():
     dividendo, divisor = entrada_numeros_a_dividir()
     resultado = división(dividendo, divisor)
     if resultado is False:
          pass
     else:
          mostrar(resultado)

main()


# Ejemplo compañero
# def principal():
#         x = float(input("numero: "))
#         y = float(input("numero: "))
#         print(f"El resultado es: {x/y:.2f}")
#         return
# def exepcion():
#      print("La respuesta es incorrecta. ")
#      return
# def final():
#     eleccion = input("Ingrese si desea continuar (S/N): ").lower()
#     if eleccion == "s":
#         True
#     elif eleccion == "n":
#         exit()
    
# def main():
#     while True:
#         try:
#             principal()
#         except:
#              exepcion()
#         finally:
#              final()

# main()