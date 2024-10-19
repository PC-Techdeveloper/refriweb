from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

# Conectando a la base de datos MySQL
db = mysql.connector.connect(
    host="localhost:3306",
    user="root",
    password="jeffer1234",
    database="refrigeraciondb",
)

# Crea el cursor para ejecutas las consultas
cursor = db.cursor()


# Rutas para las operaciones CRUD


# 1. Crear cliente
@app.route("/crear_cliente", methods=["POST"])
def crear_cliente():
    nombre = request.form["nombre"]
    celular = request.form["celular"]
    correo = request.form["correo"]
    direccion = request.form["direccion"]

    sql = "INSERT INTO clientes (nombre, celular, correo, direccion) VALUES (%s, %s, %s, %s)"
    values = (nombre, celular, correo, direccion)

    cursor.execute(sql, values)
    db.commit()
    return jsonify({"message": "Cliente creado exitosamente!"})


# 2. Leer clientes
@app.route("/clientes", methods=["GET"])
def obtener_clientes():
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    return jsonify(clientes)


# 3. Actualizar cliente
@app.route("/actualizar_cliente/<int:id>", methods=["PUT"])
def actualizar_cliente(id):
    nombre = request.form["nombre"]
    celular = request.form["celular"]
    correo = request.form["correo"]
    direccion = request.form["direccion"]

    sql = (
        "UPDATE clientes SET nombre=%s, celular=%s, correo=%s, direccion=%s WHERE id=%s"
    )
    values = (nombre, celular, correo, direccion, id)

    cursor.execute(sql, values)
    db.commit()
    return jsonify({"message": "Cliente actualizado exitosamente!"})


# 4. Eliminar cliente
@app.route("/eliminar_cliente/<int:id>", methods=["DELETE"])
def eliminar_cliente(id):
    sql = "DELETE FROM clientes WHERE id=%s"
    cursor.execute(sql, (id,))
    db.commit()
    return jsonify({"message": "Cliente eliminado exitosamente!"})


# Ruta para renderizar el formulario HTML
@app.route("/")
def formulario():
    return render_template("formulario.html")


if __name__ == "__main__":
    app.run(debug=True)
