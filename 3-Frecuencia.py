# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
# cada palabra que contiene y la cantidad de veces que aparece (frecuencia).

def contarpalabras(cadena):
    palabras = cadena.split()
    return palabras

dic = {}
parrafo = input("Ingrese Parrafo:")
resultado = contarpalabras(parrafo)
# Recorremos la cadena Quitamos los Caracteres especiales y convertimos las palabras en minuscula
for palabra in resultado:
    palabra = palabra.strip(".,!¡¿?\"'()[]{}")
    palabra = palabra.lower()
    # Contamos las palabras repetidas  y las cargamos en el diccionario
    if palabra in dic:
        dic[palabra] = dic[palabra] + 1 
    else:
        dic[palabra] = 1
# Recorremos el diccionaro y lo imprimo
for palabra, veces in dic.items():
    print(f"{palabra}: {veces}")





