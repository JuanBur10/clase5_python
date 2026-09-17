# ==========================================
# TALLER DE CLASES Y OBJETOS - CASO 1
# ==========================================

class Estudiante:
    def __init__(self, nombre, edad, programa):
        self.nombre = nombre
        self.edad = edad
        self.programa = programa

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Programa: {self.programa}")


estudiante = Estudiante(
    "Juan Josè",
    19,
    "Análisis y Desarrollo de Software"
)

print("===== INFORMACIÓN DEL ESTUDIANTE =====")
estudiante.mostrar_datos()