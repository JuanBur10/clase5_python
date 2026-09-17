# ==========================================
# TALLER DE ENCAPSULACIÓN - CASO 2
# ==========================================

class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def consultar_saldo(self):
        return self.__saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print("Depósito realizado.")
        else:
            print("Cantidad inválida.")

    def retirar(self, cantidad):
        if cantidad > self.__saldo:
            print("Saldo insuficiente.")
        elif cantidad > 0:
            self.__saldo -= cantidad
            print("Retiro realizado.")
        else:
            print("Cantidad inválida.")


cuenta = Cuenta("Juan Josè", 1000000)

print("===== CUENTA =====")
print(f"Titular: {cuenta.titular}")
print(f"Saldo: ${cuenta.consultar_saldo():,.2f}")

cuenta.depositar(500000)
cuenta.retirar(200000)

print(f"Saldo final: ${cuenta.consultar_saldo():,.2f}")