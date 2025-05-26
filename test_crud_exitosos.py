import unittest
from crud import crear_producto, obtener_productos, actualizar_producto, eliminar_producto

class TestCRUDExitosos(unittest.TestCase):

    def test_crear_producto_valido(self):
        crear_producto("TestProducto", "Producto de prueba", 999.99, 10)
        productos = obtener_productos()
        self.assertTrue(any(p[1] == "TestProducto" for p in productos))

    def test_obtener_productos_con_datos(self):
        productos = obtener_productos()
        self.assertIsInstance(productos, list)
        self.assertGreater(len(productos), 0)

    def test_actualizar_producto_valido(self):
        productos = obtener_productos()
        if productos:
            producto = productos[-1]
            actualizar_producto(producto[0], "Actualizado", "Actualizado desc", 123.45, 5)
            actualizados = obtener_productos()
            self.assertTrue(any(p[1] == "Actualizado" for p in actualizados))

    def test_eliminar_producto_existente(self):
        crear_producto("Eliminar", "Borrar este", 100.0, 1)
        productos = obtener_productos()
        producto = next(p for p in productos if p[1] == "Eliminar")
        eliminar_producto(producto[0])
        nuevos = obtener_productos()
        self.assertFalse(any(p[0] == producto[0] for p in nuevos))

if __name__ == "__main__":
    unittest.main()
