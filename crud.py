from connection import obtener_conexion

def crear_producto(nombre, descripcion, precio, cantidad):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    try:
        cursor.execute(
            "INSERT INTO productos (nombre, descripcion, precio, cantidad) VALUES (%s, %s, %s, %s)",
            (nombre, descripcion, precio, cantidad)
        )
        conexion.commit()
        print("Producto creado correctamente.")
    except Exception as e:
        print("Error al crear producto:", e)
    finally:
        cursor.close()
        conexion.close()

def obtener_productos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        return productos
    except Exception as e:
        print("Error al obtener productos:", e)
        return []
    finally:
        cursor.close()
        conexion.close()

def actualizar_producto(id_producto, nombre, descripcion, precio, cantidad):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    try:
        cursor.execute(
            """
            UPDATE productos 
            SET nombre=%s, descripcion=%s, precio=%s, cantidad=%s 
            WHERE id=%s
            """,
            (nombre, descripcion, precio, cantidad, id_producto)
        )
        conexion.commit()
        if cursor.rowcount == 0:
            print("No se encontró el producto con ese ID.")
        else:
            print("Producto actualizado correctamente.")
    except Exception as e:
        print("Error al actualizar producto:", e)
    finally:
        cursor.close()
        conexion.close()

def eliminar_producto(id_producto):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    try:
        cursor.execute("DELETE FROM productos WHERE id=%s", (id_producto,))
        conexion.commit()
        if cursor.rowcount == 0:
            print("No se encontró el producto con ese ID.")
        else:
            print("Producto eliminado correctamente.")
    except Exception as e:
        print("Error al eliminar producto:", e)
    finally:
        cursor.close()
        conexion.close()
