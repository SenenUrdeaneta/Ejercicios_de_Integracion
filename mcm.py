#Escribir una función que calcule el mínimo común múltiplo entre dos números 

from integrador_funciones import MCM

#Programa Principal
print(f"Maximo Comun Multiplo.")
numero1=int(input("Ingrese 1er Numero:"))
numero2=int(input("Ingrese 2do Numero:"))

resultado2 = MCM(numero1,numero2)
print(f"El minimo comun multiplo entre el numero {numero1} y el {numero2} es: {resultado2}")