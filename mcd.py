# git Escribir una función que calcule el máximo común divisor entre dos números.

from integrador_funciones import MCD

# Programa Principal
print(f"Maximo Comun Divisor.")
numero1 = int(input("Ingrese 1er numero: "))
numero2 = int(input("Ingrese 2do numero: "))
# Calculo el Maximo Comund Divisor y gurado Resultado en la Variable "resultado" e Imprimo Resultado.
resultado = MCD(numero1, numero2)
print(f"El Máximo Común Divisor entre {numero1} y {numero2} es: {resultado}")