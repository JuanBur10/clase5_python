# ==========================================
# TALLER DE ENCAPSULACIÓN - CASO 1
# ==========================================

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.__salario = salario

    def obtener_salario(self):
        return self.__salario

    def aumentar_salario(self, aumento):
        if aumento > 0:
            self.__salario += aumento
            print("Salario actualizado.")
        else:
            print("El aumento debe ser mayor que cero.")


empleado = Empleado("Juan Josè", 3200000)

print("===== EMPLEADO =====")
print(f"Nombre: {empleado.nombre}")
print(f"Salario: ${empleado.obtener_salario():,.2f}")

empleado.aumentar_salario(300000)

print(f"Nuevo salario: ${empleado.obtener_salario():,.2f}")
