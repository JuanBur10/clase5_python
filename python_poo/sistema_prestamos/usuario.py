# ==========================================
# CLASE USUARIO
# ==========================================

class Usuario:
    def __init__(self, documento, nombre):
        self.documento = documento
        self.nombre = nombre
        self.prestamos = []

    def agregar_prestamo(self, prestamo):
        self.prestamos.append(prestamo)

    def mostrar_informacion(self):
        print(f"Documento: {self.documento}")
        print(f"Nombre: {self.nombre}")
        print(f"Préstamos: {len(self.prestamos)}")