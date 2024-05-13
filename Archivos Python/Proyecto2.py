class Curso:
    def __init__(self, id_curso, nombre, horario, salon, catedratico):
        self.id_curso = id_curso
        self.nombre = nombre
        self.horario = horario
        self.salon = salon
        self.catedratico = catedratico

class Alumno:
    def __init__(self, carne, nombre, fecha_nacimiento):
        self.carne = carne
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento

cursos = []
alumnos = []

def crear_curso():
    id_curso = input("Ingrese el ID del curso: ")
    nombre = input("Ingrese el nombre del curso: ")
    horario = input("Ingrese el horario del curso: ")
    salon = input("Ingrese el salón del curso: ")
    catedratico = input("Ingrese el catedrático del curso: ")

    for curso in cursos:
        if curso.id_curso == id_curso:
            print("El curso ya existe en el registro.")
            return

    cursos.append(Curso(id_curso, nombre, horario, salon, catedratico))
    print("Curso creado exitosamente.")

def listar_cursos():
    for i, curso in enumerate(cursos):
        print(f"{i+1}. {curso.nombre}")

def editar_curso():
    listar_cursos()
    opcion = int(input("Seleccione el curso que desea editar: ")) - 1

    if 0 <= opcion < len(cursos):
        nuevo_nombre = input("Ingrese el nuevo nombre del curso: ")
        cursos[opcion].nombre = nuevo_nombre
        print("Curso editado exitosamente.")
    else:
        print("Opción inválida.")

def crear_alumno():
    carne = input("Ingrese el carné del alumno: ")
    nombre = input("Ingrese el nombre del alumno: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento del alumno: ")

    alumnos.append(Alumno(carne, nombre, fecha_nacimiento))
    print("Alumno creado exitosamente.")

def listar_alumnos():
    for i, alumno in enumerate(alumnos):
        print(f"{i+1}. {alumno.nombre} - Carné: {alumno.carne}")

def asignar_nota():
    listar_cursos()
    curso_opcion = int(input("Seleccione el curso: ")) - 1

    listar_alumnos()
    alumno_opcion = int(input("Seleccione el alumno: ")) - 1

    nota = float(input("Ingrese la nota del alumno: "))

    # Aquí puedes añadir la lógica para asignar la nota al alumno en el curso seleccionado

    print("Nota asignada exitosamente.")

def generar_reporte():
    print("Seleccione el tipo de reporte:")
    print("a. Listado de cursos mostrando la cantidad de estudiantes, ordenado de mayor a menor")
    print("b. Listar estudiantes de un curso seleccionado junto con las notas de ese curso")
    print("c. Listar para un estudiante seleccionado sus notas")
    print("d. Reporte con la nota media por curso")
    print("e. Reporte con estudiante con mejor desempeño en general")
    
    opcion = input("Ingrese la opción deseada: ")

    # Aquí puedes añadir la lógica para generar cada tipo de reporte

    print("Reporte generado exitosamente.")

while True:
    print("\nBienvenido al sistema de control de notas de la Universidad Rafael Landívar")
    print("1. Crear curso")
    print("2. Editar curso")
    print("3. Crear alumno")
    print("4. Asignar nota")
    print("5. Generar reporte")
    print("6. Salir")

    opcion = int(input("Ingrese la opción deseada: "))

    if opcion == 1:
        crear_curso()
    elif opcion == 2:
        editar_curso()
    elif opcion == 3:
        crear_alumno()
    elif opcion == 4:
        asignar_nota()
    elif opcion == 5:
        generar_reporte()
    elif opcion == 6:
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida.")
