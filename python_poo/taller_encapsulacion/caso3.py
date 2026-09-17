# ==========================================
# TALLER DE ENCAPSULACIÓN - CASO 3
# ==========================================

class Equipo:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self.__disponible = True

    def consultar_disponibilidad(self):
        return self.__disponible

    def prestar(self):
        if self.__disponible:
            self.__disponible = False
            print(f"El equipo {self.nombre} fue prestado.")
        else:
            print(f"El equipo {self.nombre} no está disponible.")

    def devolver(self):
        if not self.__disponible:
            self.__disponible = True
            print(f"El equipo {self.nombre} fue devuelto.")
        else:
            print(f"El equipo {self.nombre} ya estaba disponible.")


equipo = Equipo("Computador portátil", "EQ001")

print("===== EQUIPO =====")
print(f"Equipo: {equipo.nombre}")
print(f"Código: {equipo.codigo}")

print(f"Disponible: {equipo.consultar_disponibilidad()}")

equipo.prestar()

print(f"Disponible: {equipo.consultar_disponibilidad()}")

equipo.devolver()

print(f"Disponible: {equipo.consultar_disponibilidad()}")