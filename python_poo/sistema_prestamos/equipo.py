# ==========================================
# CLASE EQUIPO
# ==========================================

class Equipo:
    def __init__(self, codigo, nombre, categoria):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.__disponible = True

    def esta_disponible(self):
        return self.__disponible

    def prestar(self):
        if self.__disponible:
            self.__disponible = False
            return True
        return False

    def devolver(self):
        self.__disponible = True

    def mostrar_informacion(self):
        estado = "Disponible" if self.__disponible else "Prestado"

        print(
            f"{self.codigo:<10}"
            f"{self.nombre:<25}"
            f"{self.categoria:<20}"
            f"{estado}"
        )