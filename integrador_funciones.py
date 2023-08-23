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

class Persona:
    def __init__(self, nomApe = "", edad=0, dni=""):
        self.__nomApe = nomApe
        self.__edad = edad
        self.__dni = dni

    # Setters (2)
    def nombreApellido_setter(self, nomApe):
        self.__nomApe = nomApe

    def edad_setter(self, edad):
        if edad >= 0:
            self.__edad = edad
        else:
            print("Edad Incorrecta, tiene que ser un valor positivo")

    def dni_setter(self, dni):
        if len(dni) >= 1 and len(dni) <= 10:
            self.__dni = dni
        else:
            print("DNI no debe tener mas de 10 caracteres.")
            self.__dni = "Error en No. DNI"

    # Getters (2)
    def nombreApellido_getter(self):
        return self.__nomApe

    def edad_getter(self):
        return self.__edad

    def dni_getter(self):
        return self.__dni

    # Mostrar (3)
    def mostrar(self):
        print("Nombre y Apellido:", self.__nomApe)
        print("Edad:", self.__edad)
        print("Dni:", self.__dni)

    # Validar Edad (4)
    def mayor_de_edad(self):
        return self.__edad >= 18
    
class Cuenta:
    def __init__(self, tit, cant=0.0):
        self.__tit = tit
        self.__cant = cant

    def tit_setter(self, titular):
        self.__tit = tit

    def tit_getter(self):
        return self.__tit

    def cant_getter(self):
        return self.__cant

    def mostrar(self):
        print("Titular:", self.__tit.nombreApellido_getter())
        print("Cantidad:", self.__cant)

    def ingresar(self, cant):
        if cant > 0:
            self.__cant += cant

    def retirar(self, cant):
        if cant > 0:
            self.__cant -= cant

# Clase CuentaJoven
class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion

    def set_bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion

    def get_bonificacion(self):
        return self.__bonificacion

    def es_titular_valido(self):
        if self.tit_getter().mayor_de_edad() and self.tit_getter().edad_getter() < 25:
            return True
        return False

    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("No es posible retirar dinero. Titular no válido.")

    def mostrar(self):
        print("Cuenta Joven")
        super().mostrar()
        print("Bonificación:", self.__bonificacion)