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


if __name__ == "__main__":
    unittest.main()
