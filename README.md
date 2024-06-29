import json
from datetime import datetime

ventas = []

pizzas = {
    'cuatro quesos' : {'pequeña':6000,'mediana':9000,'familiar':12000},
    'hawaiana': {'pequeña':6000,'mediana':9000,'familiar':12000},
    'napolitana': {'pequeña':5500,'mediana':8500,'familiar':11000},
    'pepperoni': {'pequeña':7000,'mediana':10000,'familiar':13000}
}

def menu():
    print('Menu Pizzas DuocUC')
    print('1. Registrar una venta')
    print('2. Mostrar todas las ventas')
    print('3. Ver las ventas por cliente')
    print('4. Guardar las ventas en un archivo')
    print('5. Cargar ventas desde un archivo')
    print('6. Generar boleta')
    print('7. Anular una venta')
    print('8. Salir del programa')
    opcion = input("Elija una opción: ")
    return opcion

def registrar_venta():
    nombre_cliente = input("Nombre del cliente: ")
    tipo_cliente = input("Tipo de cliente (diurno/vespertino/administrativo): ").lower()
    tipo_pizza = input("Tipo de pizza (cuatro quesos/hawaiana/napolitana/pepperoni): ").lower()
    tamaño_pizza = input("Tamaño de la pizza (pequeña/mediana/familiar): ").lower()

    if tipo_pizza not in pizzas or tamaño_pizza not in pizzas[tipo_pizza]:
        print("Tipo o tamaño de pizza inválido.")
        return

    precio = pizzas[tipo_pizza][tamaño_pizza]

    descuento = 0
    if tipo_cliente == 'diurno':
        descuento = 0.12
    elif tipo_cliente == 'vespertino':
        descuento = 0.14
    elif tipo_cliente == 'administrativo':
        descuento = 0.10

    precio_final = precio * (1 - descuento)

    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    venta = {
        "fecha_hora": fecha_hora,
        "nombre_cliente": nombre_cliente,
        "tipo_cliente": tipo_cliente,
        "tipo_pizza": tipo_pizza,
        "tamaño_pizza": tamaño_pizza,
        "precio_original": precio,
        "descuento": descuento,
        "precio_final": precio_final
    }
    ventas.append(venta)
    print(f"\nVenta registrada:\n")
    print(f"Fecha y hora: {fecha_hora}")
    print(f"Cliente: {nombre_cliente}")
    print(f"Tipo de cliente: {tipo_cliente}")
    print(f"Tipo de pizza: {tipo_pizza}")
    print(f"Tamaño de pizza: {tamaño_pizza}")
    print(f"Precio original: {precio}")
    print(f"Descuento aplicado: {descuento * 100}%")
    print(f"Precio final: {precio_final}")

def mostrar_ventas():
    if not ventas:
        print("No hay ventas registradas.")
    else:
        for venta in ventas:
            print(venta)

def buscar_ventas():
    nombre_cliente = input("Ingrese el nombre del cliente a buscar: ")
    ventas_cliente = [venta for venta in ventas if venta["nombre_cliente"] == nombre_cliente]

    if not ventas_cliente:
        print(f"No se encontraron ventas para el cliente {nombre_cliente}.")
    else:
        for venta in ventas_cliente:
            print(venta)

def guardar_ventas():
    with open('ventas.json', 'w') as file:
        json.dump(ventas, file, indent=4)
    print("Ventas guardadas en 'ventas.json'.")

def cargar_ventas():
    global ventas
    try:
        with open('ventas.json', 'r') as file:
            ventas = json.load(file)
        print("Ventas cargadas desde 'ventas.json'.")
    except FileNotFoundError:
        print("No se encontró el archivo 'ventas.json'.")

def generar_boleta():
    if not ventas:
        print("No hay ventas registradas para generar una boleta.")
        return
    
    ultima_venta = ventas[-1] 

    print('Boleta Electrónica')
    print('-----------------------------------------------')
    print(f"Fecha y hora: {ultima_venta['fecha_hora']}")
    print(f"Cliente: {ultima_venta['nombre_cliente']}")
    print(f"Tipo de cliente: {ultima_venta['tipo_cliente']}")
    print(f"Tipo de pizza: {ultima_venta['tipo_pizza']}")
    print(f"Tamaño de pizza: {ultima_venta['tamaño_pizza']}")
    print('-----------------------------------------------')
    print(f"Subtotal: ${ultima_venta['precio_original']}")
    descuento_aplicado = ultima_venta['precio_original'] * ultima_venta['descuento']
    print(f"Descuento: ${descuento_aplicado}")
    print(f"Total a pagar: ${ultima_venta['precio_final']}")
    print('-----------------------------------------------')

def anular_compra():
    if not ventas:
        print("No hay ventas registradas para anular.")
        return
    
    nombre_cliente = input("Ingrese el nombre del cliente de la venta a anular: ")
    fecha_venta = input("Ingrese la fecha de la venta (YYYY-MM-DD HH:MM:SS): ")

    ventas_filtradas = [venta for venta in ventas if venta["nombre_cliente"] == nombre_cliente and venta["fecha_hora"] == fecha_venta]

    if not ventas_filtradas:
        print(f"No se encontró una venta para el cliente {nombre_cliente} en la fecha {fecha_venta}.")
    else:
        venta_a_anular = ventas_filtradas[0]
        ventas.remove(venta_a_anular)
        print("Venta anulada correctamente.")

def main():
    while True:
        opcion = menu()
        if opcion == '1':
            registrar_venta()
        elif opcion == '2':
            mostrar_ventas()
        elif opcion == '3':
            buscar_ventas()
        elif opcion == '4':
            guardar_ventas()
        elif opcion == '5':
            cargar_ventas()
        elif opcion == '6':
            generar_boleta()
        elif opcion == '7':
            anular_compra()
        elif opcion == '8':
            print(".")
            break
        else:
            print(".")

if __name__ == "__main__":
    main()
