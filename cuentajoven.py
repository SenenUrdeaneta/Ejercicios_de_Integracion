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

from integrador_funciones import Cuenta, Persona, CuentaJoven


# Ejemplo de uso
per1 = Persona("Jose Gonzalez", 38, "0987654321")
cj = CuentaJoven(per1, 15000.0, 5.0)
cj.mostrar()
cj.retirar(5000.0)
cj.mostrar()
cj.ingresar(20000.0)
cj.mostrar()
