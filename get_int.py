# Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
# cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
# del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
# ejercicio tanto de manera iterativa como recursiva.

from integrador_funciones import get_int_ite, get_int_rec

# Usando Funcion Iterativa
print("Numero entero que fue ingresado (Iterativa):", get_int_ite())


# Usando Funcion Recursiva
print("Numero entero que fue ingresado (Recursiva):", get_int_rec())
