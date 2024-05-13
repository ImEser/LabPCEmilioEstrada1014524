import operaciones

print("Ingrese dos números:")
a = int(input(" "))
b = int(input(" "))

resultado_suma = operaciones.suma(a,b)
print("El resultado de la suma es: ", resultado_suma)

resultado_resta = operaciones.resta(a,b)
print("El resultado de la resta es: ", resultado_resta)

print("Ingrese un número del cual quiera la tabla de multiplicar")
c = int(input(" "))

resultado_multiplicacion = operaciones.multiplicar(c)

import arreglos
nombre = input("Ingrese su nombre: ")

nombre_al_reves = arreglos.nombre_al_reves(nombre)
print("Tu nombre al reves es:", nombre_al_reves)

cantidad_letras = arreglos.cantidad_letras(nombre)
print("Tu nombre tiene", cantidad_letras, "letras")
