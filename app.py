from flask import Flask,render_template,request,redirect,url_for,flash,session
app = Flask(__name__)
usuarios_registrados = {}

app.config['SECRET_KEY'] = 'una_clave_secreta_muy_larga_dificil_de_adivinar'


@app.route('/')
def index():
    return render_template('inicio.html')


@app.route('/for2')
def loo():
    return render_template('for2.html')

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/animales.html')
def animales():
    return render_template('animales.html')

@app.route('/vehiculos.html')
def vehiculos():
    return render_template('vehiculos.html')

@app.route('/maravillas')
def maravillas():
    return render_template('maravillas.html')

@app.route('/acercas')
def acercas():
    return render_template('mas.html')



@app.route('/registro', methods=("GET", "POST"))
def registro():
    error = None
    if request.method == "POST":
    
        email = request.form.get("exampleInputEmail1")
        password = request.form.get("exampleInputPassword1")
        confirmar = request.form.get("exampleCheck1")
        fecha = request.form.get("ano,mes,dia")
        genero = request.form.get("mujer,hombre,personalizado")

        if not email or not password or not confirmar or not fecha or not genero:
            error = "Todos los campos son obligatorios"

        if error:
            flash(error)
            return render_template('formulario.html')
        else:
    
            flash("¡Registro exitoso!")
            return redirect(url_for('/inicio'))

    return render_template('formulario.html')
@app.route('/login', methods=("GET", "POST"))
def login():
    error = None
    if request.method == "POST":
        email = request.form.get("exampleInputEmail1")
        password = request.form.get("exampleInputPassword1")

        if not email or not password:
            error = "Todos los campos son obligatorios"

        if error:
            flash(error)
            return render_template('inicio.html')
        else:
            flash("¡Inicio de sesión exitoso!")
            return redirect(url_for('index'))

    return render_template('inicio.html')

@app.route('/logout')
def logout():
    flash("Has cerrado sesión correctamente.")
    return redirect(url_for('/inicio'))
@app.route('/profile')
def profile():
    username = session.get('username')
    if username is not None:
        return 'user: ' + username
    return 'not logged in'

if __name__ == '__main__':
    app.run(debug=True)