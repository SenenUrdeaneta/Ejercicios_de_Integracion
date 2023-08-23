from integrador import Persona

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