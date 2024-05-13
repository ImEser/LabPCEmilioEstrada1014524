#Emilio Santiago Estrada Ramírez 1014524
#Luis David Barrios Vergas 1128624
print("Bienvenidos a Proyecto1")
print("Licuado base: Leche deslactosada y sin azucar. Q. 20.00")

# Entradas
nombre = input("Escriba su nombre: ")
nit = input("Escriba su NIT: ")

# Variables de precios
PRECIO_BASE = 20.00
PRECIO_AZUCAR = 0.50
DESCUENTO_AGUA = -2.00
AUMENTO_SOYA = 3.00
AGRANDADO = 5/100

# Variables
total_azucar = 0
total_leche = 0
agrandado_aplicado = False
infocucharadas = "sin azucar"
Tipoleche = "Leche entera"
cucharadas=0

# Menú interactivo
while True:
    print("\nMenú:")
    print("1. Ver información del pedido")
    print("2. Agregar azúcar")
    print("3. Modificar leche")
    print("4. Agrandar")
    print("5. Confirmar pedido y salir")
    opcion = int(input("Ingrese el número de la opción deseada: "))

    if opcion == 1:
        print("Detalle del pedido:")
        print("Cliente:", nombre)
        print("NIT:", nit)
        print("Licuado: Fresa", Tipoleche, infocucharadas)
        precio_total = PRECIO_BASE + total_azucar + total_leche
        if agrandado_aplicado:
            precio_total += precio_total * AGRANDADO
        print("Precio total: Q", precio_total)
    elif opcion == 2:
        cucharadas = int(input("¿Cuántas cucharadas de azúcar desea agregar? (Máximo 2 cucharadas): "))
        if cucharadas <= 2:
            total_azucar += cucharadas * PRECIO_AZUCAR
            infocucharadas= "con azucar"
            print("Se agregaron", cucharadas, "cucharadas de azúcar.")
            print("Costo adicional por azúcar: Q", total_azucar)
        else:
            print("Solo se pueden agregar hasta 2 cucharadas de azúcar.")
    elif opcion == 3:
        print("Seleccione el tipo de leche:")
        print("1. Sin leche (únicamente con agua) (Descuento de Q. 2.00)")
        print("2. Leche deslactosada")
        print("3. Leche entera")
        print("4. Leche de soya (Aumento de Q. 3.00)")
        opcion_leche = int(input("Seleccione una opción: "))
        if opcion_leche == 1:
            total_leche += DESCUENTO_AGUA
            Tipoleche = "Sin leche"
            print("Se aplicó descuento por leche de agua.")
        elif opcion_leche == 2:
            total_leche += 0
            Tipoleche = "Con leche deslactosada"
        elif opcion_leche == 3:
            total_leche += 0
            Tipoleche = "Con leche entera"
        elif opcion_leche == 4:
            total_leche += AUMENTO_SOYA
            Tipoleche = "Con leche de soya"
            print("Se aplicó aumento por leche de soya.")
        else:
            print("Opción inválida.")
    elif opcion == 4:
        if not agrandado_aplicado:
            agrandado_aplicado = True
            print("El precio del licuado se aumentará en un 5%.")
        else:
            print("El licuado ya ha sido agrandado previamente.")
    elif opcion == 5:
        print("Detalle del pedido:")
        print("Cliente:", nombre)
        print("NIT:", nit)
        print("Licuado: Fresa", Tipoleche,"con", cucharadas, "de azúcar")
        precio_total = PRECIO_BASE + total_azucar + total_leche
        if agrandado_aplicado:
            precio_total += precio_total * AGRANDADO
        print("Precio total: Q", precio_total)
        break
    else:
        print("Por favor seleccione una opción válida.")