# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
# cada palabra que contiene y la cantidad de veces que aparece (frecuencia).
def cuentapalabras(cadena):
    palabras = cadena.split()
    dic = {}
    # Recorremos la cadena 
    for palabra in palabras:
        palabra = palabra.strip(".,!¡¿?\"'()[]{}") # Quitamos los Caracteres especiales
        palabra = palabra.lower() # Convertimos las palabras en minuscula
        # Contamos las palabras repetidas  y las cargamos en el diccionario
        if palabra in dic:
            dic[palabra] = dic[palabra] + 1 
        else:
            dic[palabra] = 1
    return dic

# Programa Principal
parrafo = input("Ingrese una Cadena o Parrafo:")
resultado = cuentapalabras(parrafo)
# Recorremos el diccionaro y lo imprimo
for palabra, veces in resultado.items():
    print(f"{palabra}: {veces}")





