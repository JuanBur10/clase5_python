# ==========================================
# SISTEMA DE PRÉSTAMOS DE EQUIPOS
# ==========================================

from equipo import Equipo
from usuario import Usuario
from prestamo import Prestamo


equipos = {}
usuarios = {}
prestamos = []


def registrar_equipo():
    codigo = input("Código del equipo: ")
    nombre = input("Nombre del equipo: ")
    categoria = input("Categoría: ")

    if codigo in equipos:
        print("Ya existe un equipo con ese código.")
        return

    equipo = Equipo(codigo, nombre, categoria)
    equipos[codigo] = equipo

    print("Equipo registrado correctamente.")


def registrar_usuario():
    documento = input("Documento del usuario: ")
    nombre = input("Nombre del usuario: ")

    if documento in usuarios:
        print("El usuario ya existe.")
        return

    usuario = Usuario(documento, nombre)
    usuarios[documento] = usuario

    print("Usuario registrado correctamente.")


def realizar_prestamo():
    documento = input("Documento del usuario: ")
    codigo = input("Código del equipo: ")

    if documento not in usuarios:
        print("El usuario no existe.")
        return

    if codigo not in equipos:
        print("El equipo no existe.")
        return

    usuario = usuarios[documento]
    equipo = equipos[codigo]

    if not equipo.esta_disponible():
        print("El equipo no está disponible.")
        return

    equipo.prestar()

    prestamo = Prestamo(usuario, equipo)

    usuario.agregar_prestamo(prestamo)
    prestamos.append(prestamo)

    print("Préstamo registrado correctamente.")


def devolver_equipo():
    codigo = input("Código del equipo a devolver: ")

    if codigo not in equipos:
        print("El equipo no existe.")
        return

    for prestamo in prestamos:

        if (
            prestamo.equipo.codigo == codigo
            and prestamo.esta_activo()
        ):
            prestamo.devolver()
            print("Equipo devuelto correctamente.")
            return

    print("No existe un préstamo activo para este equipo.")


def consultar_equipos():
    print("\n===== EQUIPOS =====")

    if not equipos:
        print("No hay equipos registrados.")
        return

    print(
        f"{'Código':<10}"
        f"{'Nombre':<25}"
        f"{'Categoría':<20}"
        f"Estado"
    )

    print("-" * 70)

    for equipo in equipos.values():
        equipo.mostrar_informacion()


def consultar_usuarios():
    print("\n===== USUARIOS =====")

    if not usuarios:
        print("No hay usuarios registrados.")
        return

    for usuario in usuarios.values():
        usuario.mostrar_informacion()
        print("-" * 30)


def consultar_prestamos():
    print("\n===== PRÉSTAMOS =====")

    if not prestamos:
        print("No hay préstamos registrados.")
        return

    for prestamo in prestamos:
        prestamo.mostrar_informacion()
        print("-" * 30)


def menu():
    while True:

        print("\n")
        print("=" * 45)
        print(" SISTEMA DE PRÉSTAMOS DE EQUIPOS")
        print("=" * 45)
        print("1. Registrar equipo")
        print("2. Registrar usuario")
        print("3. Realizar préstamo")
        print("4. Devolver equipo")
        print("5. Consultar equipos")
        print("6. Consultar usuarios")
        print("7. Consultar préstamos")
        print("8. Salir")
        print("=" * 45)

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_equipo()

        elif opcion == "2":
            registrar_usuario()

        elif opcion == "3":
            realizar_prestamo()

        elif opcion == "4":
            devolver_equipo()

        elif opcion == "5":
            consultar_equipos()

        elif opcion == "6":
            consultar_usuarios()

        elif opcion == "7":
            consultar_prestamos()

        elif opcion == "8":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()