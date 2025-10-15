from flask import Flask,render_template
app = Flask(__name__)


@app.route('/')
def index0():
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

if __name__ == '__main__':
    app.run(debug=True)