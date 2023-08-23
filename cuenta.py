from integrador import Cuenta, Persona

per1 = Persona("ALberto Alvarez", 53, "123456789")
cuenta = Cuenta(per1, 1000.0)
cuenta.mostrar()

cuenta.ingresar(1500.0)
cuenta.mostrar()

cuenta.retirar(3800.0)
cuenta.mostrar()