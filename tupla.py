# Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
# palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
# que reciba el diccionario generado con la función anterior y devuelva una tupla con la
# palabra más repetida y su frecuencia.

from integrador_funciones import cuentapalabras, masrepetida


parrafo = input("Ingresa Parrafo o Cadena: ")
resultado = cuentapalabras(parrafo)
tupla = masrepetida(resultado)

print(f"Palabra y veces mas repetida: {tupla} veces")