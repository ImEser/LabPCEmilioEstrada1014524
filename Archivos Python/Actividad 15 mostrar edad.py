edades = []
i=0
j=0

for i in range(5):
    
    while True: 
        edad = input(f"Ingrese la edad {i + 1} : ")
        
        if(float(edad).is_integer()):
            num = int(edad)
        
            if (num > 0 and num <= 100):
                edades.append(num)
                break
            else: 
                print("Ingrese una edad válida. Intentelo de nuevo.")
        else: 
            print("Error, debe ingresar un número entero")
    
for j in range(5):
        print(f"La edad de la persona {j + 1} es: {edades[j]}")