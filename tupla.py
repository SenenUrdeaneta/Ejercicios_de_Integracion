from integrador import cuentapalabras, masrepetida

parrafo = input("Ingresa Parrafo o Cadena: ")
resultado = cuentapalabras(parrafo)
tupla = masrepetida(resultado)

print(f"Palabra y veces mas repetida: {tupla} veces")