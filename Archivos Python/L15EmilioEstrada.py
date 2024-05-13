#EJERCICIO 1
print("¿Qué desea calcular?", "1. Área de triángulo", "2. Área de cuadrado", "3. Área de rectángulo", "4. Área de círculo", sep="\n")

opcion_calculo = input("Ingrese su opción: ")
resultado = ""

match opcion_calculo:
    case "1":
        base_t = int(input("Ingrese la base de su triángulo: "))
        altura_t = int(input("Ingrese la altura de su triángulo: "))
        resultado = (base_t * altura_t) / 2
    case "2":
        lado_c = int(input("Ingrese el lado de su cuadrado: "))
        resultado = lado_c ** 2
    case "3":
        base_r = int(input("Ingrese la base de su rectángulo: "))
        altura_r = int(input("Ingrese la altura de su rectángulo: "))
        resultado = (altura_r * base_r)
    case "4":
        radio_c = int(input("Ingrese el radio de su círculo: "))
        resultado = float(3.1415 * (radio_c ** 2))
    case _:
        print("Opción no válida")

print("El área que solicitó es:", resultado)

#EJERCICIO2
x = 0
y = 0

def mover_posicion(cambio_x, cambio_y):
    global x, y
    x += cambio_x
    y += cambio_y

opcion_movimiento = 'a'
while opcion_movimiento != 'e':
    print("Posibles movimientos:")
    print("a. sube", "b. baja", "c. izquierda", "d. derecha", "e. salir", sep="\n")
    opcion_movimiento = input("Ingrese la acción que desea realizar: ")

    match opcion_movimiento:
        case "a":
            mover_posicion(0, 1)
        case "b":
            mover_posicion(0, -1)
        case "c":
            mover_posicion(-1, 0)
        case "d":
            mover_posicion(1, 0)
        case _:
            print("Error")

print(f"La posición del jugador es [{x}][{y}]")
