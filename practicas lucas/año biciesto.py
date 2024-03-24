# un funcion que permita ingresar un año y ver si es biciesto o no.
# Se recuerda que los años bisiestos son múltiplos de 4, 
# pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí


def es_biciesto(año: int):
    if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
         return f'El año {año} es biciesto'
    else: 
        return f'El año {año} no es biciesto.'

# def es_biciesto(año: int):
#     return (año % 4 == 0 and año % 100 != 0) or año % 400 == 0 

print(es_biciesto(2012))
print(es_biciesto(2010))
print(es_biciesto(2000))
print(es_biciesto(1900))