x=2
y=2

matriz=[]

for i in range(x):
    x=[]
    for j in range (y):
        valor = int(input(f"Ingrese el valor para la fila {i+1} y columna {i+1}: "))
        x.append(valor)
    matriz.append(x)

for x in matriz:
    print(x)
    print(x+y)
    print(x-y)