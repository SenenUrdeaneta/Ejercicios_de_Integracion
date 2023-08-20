"""
def maximo_comun_divisor(a, b):
    while b:
        a, b = b, a % b
    return a
"""


def maximo_comun_divisor(a, b):
    temporal = 0
    while b != 0:
        temporal = b
        b = a % b
        a = temporal
    return a

numero1 = int(input("Ingrese 1er numero: "))
numero2 = int(input("Ingrese 2do numero: "))

mcd = maximo_comun_divisor(numero1, numero2)
print(f"El máximo común divisor entre {numero1} y {numero2} es {mcd}.")