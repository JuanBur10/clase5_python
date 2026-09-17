# ==========================================
# EJEMPLO: CLASES Y OBJETOS
# ==========================================

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}")

    def es_mayor_edad(self):
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad.")
        else:
            print(f"{self.nombre} es menor de edad.")


persona1 = Persona("Juan", 19)
persona2 = Persona("Samara", 17)

print("===== PERSONA 1 =====")
persona1.mostrar_informacion()
persona1.saludar()
persona1.es_mayor_edad()

print("\n===== PERSONA 2 =====")
persona2.mostrar_informacion()
persona2.saludar()
persona2.es_mayor_edad()