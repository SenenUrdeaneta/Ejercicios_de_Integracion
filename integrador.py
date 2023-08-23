#=============================================#
# Funcion que Calcula el Maximo Comun Divisor
#=============================================#
def MCD(a, b):
    temporal = 0
    while b != 0:
        temporal = b
        b = a % b
        a = temporal
    return a

#==================================================================================#
# Definimos la Funcion de Maximo Comun Multiplo en la misma utilizo la Funcion MCD
#==================================================================================#
def MCM(x, y):     
    return (x * y) // MCD(x,y)

#==========================================================================================#
# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
# cada palabra que contiene y la cantidad de veces que aparece (frecuencia).
# Funcion cuentapalabras y retorna diccionario
#==========================================================================================#
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

#==============================================================================================#
# Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
# palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
# que reciba el diccionario generado con la función anterior y devuelva una tupla con la
# palabra más repetida y su frecuencia.
# Funcion retorna palabra mas repetida y veces que se repitio
#==============================================================================================#
def masrepetida(dic):
    palabra_ini = ""
    veces_max = 0
    for palabra, veces in dic.items():
        if veces > veces_max:
            palabra_ini = palabra
            veces_max = veces
    return palabra_ini, veces_max

#==============================================================================================#
# Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
# cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
# del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
# ejercicio tanto de manera iterativa como recursiva.
#==============================================================================================#
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

#===========================================================================================#
# Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
# siguientes métodos para la clase:
# (1) Un constructor, donde los datos pueden estar vacíos.
# (2) Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
# datos.
# (3) mostrar(): Muestra los datos de la persona.
# (4) Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad
#===========================================================================================#
# (1)
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

#================================================================================================#
# Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
# persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
# opcional. Crear los siguientes métodos para la clase:
# (1) Un constructor, donde los datos pueden estar vacíos.
# (2) Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
# directamente, sólo ingresando o retirando dinero.
# (3) mostrar(): Muestra los datos de la cuenta.
# (4) ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
# negativa, no se hará nada.
# (5) retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
# rojos. 
#=================================================================================================#

#(1)  
class Cuenta:
    def __init__(self, tit, cant=0.0):
        self.__tit = tit
        self.__cant = cant
    #(2)
    def tit_setter(self, titular):
        self.__tit = tit
    def tit_getter(self):
        return self.__tit
    def cant_getter(self):
        return self.__cant
    # (3)
    def mostrar(self):
        print("Titular:", self.__tit.nombreApellido_getter())
        print("Cantidad:", self.__cant)
    # (4)
    def ingresar(self, cant):
        if cant > 0:
            self.__cant += cant
    # (5)
    def retirar(self, cant):
        if cant > 0:
            self.__cant -= cant

#=============================================================================================#
# Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
# CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
# además del titular y la cantidad se debe guardar una bonificación que estará expresada en
# tanto por ciento. Crear los siguientes métodos para la clase:
# (1) Un constructor.
# (2) Los setters y getters para el nuevo atributo.
# (3) En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
# tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
# mayor de edad pero menor de 25 años y falso en caso contrario.
# (4) Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
# (5) El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la
# cuenta.
#=============================================================================================#
# (1)
class Cuentajoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion
    # (2)
    def boni_setter(self, bonificacion):
        self.__bonificacion = bonificacion
    def boni_getter(self):
        return self.__bonificacion
    # (3)
    def es_titular_valido(self):
        if self.tit_getter().mayor_de_edad() and self.tit_getter().edad_getter() < 25:
            return True
        return False
    # (4)
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("No es posible retirar dinero. Titular no válido.")
    # (5)
    def mostrar(self):
        print("Cuenta Joven")
        super().mostrar()
        print("Bonificación:", self.__bonificacion)