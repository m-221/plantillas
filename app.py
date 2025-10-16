from flask import Flask,render_template,request,redirect,url_for,flash
app = Flask(__name__)

app.config['SECRET_KEY'] = 'una_clave_secreta_muy_larga_dificil_de_adivinar'


@app.route('/')
def index():
    return render_template('formulario')

@app.route('/for2')
def loo():
    return render_template('for2.html')

@app.route('/inicio.html')
def inicio():
    return render_template('inicio.html')

@app.route('/animales.html')
def animales():
    return render_template('animales.html')

@app.route('/vehiculos.html')
def vehiculos():
    return render_template('vehiculos.html')

@app.route('/maravillas.html')
def maravillas():
    return render_template('maravillas.html')

@app.route('/acercas.html')
def acercas():
    return render_template('mas.html')

@app.route('/' ,methods = ("GET" , "POST"))
def registro():
    error= None
    if request.method == "POST":
        nombrecompleto = request.form["nombre"]
        CORREO= request.form ["email"]
        password =request.form ["contraseña"]
        fecha =request.form ["dia"]
        fecha =request.form ["mes"]
        fecha=request.form ["año"]
        genero =request.form ["hombre"]
        genero =request.form ["mujer"]
        genero =request.form ["personalizado"]
        
        if password != contraseña:
            error = "lacontraseña no coincide"
        if error != None:
            flash(eroor)
            return render_template('formulario.html')
        else:
            (f"!registro exitoso! : {nombrecompleto}!")
            return render_template('base.html')
        

if __name__ == '__main__':
    app.run(debug=True)