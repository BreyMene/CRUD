# interface.py

from crud import crear_producto, obtener_productos, actualizar_producto, eliminar_producto

def iniciar_interface():
    while True:
        print("\n===== MENÚ CRUD =====")
        print("1. Crear producto")
        print("2. Ver productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        match opcion:
            case "1":
                nombre = input("Nombre: ")
                descripcion = input("Descripción: ")
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad: "))
                crear_producto(nombre, descripcion, precio, cantidad)

            case "2":
                productos = obtener_productos()
                if productos:
                    print("\n=== Lista de Productos ===")
                    for p in productos:
                        print(f"{p[0]}. {p[1]} | {p[2]} | Precio: ${p[3]} | Cantidad: {p[4]}")
                else:
                    print("No hay productos registrados.")

            case "3":
                id_producto = int(input("ID del producto a actualizar: "))
                nombre = input("Nuevo nombre: ")
                descripcion = input("Nueva descripción: ")
                precio = float(input("Nuevo precio: "))
                cantidad = int(input("Nueva cantidad: "))
                actualizar_producto(id_producto, nombre, descripcion, precio, cantidad)

            case "4":
                id_producto = int(input("ID del producto a eliminar: "))
                eliminar_producto(id_producto)

            case "5":
                print("Saliendo...")
                break

            case _:
                print("Opción no válida. Intente nuevamente.")
