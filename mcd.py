# Defino La Funcion que Calcula el Maximo Comun Divisor
def MCD(a, b):
    temporal = 0
    while b != 0:
        temporal = b
        b = a % b
        a = temporal
    return a

# Programa Principal
print(f"Maximo Comun Divisor.")
numero1 = int(input("Ingrese 1er numero: "))
numero2 = int(input("Ingrese 2do numero: "))
# Calculo el Maximo Comund Divisor y gurado Resultado en la Variable "resultado" e Imprimo Resultado.
resultado = MCD(numero1, numero2)
print(f"El Máximo Común Divisor entre {numero1} y {numero2} es: {resultado}")