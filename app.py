from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)


# Conexión a la base de datos
def get_db_connection():
    return mysql.connector.connect(
        host="localhost", user="root", password="jeffer1234", database="refrigeraciondb"
    )

# Página principal
@app.route("/")
def index():
    return render_template("index.html")


# CRUD para Clientes
@app.route("/clientes", methods=["GET", "POST"])
def clientes():
    conn = get_db_connection()
    cursor = conn.cursor()
    if request.method == "POST":
        nombre = request.form["nombre"]
        telefono = request.form["telefono"]
        correo = request.form["correo"]
        direccion = request.form["direccion"]

        cursor.execute(
            "INSERT INTO cliente (nombre, telefono, correo, direccion) VALUES (%s, %s, %s, %s)",
            (nombre, telefono, correo, direccion),
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for("success", type="cliente"))

    cursor.execute("SELECT * FROM cliente")
    clientes = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("formulario.html", clientes=clientes)


@app.route("/clientes/<int:id>/edit", methods=["GET", "POST"])
def edit_cliente(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    if request.method == "POST":
        nombre = request.form["nombre"]
        telefono = request.form["telefono"]
        correo = request.form["correo"]
        direccion = request.form["direccion"]

        cursor.execute(
            "UPDATE cliente SET nombre=%s, telefono=%s, correo=%s, direccion=%s WHERE cliente_id=%s",
            (nombre, telefono, correo, direccion, id),
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for("clientes"))

    cursor.execute("SELECT * FROM cliente WHERE cliente_id=%s", (id,))
    cliente = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template("formulario.html", cliente=cliente)


@app.route("/clientes/<int:id>/delete", methods=["POST"])
def delete_cliente(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cliente WHERE cliente_id=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for("clientes"))


# CRUD para Productos
@app.route("/productos", methods=["GET", "POST"])
def productos():
    conn = get_db_connection()
    cursor = conn.cursor()
    if request.method == "POST":
        nombre = request.form["nombre"]
        descripcion = request.form["descripcion"]
        precio = request.form["precio"]
        cantidad = request.form["cantidad"]
        fecha_vencimiento = request.form["fecha_vencimiento"]

        cursor.execute(
            "INSERT INTO producto (nombre, descripcion, precio, cantidad, fecha_vencimiento) VALUES (%s, %s, %s, %s, %s)",
            (nombre, descripcion, precio, cantidad, fecha_vencimiento),
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for("success", type="producto"))

    cursor.execute("SELECT * FROM producto")
    productos = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("datos-productos.html", productos=productos)


@app.route("/productos/<int:id>/edit", methods=["GET", "POST"])
def edit_producto(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    if request.method == "POST":
        nombre = request.form["nombre"]
        descripcion = request.form["descripcion"]
        precio = request.form["precio"]
        cantidad = request.form["cantidad"]
        fecha_vencimiento = request.form["fecha_vencimiento"]

        cursor.execute(
            "UPDATE producto SET nombre=%s, descripcion=%s, precio=%s, cantidad=%s, fecha_vencimiento=%s WHERE producto_id=%s",
            (nombre, descripcion, precio, cantidad, fecha_vencimiento, id),
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for("productos"))

    cursor.execute("SELECT * FROM producto WHERE producto_id=%s", (id,))
    producto = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template("datos-productos.html", producto=producto)


@app.route("/productos/<int:id>/delete", methods=["POST"])
def delete_producto(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM producto WHERE producto_id=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for("productos"))


# CRUD para Almacenamientos
@app.route("/almacenamientos", methods=["GET", "POST"])
def almacenamientos():
    conn = get_db_connection()
    cursor = conn.cursor()
    if request.method == "POST":
        capacidad = request.form["capacidad"]
        temperatura = request.form["temperatura"]
        medidas = request.form["medidas"]
        tipo_trabajo = request.form["tipo_trabajo"]
        tipo_producto = request.form["tipo_producto"]
        humedad = request.form["humedad"]
        tiempo_rotacion = request.form["tiempo_rotacion"]

        cursor.execute(
            "INSERT INTO cuarto_refrigeracion (capacidad, temperatura, medidas, tipo_trabajo, tipo_producto, humedad, tiempo_rotacion) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (
                capacidad,
                temperatura,
                medidas,
                tipo_trabajo,
                tipo_producto,
                humedad,
                tiempo_rotacion,
            ),
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for("success", type="almacenamiento"))

    cursor.execute("SELECT * FROM cuarto_refrigeracion")
    almacenamientos = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template(
        "almacenamiento-productos.html", almacenamientos=almacenamientos
    )


@app.route("/almacenamientos/<int:id>/edit", methods=["GET", "POST"])
def edit_almacenamiento(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    if request.method == "POST":
        capacidad = request.form["capacidad"]
        temperatura = request.form["temperatura"]
        medidas = request.form["medidas"]
        tipo_trabajo = request.form["tipo_trabajo"]
        tipo_producto = request.form["tipo_producto"]
        humedad = request.form["humedad"]
        tiempo_rotacion = request.form["tiempo_rotacion"]

        cursor.execute(
            "UPDATE cuarto_refrigeracion SET capacidad=%s, temperatura=%s, medidas=%s, tipo_trabajo=%s, tipo_producto=%s, humedad=%s, tiempo_rotacion=%s WHERE cuarto_id=%s",
            (
                capacidad,
                temperatura,
                medidas,
                tipo_trabajo,
                tipo_producto,
                humedad,
                tiempo_rotacion,
                id,
            ),
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for("almacenamientos"))

    cursor.execute("SELECT * FROM cuarto_refrigeracion WHERE cuarto_id=%s", (id,))
    almacenamiento = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template(
        "almacenamiento-productos.html", almacenamiento=almacenamiento
    )


@app.route("/almacenamientos/<int:id>/delete", methods=["POST"])
def delete_almacenamiento(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cuarto_refrigeracion WHERE cuarto_id=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for("almacenamientos"))


# CRUD para Pedidos
@app.route("/pedidos", methods=["GET", "POST"])
def pedidos():
    conn = get_db_connection()
    cursor = conn.cursor()
    if request.method == "POST":
        cliente_id = request.form["cliente_id"]
        fecha_pedido = request.form["fecha_pedido"]
        estado = request.form["estado"]
        ciudad = request.form["ciudad"]
        cantidad_variable = request.form["cantidad_variable"]

        cursor.execute(
            "INSERT INTO pedido (cliente_id, fecha_pedido, estado, ciudad, cantidad_variable) VALUES (%s, %s, %s, %s, %s)",
            (cliente_id, fecha_pedido, estado, ciudad, cantidad_variable),
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for("success", type="pedido"))

    cursor.execute("SELECT * FROM pedido")
    pedidos = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("datos-pedidos.html", pedidos=pedidos)


@app.route("/pedidos/<int:id>/edit", methods=["GET", "POST"])
def edit_pedido(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    if request.method == "POST":
        cliente_id = request.form["cliente_id"]
        fecha_pedido = request.form["fecha_pedido"]
        estado = request.form["estado"]
        ciudad = request.form["ciudad"]
        cantidad_variable = request.form["cantidad_variable"]

        cursor.execute(
            "UPDATE pedido SET cliente_id=%s, fecha_pedido=%s, estado=%s, ciudad=%s, cantidad_variable=%s WHERE pedido_id=%s",
            (cliente_id, fecha_pedido, estado, ciudad, cantidad_variable, id),
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for("pedidos"))

    cursor.execute("SELECT * FROM pedido WHERE pedido_id=%s", (id,))
    pedido = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template("datos-pedidos.html", pedido=pedido)


@app.route("/pedidos/<int:id>/delete", methods=["POST"])
def delete_pedido(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM pedido WHERE pedido_id=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for("pedidos"))


# Página de éxito
@app.route("/success/<type>")
def success(type):
    return render_template("success.html", type=type)


if __name__ == "__main__":
    app.run(debug=True)
