import random

nombres = ["Emilio", "Lourdes", "Mariana", "Jimena", "Vivian"]
a = 0
while a < len(nombres):
    edad = random.randint(0, 100)
    print("Soy", nombres[a], "y tengo", edad, "años")
    a += 1
