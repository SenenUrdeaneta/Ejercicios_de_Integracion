# Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
# siguientes métodos para la clase:
# (1) Un constructor, donde los datos pueden estar vacíos.
# (2) Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
# datos.
# (3) mostrar(): Muestra los datos de la persona.
# (4) Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad

# Programa Principal
from integrador_funciones import Persona

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