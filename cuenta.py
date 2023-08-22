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


# Ejemplo de uso
from integrador_funciones import Persona, Cuenta

per1 = Persona("ALberto Alvarez", 53, "123456789")
cuenta = Cuenta(per1, 1000.0)
cuenta.mostrar()

cuenta.ingresar(1500.0)
cuenta.mostrar()

cuenta.retirar(3800.0)
cuenta.mostrar()