from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inscripcion_curso', methods=['GET', 'POST'])
def inscripcion_curso():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        curso = request.form['curso']
        return f"Te has inscrito exitosamente al curso {curso}, {nombre} {apellidos}."
    return render_template('curso.html')

@app.route('/registro_usuarios', methods=['GET', 'POST'])
def registro_usuarios():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        return f"Usuario {nombre} {apellidos} registrado exitosamente con el correo {correo}."
    return render_template('usuario.html')

@app.route('/registro_productos', methods=['GET', 'POST'])
def registro_productos():
    if request.method == 'POST':
        producto = request.form['producto']
        categoria = request.form['categoria']
        existencia = request.form['existencia']
        precio = request.form['precio']
        return f"Producto {producto} registrado en la categoría {categoria} con {existencia} unidades a un precio de {precio}."
    return render_template('producto.html')

@app.route('/registro_libros', methods=['GET', 'POST'])
def registro_libros():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        resumen = request.form['resumen']
        medio = request.form['medio']
        return f"Libro '{titulo}' de {autor} registrado exitosamente. Medio: {medio}."
    return render_template('libro.html')

if __name__ == '__main__':
    app.run(debug=True)
