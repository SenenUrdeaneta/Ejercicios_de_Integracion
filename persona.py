# Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
# siguientes métodos para la clase:
# (1) Un constructor, donde los datos pueden estar vacíos.
# (2) Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
# datos.
# (3) mostrar(): Muestra los datos de la persona.
# (4) Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad

# Crear la Clase (1)
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

# Programa Principal
# Intanciamos la Clase con Datos de Prueba
persona = Persona()
persona.nombreApellido_setter("Juan Perez")
persona.edad_setter(20)
persona.dni_setter("1234567890")
# Mostramos los datos 
persona.mostrar()
#Verificamos si es mayor de edad o no
if persona.mayor_de_edad():
    print("La Persona Es mayor de edad")
else:
    print("La Persona No es mayor de edad")