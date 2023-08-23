from integrador import Cuenta, Persona, Cuentajoven

per1 = Persona("Jose Gonzalez", 38, "0987654321")
cjper1 = Cuentajoven(per1, 15000.0, 5.0)
cjper1.mostrar()
cjper1.retirar(5000.0)
cjper1.mostrar()
cjper1.ingresar(20000.0)
cjper1.mostrar()
