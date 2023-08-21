#Escribir una función que calcule el mínimo común múltiplo entre dos números 

# Creamos la Funcion de Calculo de Maximo Comun Divisor que la vamos a utilizar para Calcular el MCM
def MCD(a, b):
    temporal = 0
    while b != 0:
        temporal = b
        b = a % b
        a = temporal
    return a
# Definimos la Funcion de Maximo Comun ultiplo
def MCM(x, y):     
    return (x * y) // MCD(x,y)

#Programa Principal
print(f"Maximo Comun Multiplo.")
numero1=int(input("Ingrese 1er Numero:"))
numero2=int(input("Ingrese 2do Numero:"))

resultado2 = MCM(numero1,numero2)
print(f"El minimo comun multiplo entre el numero {numero1} y el {numero2} es: {resultado2}")