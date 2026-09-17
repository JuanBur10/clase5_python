# ==========================================
# TALLER DE CLASES Y OBJETOS - CASO 2
# ==========================================

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def calcular_total(self):
        return self.precio * self.cantidad

    def mostrar_producto(self):
        print(f"Producto: {self.nombre}")
        print(f"Precio: ${self.precio:,.2f}")
        print(f"Cantidad: {self.cantidad}")
        print(f"Total: ${self.calcular_total():,.2f}")


producto = Producto("Teclado", 120000, 2)

print("===== PRODUCTO =====")
producto.mostrar_producto()