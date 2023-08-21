# def MCD(a, b):
#     temporal = 0
#     while b != 0:
#         temporal = b
#         b = a % b
#         a = temporal
#     return a

from mcd import MCD

def MCM(x, y):     
    maxcm = MCD(x,y)
    print(maxcm)
    return (x * y) // maxcm

print(f"Maximo Comun Multiplo.")
numero1=int(input("Ingrese 1er Numero:"))
numero2=int(input("Ingrese 2do Numero:"))

resultado2 = MCM(numero1,numero2)
print(f"El minimo comun multiplo entre el numero {numero1} y el {numero2} es: {resultado2}")