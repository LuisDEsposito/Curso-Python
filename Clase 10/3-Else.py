try: 
    x = float(input("Número 1: "))
    y = float(input("Número 2: "))
    division = round(x / y, 2)
except: #En caso de haber error en algun paso, salta hasta esta parte. Si todo anda bien se ejecuta con normalidad.
    print("Algo salió mal...")
else: #Se ejecuta cuando no hay errores.
    print(division)
# try:
    #     print(10/0)
    # except:
    #     print("un error")
finally: #Es opcional, siempre se ejecuta aunque haya errores.
    print("fin.")