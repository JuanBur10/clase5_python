# ==========================================
# EJEMPLO: ENCAPSULACIÓN
# ==========================================

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, nuevo_saldo):
        if nuevo_saldo >= 0:
            self.__saldo = nuevo_saldo
        else:
            print("El saldo no puede ser negativo.")

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito realizado: ${cantidad:,.2f}")
        else:
            print("Cantidad inválida.")

    def retirar(self, cantidad):
        if cantidad <= 0:
            print("Cantidad inválida.")
        elif cantidad > self.__saldo:
            print("Saldo insuficiente.")
        else:
            self.__saldo -= cantidad
            print(f"Retiro realizado: ${cantidad:,.2f}")

    def mostrar_saldo(self):
        print(f"Saldo disponible: ${self.__saldo:,.2f}")


cuenta = CuentaBancaria("Juan Josè", 1000000)

print("===== CUENTA BANCARIA =====")

cuenta.mostrar_saldo()

cuenta.depositar(500000)

cuenta.mostrar_saldo()

cuenta.retirar(200000)

cuenta.mostrar_saldo()