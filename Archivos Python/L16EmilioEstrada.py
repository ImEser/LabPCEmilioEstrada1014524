import random

print("Semana No. 16: Ejercicio 1")

lista = []

for x in range(10):
    lista.append(random.randint(0,10))

opcion = 'a'

while(opcion != 'e'):
    print("Menú")
    print("a. Mostrar números", 
          "b. Promedio", 
          "c. Longitud", 
          "d. Posición pares e impares",
          "e. Salir")
    opcion = input("Ingrese su opción: ")

    match opcion:
        case 'a': #opción mostrar números
            for x in range (len(lista)):
                print(f"No. {x}: {lista[x]}")
        case 'b': #opción promedio
            print("Promedio")
            sumatoria = 0
            for x in range(len(lista)):
                sumatoria += lista[x]
            promedio = sumatoria / len(lista)
            print(f"----Promedio: {promedio}")
        case 'c':
            print("Longitud")
            print(f"----Longitud del arreglo: {len(lista)}")
        case 'd':
            print("Pares e impares")
            suma_pares = sum(lista[x] for x in range(0, len(lista), 2))
            suma_impares = sum(lista[x] for x in range(1, len(lista), 2))
            print(f"----Suma de posiciones pares: {suma_pares}")
            print(f"----Suma de posiciones impares: {suma_impares}")

print("Semana No. 16: Ejercicio 2")

cantFilas = int(input("Ingrese la cantidad de filas"))
cantCols = int(input("Ingrese la cantidad de columnas"))

matriz = [[0 for x in range(cantCols)] for y in range (cantFilas)]
mayor = 0

for xFilas in range(cantFilas):
    for xCols in range(cantCols):
        matriz[xFilas][xCols] = random.randint(0,1000)

        #Comparación mayor
        if(matriz[xFilas][xCols] > mayor):
            mayor = matriz[xFilas][xCols]

print(matriz)
print(f"El número mayor es: {mayor}")