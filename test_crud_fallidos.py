import unittest
import io
from contextlib import redirect_stdout
from crud import crear_producto, obtener_productos, actualizar_producto, eliminar_producto

class TestCRUDFallidos(unittest.TestCase):

    def test_crear_producto_valor_invalido(self):
        f = io.StringIO()
        with redirect_stdout(f):
            try:
                crear_producto("Producto Test", "Descripción", "mil", 10)  # 'mil' es inválido
            except Exception:
                pass
        salida = f.getvalue()
        self.assertIn("Error al crear producto", salida)
        print("Crear (fallido): completado")

    def test_obtener_productos_vacio(self):
        productos = obtener_productos()
        self.assertEqual(len(productos), 0, "Se esperaban 0 productos en la base de datos.")
        print("Read (fallido): completado")

    def test_actualizar_producto_id_inexistente(self):
        f = io.StringIO()
        with redirect_stdout(f):
            actualizar_producto(9999, "Nuevo", "Descripción", 100, 10)  # ID 9999 no existe
        salida = f.getvalue()
        self.assertIn("No se encontró el producto con ese ID.", salida)
        print("Update (fallido): completado")

    def test_eliminar_producto_id_inexistente(self):
        f = io.StringIO()
        with redirect_stdout(f):
            eliminar_producto(9999)  # ID 9999 no existe
        salida = f.getvalue()
        self.assertIn("No se encontró el producto con ese ID.", salida)
        print("Delete (fallido): completado")


if __name__ == "__main__":
    unittest.main()
