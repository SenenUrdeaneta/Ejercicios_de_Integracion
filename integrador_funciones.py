# Funcion que Calculo No. Primo
def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

# Funcion que Calcula el Maximo Comun Divisor
def MCD(a, b):
    temporal = 0
    while b != 0:
        temporal = b
        b = a % b
        a = temporal
    return a

# Definimos la Funcion de Maximo Comun Multiplo en la misma utilizo la Funcion MCD
def MCM(x, y):     
    return (x * y) // MCD(x,y)

# Funcion cuentapalabras y retorna diccionario
def cuentapalabras(cadena):
    palabras = cadena.split()
    dic = {}
    # Recorremos la cadena 
    for palabra in palabras:
        palabra = palabra.strip(".,!¡¿?\"'()[]{}") # Quitamos los Caracteres especiales
        palabra = palabra.lower() # Convertimos las palabras en minuscula
        # Contamos las palabras repetidas  y las cargamos en el diccionario
        if palabra in dic:
            dic[palabra] = dic[palabra] + 1 
        else:
            dic[palabra] = 1
    return dic

# Funcion retorna palabra mas repetida y veces que se repitio
def masrepetida(dic):
    palabra_ini = ""
    veces_max = 0
    for palabra, veces in dic.items():
        if veces > veces_max:
            palabra_ini = palabra
            veces_max = veces
    return palabra_ini, veces_max

# Funcion get_int Versión Iterativa:
def get_int_ite():
    while True:
        try:
            ve = input("Numero entero:")
            val = int(ve)
            return val
        except ValueError:
            print("Error en Entrada de Dato No Valida. Vuelva a Intentar")

# Funcion get_int Versión Recursiva
def get_int_rec():
    try:
        ve = input("Numero entero:")
        val = int(ve)
        return val
    except ValueError:
        print("Error en Entrada de Dato No Valida. Vuelva a Intentar")
        return get_int_rec()
