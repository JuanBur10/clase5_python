# ==========================================
# TALLER DE CLASES Y OBJETOS - CASO 3
# ==========================================

class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")

    def encender(self):
        print(f"El vehículo {self.marca} {self.modelo} está encendido.")


vehiculo = Vehiculo("Toyota", "Mustang", 2024)

print("===== VEHÍCULO =====")
vehiculo.mostrar_informacion()
vehiculo.encender()