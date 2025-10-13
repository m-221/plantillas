from flask import Flask,render_template
app = Flask(__name__)


@app.route('/')
def index0():
    return render_template('inicio.html')

@app.route('/animales')
def index2():
    return render_template('animales.html')

@app.route('/vehiculos')
def index3():
    return render_template('vehiculos.html')

@app.route('/maravillas')
def index4():
    return render_template('maravillas.html')

@app.route('/acercas')
def index5():
    return render_template('mas.html')

if __name__ == '__main__':
    app.run(debug=True)