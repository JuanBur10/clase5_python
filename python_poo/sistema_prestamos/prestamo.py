# ==========================================
# CLASE PRESTAMO
# ==========================================

class Prestamo:
    def __init__(self, usuario, equipo):
        self.usuario = usuario
        self.equipo = equipo
        self.__activo = True

    def esta_activo(self):
        return self.__activo

    def devolver(self):
        if self.__activo:
            self.__activo = False
            self.equipo.devolver()
            return True

        return False

    def mostrar_informacion(self):
        estado = "Activo" if self.__activo else "Devuelto"

        print(f"Usuario: {self.usuario.nombre}")
        print(f"Equipo: {self.equipo.nombre}")
        print(f"Estado: {estado}")