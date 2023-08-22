# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
# cada palabra que contiene y la cantidad de veces que aparece (frecuencia).

from integrador_funciones import cuentapalabras

# Programa Principal
parrafo = input("Ingrese una Cadena o Parrafo:")
resultado = cuentapalabras(parrafo)
# Recorremos el diccionaro y lo imprimo
for palabra, veces in resultado.items():
    print(f"La palabra: '{palabra}': aparece {veces}", end="")
    if veces == 1:
        print(" vez")
    else:
        print(" veces")




