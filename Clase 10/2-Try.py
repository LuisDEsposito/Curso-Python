try: 
    x = float(input("Número 1: "))
    y = float(input("Número 2: "))
    division = round(x / y, 2)
    print(x / y)
except: #En caso de haber error en algun paso, salta hasta esta parte. Si todo anda bien se ejecuta con normalidad.
    print("Algo salió mal...")
print("fin.")