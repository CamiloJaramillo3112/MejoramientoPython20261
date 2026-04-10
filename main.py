from modules.usuarios import registrar_usuario, iniciar_sesion
from modules.ventas import (
    mostrar_ventas,
    ordenar_ventas,
    buscar_venta,
    eliminar_venta,
    agregar_venta
)


def menu_ventas():
    while True:
        print("\n===== GESTIONAR VENTAS DEL RESTAURANTE =====")
        print("1. Mostrar todas las ventas registradas")
        print("2. Ordenar ventas por valorConsumo")
        print("3. Buscar una venta por idVenta")
        print("4. Eliminar una venta")
        print("5. Agregar una nueva venta")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_ventas()
        elif opcion == "2":
            ordenar_ventas()
            mostrar_ventas()
        elif opcion == "3":
            buscar_venta()
        elif opcion == "4":
            eliminar_venta()
        elif opcion == "5":
            agregar_venta()
        elif opcion == "6":
            print("Saliendo del menú de ventas...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


def main():
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            acceso = iniciar_sesion()
            if acceso:
                menu_ventas()
            else:
                break
        elif opcion == "3":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida.")


main()