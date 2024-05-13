total_desayuno = 0
total_almuerzo = 0
total_cena = 0

while True:
    print("Menú:")
    print("1. Desayuno")
    print("2. Almuerzo")
    print("3. Cena")
    print("4. Salir")

    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        print("Huevos revueltos con frijoles, salchicha, pan tostado y jugo de naranja. Q. 40.00")
        cantidad_desayuno = int(input("Cuántos desayunos desea pedir? "))
        total_desayuno = cantidad_desayuno * 40
        print(f"Se agregaron {cantidad_desayuno} desayunos al pedido.")
        continuar = input("Desea agregar otro platillo diferente?\nSi o no? ")
        if continuar.lower() == 'si':
            continue
        else:
            total = total_desayuno + total_almuerzo + total_cena
            print("El total a pagar es:", total, "quetzales")
            break
    elif opcion == "2":
        print("Queso burguesa con papas y limonada. Q. 55.00")
        cantidad_almuerzo = int(input("Cuántos almuerzos desea pedir? "))
        total_almuerzo = cantidad_almuerzo * 55
        print(f"Se agregaron {cantidad_almuerzo} almuerzos al pedido.")
        continuar = input("Desea agregar otro platillo diferente?\nSi o no? ")
        if continuar.lower() == 'si':
            continue
        else:
            total = total_desayuno + total_almuerzo + total_cena
            print("El total a pagar es:", total, "quetzales")
            break
    elif opcion == "3":
        print("Pollo a la plancha con verduras cocidas y naranjada. Q. 45.00")
        cantidad_cena = int(input("¿Cuántas cenas desea pedir? "))
        total_cena = cantidad_cena * 45
        print(f"Se agregaron {cantidad_cena} cenas al pedido.")
        continuar = input("¿Desea agregar otro platillo diferente?\nSi o no? ")
        if continuar.lower() == 'si':
            continue
        else:
            total = total_desayuno + total_almuerzo + total_cena
            print("El total a pagar es:", total, "quetzales")
            break
    elif opcion == "4":
        break
    else:
        print("Opción incorrecta")
