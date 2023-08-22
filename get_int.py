# Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
# cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
# del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
# ejercicio tanto de manera iterativa como recursiva.

# Versión Iterativa
def get_int_ite():
    while True:
        try:
            ve = input("Numero entero:")
            val = int(ve)
            return val
        except ValueError:
            print("Error en Entrada de Dato No Valida. Vuelva a Intentar")

print("Numero entero que fue ingresado (Iterativa):", get_int_ite())

# Versión Recursiva:
def get_int_rec():
    try:
        ve = input("Numero entero:")
        val = int(ve)
        return val
    except ValueError:
        print("Error en Entrada de Dato No Valida. Vuelva a Intentar")
        return get_int_rec()
    
print("Numero entero que fue ingresado (Recursiva):", get_int_rec())
