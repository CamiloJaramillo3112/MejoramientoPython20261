from data.registros import ventas_restaurante


def mostrar_ventas():
    print("\n--- LISTA DE VENTAS ---")

    if len(ventas_restaurante) == 0:
        print("No hay ventas registradas.")
        return

    for venta in ventas_restaurante:
        print("-----------------------------")
        print(f"ID Venta: {venta['idVenta']}")
        print(f"Cliente: {venta['nombreCliente']}")
        print(f"Mesa: {venta['numeroMesa']}")
        print(f"Plato principal: {venta['platoPrincipal']}")
        print(f"Valor consumo: ${venta['valorConsumo']}")
        print(f"Método de pago: {venta['metodoPago']}")
        print(f"Estado del pedido: {venta['estadoPedido']}")
    print("-----------------------------")


def ordenar_ventas():
    print("\n--- ORDENAR VENTAS POR VALOR DE CONSUMO ---")
    ventas_restaurante.sort(key=lambda venta: venta["valorConsumo"])
    print("Ventas ordenadas de menor a mayor.")


def buscar_venta():
    print("\n--- BUSCAR VENTA ---")
    id_buscar = int(input("Ingrese el idVenta que desea buscar: "))

    for venta in ventas_restaurante:
        if venta["idVenta"] == id_buscar:
            print("\nVenta encontrada:")
            print("-----------------------------")
            print(f"ID Venta: {venta['idVenta']}")
            print(f"Cliente: {venta['nombreCliente']}")
            print(f"Mesa: {venta['numeroMesa']}")
            print(f"Plato principal: {venta['platoPrincipal']}")
            print(f"Valor consumo: ${venta['valorConsumo']}")
            print(f"Método de pago: {venta['metodoPago']}")
            print(f"Estado del pedido: {venta['estadoPedido']}")
            print("-----------------------------")
            return

    print("No se encontró una venta con ese ID.")


def eliminar_venta():
    print("\n--- ELIMINAR VENTA ---")
    id_eliminar = int(input("Ingrese el idVenta que desea eliminar: "))

    for venta in ventas_restaurante:
        if venta["idVenta"] == id_eliminar:
            ventas_restaurante.remove(venta)
            print("Venta eliminada correctamente.")
            return

    print("No se encontró una venta con ese ID.")


def agregar_venta():
    print("\n--- AGREGAR NUEVA VENTA ---")

    id_venta = int(input("Ingrese el ID de la venta: "))
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    numero_mesa = int(input("Ingrese el número de mesa: "))
    plato_principal = input("Ingrese el plato principal: ")
    valor_consumo = float(input("Ingrese el valor del consumo: "))
    metodo_pago = input("Ingrese el método de pago (EFECTIVO, TARJETA, TRANSFERENCIA): ").upper()
    estado_pedido = input("Ingrese el estado del pedido (ENTREGADO o PENDIENTE): ").upper()

    nueva_venta = {
        "idVenta": id_venta,
        "nombreCliente": nombre_cliente,
        "numeroMesa": numero_mesa,
        "platoPrincipal": plato_principal,
        "valorConsumo": valor_consumo,
        "metodoPago": metodo_pago,
        "estadoPedido": estado_pedido
    }

    ventas_restaurante.append(nueva_venta)
    print("Nueva venta agregada correctamente.")