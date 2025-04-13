import unittest
from flask import Flask
from app import app, get_db_connection


class TestApp(unittest.TestCase):
    def test_db_connection(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT 1")
            conn.close()
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"Error de conexión a la base de datos: {e}")

    # Configuración de pruebas
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        app.config["DEBUG"] = True  # Activa el modo debug

    # Prueba para la página principal
    def test_index(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)

    # Prueba para obtener clientes
    def test_clientes_get(self):
        response = self.app.get("/clientes")
        print(response.data.decode())
        self.assertEqual(response.status_code, 200)

    # Prueba para agregar un cliente (requiere BD)
    def test_clientes_post(self):
        response = self.app.post(
            "/clientes",
            data=dict(
                nombre="Juan Pérez",
                telefono="123456789",
                correo="juan@example.com",
                direccion="Calle 123",
            ),
            follow_redirects=True,
        )
        self.assertEqual(response.status_code, 200)

    # Prueba para editar un cliente
    def test_edit_cliente(self):
        response = self.app.post(
            "/clientes/1/edit",
            data=dict(
                nombre="Juan Editado",
                telefono="987654321",
                correo="editado@example.com",
                direccion="Calle Nueva",
            ),
            follow_redirects=True,
        )
        self.assertEqual(response.status_code, 200)

    # Prueba para eliminar un cliente
    def test_delete_cliente(self):
        response = self.app.post("/clientes/1/delete", follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # ---------------------------------
    # Pruebas para Productos (CRUD)
    # ---------------------------------

    # Prueba para obtener productos
    def test_productos_get(self):
        response = self.app.get("/productos")
        self.assertEqual(response.status_code, 200)

    # Prueba para agregar un producto
    def test_productos_post(self):
        response = self.app.post(
            "/productos",
            data=dict(
                nombre="Refrigerador",
                descripcion="Refrigerador de alta eficiencia",
                precio="500.00",
                cantidad="20",
                fecha_vencimiento="2025-12-31",
            ),
            follow_redirects=True,
        )
        self.assertEqual(response.status_code, 200)

    # Prueba para editar un producto
    def test_edit_producto(self):
        response = self.app.post(
            "/productos/1/edit",
            data=dict(
                nombre="Refrigerador Editado",
                descripcion="Refrigerador grande",
                precio="600.00",
                cantidad="25",
                fecha_vencimiento="2026-01-01",
            ),
            follow_redirects=True,
        )
        self.assertEqual(response.status_code, 200)

    # Prueba para eliminar un producto
    def test_delete_producto(self):
        response = self.app.post("/productos/1/delete", follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # ---------------------------------
    # Pruebas para Almacenamientos (CRUD)
    # ---------------------------------

    # Prueba para obtener almacenamientos
    def test_almacenamientos_get(self):
        response = self.app.get("/almacenamientos")
        self.assertEqual(response.status_code, 200)

    # Prueba para agregar un almacenamiento
    def test_almacenamientos_post(self):
        response = self.app.post(
            "/almacenamientos",
            data=dict(
                capacidad="1000",
                temperatura="4",
                medidas="10x10x10",
                tipo_trabajo="Frío",
                tipo_producto="Alimentos",
                humedad="80%",
                tiempo_rotacion="30",
            ),
            follow_redirects=True,
        )
        self.assertEqual(response.status_code, 200)

    # Prueba para editar un almacenamiento
    def test_edit_almacenamiento(self):
        response = self.app.post(
            "/almacenamientos/1/edit",
            data=dict(
                capacidad="1200",
                temperatura="5",
                medidas="12x12x12",
                tipo_trabajo="Congelación",
                tipo_producto="Bebidas",
                humedad="75%",
                tiempo_rotacion="25",
            ),
            follow_redirects=True,
        )
        self.assertEqual(response.status_code, 200)

    # Prueba para eliminar un almacenamiento
    def test_delete_almacenamiento(self):
        response = self.app.post(
            "/almacenamientos/1/delete", follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # ---------------------------------
    # Pruebas para Pedidos (CRUD)
    # ---------------------------------

    # Prueba para obtener pedidos
    def test_pedidos_get(self):
        response = self.app.get("/pedidos")
        self.assertEqual(response.status_code, 200)

    # Prueba para agregar un pedido
    def test_pedidos_post(self):
        response = self.app.post(
            "/pedidos",
            data=dict(
                cliente_id="1",
                fecha_pedido="2025-05-10",
                estado="Pendiente",
                ciudad="Ciudad X",
                cantidad_variable="10",
            ),
            follow_redirects=True,
        )
        self.assertEqual(response.status_code, 200)

    # Prueba para editar un pedido
    def test_edit_pedido(self):
        response = self.app.post(
            "/pedidos/1/edit",
            data=dict(
                cliente_id="1",
                fecha_pedido="2025-05-15",
                estado="Enviado",
                ciudad="Ciudad Y",
                cantidad_variable="15",
            ),
            follow_redirects=True,
        )
        self.assertEqual(response.status_code, 200)

    # Prueba para eliminar un pedido
    def test_delete_pedido(self):
        response = self.app.post("/pedidos/1/delete", follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
