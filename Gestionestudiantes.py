class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.cursos = []
        self.calificaciones = {}

    def inscribir_curso(self, curso):
        if curso not in self.cursos:
            self.cursos.append(curso)
            self.calificaciones[curso] = []

    def agregar_calificacion(self, curso, nota):
        if curso in self.calificaciones:
            self.calificaciones[curso].append(nota)
        else:
            print(f"El estudiante no está inscrito en el curso {curso}")

    def promedio_notas(self):
        todas_las_notas = [nota for notas in self.calificaciones.values() for nota in notas]
        return round(sum(todas_las_notas) / len(todas_las_notas), 2) if todas_las_notas else "No hay calificaciones aún"


# Crear un estudiante
estudiante1 = Estudiante("Carlos", 20)

# Inscribir cursos y agregar calificaciones
estudiante1.inscribir_curso("Matemáticas")
estudiante1.inscribir_curso("Historia")

estudiante1.agregar_calificacion("Matemáticas", 90)
estudiante1.agregar_calificacion("Matemáticas", 85)
estudiante1.agregar_calificacion("Historia", 88)

# Mostrar información
print(f"Nombre: {estudiante1.nombre}")
print(f"Edad: {estudiante1.edad}")
print(f"Cursos inscritos: {estudiante1.cursos}")
print(f"Promedio de notas: {estudiante1.promedio_notas()}")
