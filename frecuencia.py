from integrador import cuentapalabras

parrafo = input("Ingrese una Cadena o Parrafo:")
resultado = cuentapalabras(parrafo)
# Recorremos el diccionaro y lo imprimo
for palabra, veces in resultado.items():
    print(f"La palabra: '{palabra}': aparece {veces}", end="")
    if veces == 1:
        print(" vez")
    else:
        print(" veces")




