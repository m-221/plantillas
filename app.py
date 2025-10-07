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
    mensaje += '<h3> 🦑 1. Calamar Gigante</h3>'
    mensaje += '<p>El calamar gigante (Architeuthis dux) es una de las criaturas más misteriosas y fascinantes de los océanos. Aunque se ha documentado de manera limitada debido a su naturaleza esquiva y habitar en profundidades extremas, se sabe que puede alcanzar longitudes impresionantes de hasta 13 metros, lo que lo convierte en uno de los invertebrados más grandes del planeta. Su cuerpo es alargado y flexible, y tiene unos ojos de un tamaño sorprendente, los más grandes del reino animal, con un diámetro que puede superar los 25 centímetros.</p>' 
    mensaje += '<p>Uno de los aspectos más intrigantes del calamar gigante es su capacidad para cazar en la oscuridad profunda del océano. Se alimenta principalmente de peces y calamares más pequeños, utilizando sus largos tentáculos armados con ventosas y garfios para atrapar a sus presas. Aunque se sabe que existe, la mayoría de lo que se conoce sobre su biología proviene de ejemplares encontrados muertos o grabaciones de su caza a grandes profundidades, por lo que su comportamiento real sigue siendo en gran parte un enigma. </p>'
    mensaje += '<p>El calamar gigante ha capturado la imaginación popular por siglos, a menudo asociado con leyendas de monstruos marinos como el Kraken. Si bien no hay evidencia de que el calamar ataque barcos, su tamaño y naturaleza furtiva han contribuido a su estatus de criatura mitológica. A pesar de los avances en la ciencia marina, gran parte de su vida y comportamiento siguen siendo un misterio debido a la dificultad de estudiarlo en su hábitat natural.</p>'
    return mensaje


@app.route('/carros')
def carros():
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