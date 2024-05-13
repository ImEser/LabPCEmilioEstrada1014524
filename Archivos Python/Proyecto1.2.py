#Emilio Santiago Estrada Ramírez 1014524
#Luis David Barrios Vergas 1128624

print("Bienvenidos a Proyecto1")
# Entradas
nombre = input("Escriba su nombre: ")
nit = input("Escriba su NIT: ")
print("¿Qué desean ordenar?\n 1. Licuado de fresa Q.20.00\n 2.\n 3.")
menu = int(input("Ingrese el número de lo que desea ordenar: "))

# Licuado de fresa
precioinicial = 20.00
precio_azúcar = 0.50
precio_agua = -2.00
precio_lechesoya = 3.00
precio_lecheentera = 0.00
agrandado = 5/100
if menu == 1:
    print("Descripción del licuado:\nTamaño mediano, leche deslactosada y sin azúcar\n¿Deseas modificar el licuado? (Modificar podría incrementar o disminuir el precio inicial): ")
    modlicuado = input("¿Sí o No? ")
    if modlicuado.lower() == "si":
        #AZÚCAR
        print("¿Desea agregar azúcar? (Máximo 2 cucharadas)(Q. 0.50 extras por cada cucharada)")
        modlicuado = input("¿Sí o No? ")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
        #SI azúcar
        if modlicuado.lower() == "si":
            print("¿Cuántas cucharadas de azúcar desea agregar? (Máximo 2 cucharadas)")
            cucharadas_azucar = int(input("¿1 o 2? "))
            if (cucharadas_azucar <= 2):
                licuado_azucar = cucharadas_azucar * precio_azúcar
                total_licuado_con_azucar = precioinicial + licuado_azucar
                print("El precio del licuado con",cucharadas_azucar, "cucharadas de azúcar es: Q. " ,total_licuado_con_azucar)

                #SI azúcar y SI leche
                print("¿Desea modificar la leche de su licuado?")
                tipo_de_leche = input("¿Sí o No? ")
                if tipo_de_leche.lower() == "si":
                    print("1. Sin leche (únicamente con agua) (Descuento de Q. 2.00). \n2. Leche deslactosada (no altera el precio). \n3. Leche entera (no altera el precio). \n4. Leche de soya (Aumento de Q. 3.00).")
                    opcion_leche = int(input("Seleccione una opción: "))
                    if opcion_leche == 1:
                        total_licuado_con_leche = total_licuado_con_azucar + precio_agua
                        print("El precio del licuado con",cucharadas_azucar, "cucharadas de azúcar y agua es: Q. ", total_licuado_con_leche)
                    elif opcion_leche == 2:
                        total_licuado_con_leche = total_licuado_con_azucar + 0
                        print("El precio del licuado con",cucharadas_azucar, "cucharadas de azúcar y leche deslactosada es: Q. ", total_licuado_con_leche)
                    elif opcion_leche == 3:
                        total_licuado_con_leche = total_licuado_con_azucar + precio_lecheentera
                        print("El precio del licuado con",cucharadas_azucar, "cucharadas de azúcar y leche entera es: Q. ", total_licuado_con_leche)
                    elif opcion_leche == 4:
                        total_licuado_con_leche = total_licuado_con_azucar + precio_lechesoya
                        print("El precio del licuado con",cucharadas_azucar, "cucharadas de azúcar y leche de soya es: Q. ", total_licuado_con_leche)
                    else:
                        print("Elija una opción correcta")
                        #PENDIENTE EL RETORNO A LA PREGUNTA----------------------------------------------------------------------------
                    
                    #SI azúcar y SI leche y SI tamaño
                    print("¿Desea modificar el tamaño del licuado?\nEl licuado es de tamaño mediano y solamente lo podrá modificar a tamaño grande")
                    tamano_licuado = input("¿Sí o No? ")
                    if tamano_licuado.lower() == "si":
                        calculo_tamano = total_licuado_con_leche * agrandado
                        total_licuado_agrandado = calculo_tamano + total_licuado_con_leche
                        print(nombre, "con NIT:", nit)
                        #PENDIENTE PODER VISUALIZAR TODAS LAS MODIFICACIONES!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                        print("Su total a pagar es de: Q. ",total_licuado_agrandado)
                    
                    #SI azúcar y SI Leche, pero NO tamaño
                    else:
                        print(nombre, "con NIT: ", nit)
                        #PENDIENTE PODER VISUALIZAR TODAS LAS MODIFICACIONES!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                        print("Su total a pagar es de: Q. ",total_licuado_con_leche)
                #SI azúcar, pero NO LECHE
                else:
                    #SI azúcar, pero NO LECHE, pero SI tamaño
                    print("¿Desea modificar el tamaño del licuado?\nEl licuado es de tamaño mediano y solamente lo podrá modificar a tamaño grande")
                    tamano_licuado = input("Sí o No")
                    if tamano_licuado.lower() == "si":
                        calculo_tamano = total_licuado_con_azucar * agrandado
                        total_licuado_agrandado = calculo_tamano + total_licuado_con_azucar
                        print(nombre, "con NIT:", nit)
                        print("El precio del licuado con",cucharadas_azucar, "cucharadas de azúcar, leche deslactosada y agrandado es: Q. " ,total_licuado_agrandado)
                    #SI azúcar, pero NO LECHE y NO tamaño
                    else:
                        print(nombre, "con NIT:", nit)
                        print("El precio del licuado con",cucharadas_azucar, "cucharadas de azúcar, leche deslactosada y sin agrandar es: Q. " ,total_licuado_con_azucar)
            #más de 2 cucharadas
            else:
                print("Máximo 2 cucharadas de azúcar")
                #PENDIENTE EL RETORNO A LA PREGUNTA------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                
        #NO azúcar  
        else:
            #NO azúcar, pero SI leche 
            print("¿Desea modificar la leche de su licuado?")
            tipo_de_leche = input("¿Sí o No? ")
            if tipo_de_leche.lower() == "si":
                print("1. Sin leche (únicamente con agua) (Descuento de Q. 2.00). \n2. Leche deslactosada (no altera el precio). \n3. Leche entera (no altera el precio). \n4. Leche de soya (Aumento de Q. 3.00).")
                opcion_leche = int(input("Elija una opción: "))
                if opcion_leche == 1:
                    total_licuado_con_leche = precioinicial + precio_agua
                    print("El precio del licuado con leche de agua es: Q. ", total_licuado_con_leche)
                elif opcion_leche == 2:
                    total_licuado_con_leche = precioinicial + 0
                    print("El precio del licuado con leche deslactosada es: Q. ", total_licuado_con_leche)
                elif opcion_leche == 3:
                    total_licuado_con_leche = precioinicial + precio_lecheentera
                    print("El precio del licuado con leche entera es: Q. ", total_licuado_con_leche)
                elif opcion_leche == 4:
                    total_licuado_con_leche = precioinicial + precio_lechesoya
                    print("El precio del licuado con leche de soya es: Q. ", total_licuado_con_leche)
                else:
                    print("Elija una opción correcta")
                    #PENDIENTE EL RETORNO A LA PREGUNTA----------------------------------------------------------------------------

                #NO azúcar, pero SI LECHE y SI tamaño
                print("¿Desea modificar el tamaño del licuado?\nEl licuado es de tamaño mediano y solamente lo podrá modificar a tamaño grande")
                tamano_licuado = input("¿Sí o No? ")
                if tamano_licuado.lower() == "si":
                    calculo_tamano = total_licuado_con_leche * agrandado
                    total_licuado_agrandado = calculo_tamano + total_licuado_con_leche
                    print(nombre, "con NIT:", nit)
                    #PENDIENTE PODER VISUALIZAR TODAS LAS MODIFICACIONES!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    print("Su total a pagar es de: Q. ",total_licuado_agrandado)
                    
                #NO azúcar, pero SI LECHE y NO tamaño
                else:
                    print(nombre, "con NIT: ", nit)
                    #PENDIENTE PODER VISUALIZAR TODAS LAS MODIFICACIONES!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    print("Su total a pagar es de: Q. ",total_licuado_con_leche)
            #NO azúcar y NO leche
            else:
                #NO azúcar y NO leche, pero SI tamaño
                print("¿Desea modificar el tamaño del licuado?\nEl licuado es de tamaño mediano y solamente lo podrá modificar a tamaño grande")
                tamano_licuado = input("Sí o No")
                if tamano_licuado.lower() == "si":
                    calculo_tamano = agrandado * precioinicial
                    total_licuado_agrandado = calculo_tamano + precioinicial
                    print(nombre, "con NIT: ", nit)
                    print("El precio del licuado sin azúcar, con leche deslactosada y agrandado es: Q.",total_licuado_agrandado)
                    
                #NO azúcar y NO leche, pero NO tamaño
                else:
                    print(nombre, "con NIT: ", nit)
                    print("El precio del licuado sin azúcar, con leche deslactosada y sin agrandar es: Q.", precioinicial)

#Licuado sin modificaciones
    else:
        print(nombre, "con NIT: ", nit)
        print("El precio del licuado sin azúcar, con leche deslactosada y sin agrandar es: Q.", precioinicial)

