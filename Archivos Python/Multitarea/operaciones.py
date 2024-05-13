# 3 operaciones :
# suma (dos parámetros)
# re 
def suma(a,b):
    return a+b


def resta(a,b):
    num = a
    num2 = b 
    if (num > num2):
        return num-num2
    else:
        return num2-num
    
def multiplicar(c):
    i = 1
    print(f"Tabla de multiplicar de {c}:")
    while (i<=10):
            resultado = c * i
            print(f"{c} x {i} = {resultado}")
            i += 1

    