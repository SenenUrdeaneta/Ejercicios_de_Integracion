from integrador_funciones import es_primo

numero = int(input("Ingrese un número: "))

if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")