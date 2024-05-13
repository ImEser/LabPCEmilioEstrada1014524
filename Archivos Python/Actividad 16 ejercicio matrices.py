#Gabriela Santizo 1019324
#Emilio Estrada 1014524
A=[[1, 4, 5],
   [4, 2, 9],
   [6, 8, 7]]

B=[[1, 2, 5],
   [-4, 8, 3],
   [6, 7, 9]]

RESULTADO=[[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

print("La suma de las dos matrices es:")
for i in range(len(A)):
    for j in range(len(A[0])):
        RESULTADO[i][j] = A[i][j] + B[i][j]
for res in RESULTADO:
    print(res)

print("La resta de las dos matrices es:")
for i in range(len(A)):
    for j in range(len(A[0])):
        RESULTADO[i][j] = A[i][j] - B[i][j]
for res in RESULTADO:
    print(res)

print("La multiplicación de las dos matrices es:")
for i in range(len(A)):
    for j in range(len(A[0])):
        RESULTADO[i][j] = A[i][j] * B[i][j]
for res in RESULTADO:
    print(res)


print("Los números pares de la primera matriz son:")
for i in range(len(A)):
    for j in range(len(A[0])):
        if A[i][j] % 2 == 0:
            print(A[i][j])

print("Los números impares de la primera matriz son:")
for r in range(len(B)):
    for t in range(len(B[0])):
        if B[r][t] % 2 != 0:
          print(B[r][t])