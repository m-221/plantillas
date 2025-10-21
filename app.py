from flask import Flask,render_template,request,redirect,url_for,flash
app = Flask(__name__)

app.config['SECRET_KEY'] = 'una_clave_secreta_muy_larga_dificil_de_adivinar'


@app.route('/')
def index():
    return render_template('base.html')

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

@app.route('/for2')
def loo():mmmm
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



@app.route('/formulario', methods=("GET", "POST"))
def registro():
    error = None
    if request.method == "POST":
      
        email = request.form.get("exampleInputEmail1")
        password = request.form.get("exampleInputPassword1")
        confirmar = request.form.get("exampleCheck1")

      
        if not email or not password or not confirmar:
            error = "Todos los campos son obligatorios"

        if error:
            flash(error)
            return render_template('formulario.html')
        else:
          
            flash("¡Registro exitoso!")
            return redirect(url_for('/inicio'))

    return render_template('formulario.html')

        

if __name__ == '__main__':
    app.run(debug=True)