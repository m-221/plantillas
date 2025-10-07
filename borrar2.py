from flask import Flask
app = Flask(__name__)

@app.route('/')
def hol():
    mensaje = '<h1>¡Hola bienvenidos!</h1>'
    mensaje += '<ol>'
    mensaje += '<li><h2>1.- animales: http://127.0.0.1:5000/animales</h2></li>'
    mensaje += '<li><h2>2.- carros: http://127.0.0.1:5000/carros</h2></li>'
    mensaje += '<li><h2>3.- mundo: http://127.0.0.1:5000/mundo</h2></li>'
    mensaje += '<li><h2>4.- acerca: http://127.0.0.1:5000/acerca</h2></li>'
    mensaje += '</ol>'
    return mensaje

@app.route('/animales')
def animales():
    mensaje = '<h1>Animales Exóticos</h1>'
    mensaje += '<h3>🌸 La Belleza del Reino Animal</h3>'

    mensaje += '<p>Los animales son una de las maravillas más grandes de la naturaleza. Cada uno, con sus colores, formas y comportamientos únicos, nos demuestra lo increíblemente diversa y hermosa que es la vida en nuestro planeta. Desde los peces que iluminan las profundidades del océano hasta las aves que pintan el cielo con sus alas, todos los seres vivos tienen una historia que contar. 🐠🦜🐆Observarlos nos enseña a valorar la perfección de la naturaleza, a respetar la vida y a cuidar nuestro entorno. Porque en cada mirada, cada canto y cada movimiento, los animales nos recuerdan que la belleza está en todas partes… solo hay que saber mirar. 🌿💫</p>'
    mensaje += '<p> 🦑 2. Calamar Gigante

Dato curioso: Puede medir más de 13 metros de largo y vive en las profundidades del océano.

Curiosidad: Sus ojos son del tamaño de un balón de fútbol.</p>' 
    return mensaje

@app.route('/restar/<v1>/<v2>')
def restar1(v1, v2):
    s = str(float(v1) - float(v2))
    mensaje = f'<h1>La resta de {v1} - {v2} es {s}</h1>'
    return mensaje

@app.route('/dividir/<v1>/<v2>')
def dividir1(v1, v2):
        m = float(v1) / float(v2)
        mensaje = f'<h1>La división de {v1} / {v2} es {m}</h1>'
        return mensaje

@app.route('/multiplicar/<v1>/<v2>')
def multiplicar1(v1, v2):
    r = float(v1) * float(v2)
    mensaje = f'<h1>La multiplicación de {v1} * {v2} es {r}</h1>'
    return mensaje

if __name__ == '__main__':
    app.run(debug=True)