"""Para aprobar un crédito, el cliente debe ser mayor de edad. 
Además, debe tener una antigüedad en el sistema financiero de mínimo 3 años y un ingreso mayor a 2500 dólares. 
En caso no tenga la antigüedad suficiente, su ingreso mensual debe ser como mínimo 4000 dólares.
Si no cumple ninguna de las condiciones, no se aprueba el crédito
edad = 15
antigüedad = 10
ingreso = 1500"""


mayoria_edad = 18
antiguedad_minima = 3
ingreso_minimo = 2500
ingreso_menor_de_edad = 4000 
print("Bienvenido...")
edad = int(input("Ingrese su edad: "))
antigüedad = int(input("Ingrese su antigüedad: "))
ingreso = int(input("Ingrese el monto de sus ingresos mensuales: "))

if edad >= mayoria_edad and antigüedad >= antiguedad_minima and ingreso > ingreso_minimo:
    print("Tu credito ha sido aprobado.")
elif antigüedad < antiguedad_minima and ingreso >= ingreso_menor_de_edad:
    print(f"""Tu antiguedad no es suficiente, pero debido a que tu ingresos son 
mayores a {ingreso_menor_de_edad}, hemos aprobado el credito""")
else: print(f"""Lo siento, no cumples con los requisitos solicitados para recibir un credito.
Ten en cuenta que debes ser mayor de {mayoria_edad} años,
tener una antiguedad de al menos {antiguedad_minima} años y un ingreso mensual mayor a {ingreso_minimo} USD.
Si eres menor debes tener un ingreso minimo de {ingreso_menor_de_edad} USD.
Te esperamos nuevamente cuando logres reunir con las pautas requeridas y con gusto te brindaremos un credito apropiado.
Saludos.""")