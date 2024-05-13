nombres = []
j = 0
i = 0 
for i in range(5):
    i = input("Ingrese un nombre: ")
    nombres.append(i)

for j in range(5):
    print(f"El nombre {j + 1} de la lista es: {nombres[j]}")