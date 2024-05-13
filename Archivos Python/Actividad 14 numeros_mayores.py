print("Elija una opción\n1. Identificar el número mayor entre 5 valores\n2. Mostrar las tablas de múltiplicar del 1 al 10\n3. Salir")
opcion = int(input(" "))
val1 = 0
i = 0
mayor = 0

if opcion==1:
    while i<=4:
        val1 = int(input("Ingrese 5 valores "))
        if i == 0:
            mayor = val1
        else:
            if val1>mayor:
                mayor = val1
        i += 1
    print("El número mayor es", mayor)
if opcion==2:
    i = 1
    j = 1
    for i in range(1,11):
        print("Tabla de multiplicar del", i)
        for a in range(1,11):
            resultado = i * a
            print(f"{i} X {a} = {resultado}")
 

if opcion==3:
    print("SALIDA")
