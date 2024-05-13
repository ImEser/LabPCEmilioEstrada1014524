def nombre_al_reves(nombre):
    nombre_reverso = " "
    for letra in nombre:
        nombre_reverso = letra + nombre_reverso
    return nombre_reverso

def cantidad_letras(nombre):
    d = 0
    for letra in nombre:
        d += 1
    return d
