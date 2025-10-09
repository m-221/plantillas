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
    mensaje += '<p>Los animales son una de las maravillas más grandes de la naturaleza. Cada uno, con sus colores, formas y comportamientos únicos, nos demuestra lo increíblemente diversa y hermosa que es la vida en nuestro planeta. Desde los peces que iluminan las profundidades del océano hasta las aves que pintan el cielo con sus alas, todos los seres vivos tienen una historia que contar. 🐠🦜🐆Observarlos nos enseña a valorar la perfección de la naturaleza, a respetar la vida y a cuidar nuestro entorno. Porque en cada mirada, cada canto y cada movimiento, los animales nos recuerdan que la belleza está en todas partes… solo hay que saber mirar. 🌿💫 A continuación te mostrare 6 especies facinantes...</p>'
    mensaje += '<h3> 🦑 1. Calamar Gigante</h3>'
    mensaje += '<p>El calamar gigante (Architeuthis dux) es una de las criaturas más misteriosas y fascinantes de los océanos. Aunque se ha documentado de manera limitada debido a su naturaleza esquiva y habitar en profundidades extremas, se sabe que puede alcanzar longitudes impresionantes de hasta 13 metros, lo que lo convierte en uno de los invertebrados más grandes del planeta. Su cuerpo es alargado y flexible, y tiene unos ojos de un tamaño sorprendente, los más grandes del reino animal, con un diámetro que puede superar los 25 centímetros.</p>' 
    mensaje += '<p>Uno de los aspectos más intrigantes del calamar gigante es su capacidad para cazar en la oscuridad profunda del océano. Se alimenta principalmente de peces y calamares más pequeños, utilizando sus largos tentáculos armados con ventosas y garfios para atrapar a sus presas. Aunque se sabe que existe, la mayoría de lo que se conoce sobre su biología proviene de ejemplares encontrados muertos o grabaciones de su caza a grandes profundidades, por lo que su comportamiento real sigue siendo en gran parte un enigma. </p>'
    mensaje += '<p>El calamar gigante ha capturado la imaginación popular por siglos, a menudo asociado con leyendas de monstruos marinos como el Kraken. Si bien no hay evidencia de que el calamar ataque barcos, su tamaño y naturaleza furtiva han contribuido a su estatus de criatura mitológica. A pesar de los avances en la ciencia marina, gran parte de su vida y comportamiento siguen siendo un misterio debido a la dificultad de estudiarlo en su hábitat natural.</p>'
    mensaje += '<img src="static/cala.jpeg"  alt="Calamar Gigante" width="300">'
    mensaje += '<h3> 2.El Delfín Nariz de Botella 🐬</h3>'
    mensaje += '<p>El delfín nariz de botella (Tursiops truncatus) es una de las especies de delfines más conocidas y estudiadas. Se caracteriza por su hocico alargado y su inteligencia excepcional. Estos delfines son muy sociales y suelen vivir en grupos llamados manadas, donde establecen fuertes lazos entre sí.El delfín nariz de botella (Tursiops truncatus) es uno de los animales marinos más fascinantes e inteligentes del planeta. Habita en mares cálidos y templados de casi todo el mundo, especialmente en zonas costeras, donde encuentra abundante alimento y puede interactuar con otros delfines. Su cuerpo es alargado y aerodinámico, mide entre dos y cuatro metros de longitud, y su piel es lisa de color gris con tonos más claros en el vientre.</p>'
    mensaje += '<p>Estos delfines son conocidos por su gran inteligencia y sociabilidad. Viven en grupos llamados manadas o pods, en los que cooperan para cazar peces, protegerse de los depredadores y cuidar a sus crías. Su forma de comunicarse es muy compleja, ya que utilizan una combinación de chasquidos y silbidos. Cada individuo tiene un “silbido firma” único, parecido a un nombre propio, que permite que se reconozcan entre ellos. Además, el delfín nariz de botella ha demostrado una notable capacidad para aprender y resolver problemas, incluso para interactuar con humanos en investigaciones y rescates. Su comportamiento curioso, amistoso y juguetón lo convierte en un símbolo de la inteligencia y armonía del mundo marino, y en un recordatorio de la importancia de cuidar nuestros océanos. Además, el delfín nariz de botella ha demostrado una notable capacidad para aprender y resolver problemas, incluso para interactuar con humanos en investigaciones y rescates. Su comportamiento curioso, amistoso y juguetón lo convierte en un símbolo de la inteligencia y armonía del mundo marino, y en un recordatorio de la importancia de cuidar nuestros océanos.</p>'
    mensaje += '<img src="static/delf.jpeg"  alt="Delfín Nariz de Botella" width="300">'
    mensaje += '<h3>🐘 3. Elefante Africano</h3>'
    mensaje += '<p>El elefante africano (Loxodonta africana) es el mamífero terrestre más grande del mundo y un símbolo icónico de la vida salvaje en África. Estos majestuosos animales son conocidos por su tamaño imponente, sus orejas grandes y sus colmillos de marfil, que utilizan para diversas tareas como cavar en busca de agua, pelar corteza de los árboles y defenderse de depredadores. Los elefantes africanos habitan en una variedad de ecosistemas, desde sabanas y bosques hasta desiertos, y son fundamentales para el equilibrio ecológico de su entorno.</p>'
    mensaje += '<p>Su característica más distintiva son sus enormes orejas, que le ayudan a regular la temperatura corporal, y su trompa, una prolongación de la nariz y el labio superior, con la que puede respirar, alimentarse, comunicarse y manipular objetos.Estos animales habitan en las sabanas y bosques de África, donde se alimentan principalmente de hierbas, frutas, cortezas y hojas. Son animales muy sociales e inteligentes, que viven en grupos familiares dirigidos por una hembra mayor llamada matriarca. Tienen una memoria excepcional, capaz de recordar rutas de agua o lugares visitados años atrás.</p>'
    mensaje += '<p>El elefante africano cumple un papel esencial en su ecosistema: al derribar árboles y abrir caminos, ayuda a mantener el equilibrio de la sabana. Sin embargo, su supervivencia se ve amenazada por la caza furtiva y la pérdida de hábitat. Su fuerza, sabiduría y nobleza lo han convertido en un símbolo de respeto y poder en muchas culturas del mundo.</p>'
    mensaje += '<img src="static/elef.jpeg"  alt="Elefante Africano" width="300">'
    mensaje += '<h3>🐅 4. Tigre de Bengala</h3>'
    mensaje += '<p>El tigre de Bengala (Panthera tigris tigris) es una de las subespecies de tigre más emblemáticas y reconocidas en el mundo. Con su impresionante pelaje anaranjado adornado con rayas negras, este majestuoso felino es un símbolo de fuerza, poder y belleza en la naturaleza. Habita principalmente en India, Bangladesh, Nepal y Bután, donde se encuentra en una variedad de hábitats que incluyen bosques tropicales, manglares y praderas.</p>'
    mensaje += '<p>El tigre de Bengala es un depredador ápice, lo que significa que está en la cima de la cadena alimentaria. Su dieta se compone principalmente de grandes herbívoros como ciervos, jabalíes y búfalos. Son cazadores solitarios y territoriales, utilizando su aguda visión y sentido del olfato para rastrear a sus presas. A pesar de su tamaño y fuerza, los tigres son animales ágiles y sigilosos, capaces de moverse silenciosamente a través de su entorno para acechar a sus víctimas.</p>'
    mensaje += '<p>El tigre de Bengala juega un papel crucial en el mantenimiento del equilibrio ecológico de su hábitat, controlando las poblaciones de herbívoros y promoviendo la biodiversidad. Sin embargo, esta magnífica criatura enfrenta numerosas amenazas, incluyendo la pérdida de hábitat, la caza furtiva y el conflicto con los humanos. Afortunadamente, existen esfuerzos de conservación dedicados a proteger a los tigres de Bengala y su entorno natural, asegurando que futuras generaciones puedan seguir admirando a este símbolo icónico de la vida salvaje.</p>'
    mensaje += '<p>Es un cazador solitario y territorial que se alimenta de ciervos, búfalos, jabalíes y otros animales medianos. Se mueve sigilosamente y ataca con rapidez y precisión. Además de su fuerza, el tigre de Bengala destaca por su inteligencia y adaptabilidad, pudiendo sobrevivir tanto en la selva húmeda como en zonas montañosas. Actualmente está considerado una especie en peligro de extinción debido a la caza ilegal y la destrucción de su hábitat. Sin embargo, gracias a programas de conservación, su población comienza a recuperarse. El tigre representa la belleza salvaje y la fuerza de la naturaleza, y es un recordatorio del valor de proteger la vida silvestre.</p>'
    mensaje += '<img src="static/tig.jpeg"  alt="Tigre de Bengala" width="300">'
    mensaje += '<h3>🦜 5. Guacamayo rojo</h3>'
    mensaje += '<p>El guacamayo rojo (Ara macao) es una de las aves más coloridas y llamativas del mundo. Con su plumaje vibrante en tonos de rojo, azul y amarillo, esta especie de loro es un espectáculo visual que captura la atención de cualquiera que tenga la suerte de observarlo en su hábitat natural. Originario de las selvas tropicales de América Central y del Sur, el guacamayo rojo es conocido por su inteligencia, sociabilidad y habilidades vocales.</p>'
    mensaje += '<p>El guacamayo rojo es un ave grande, que puede medir hasta 90 centímetros de longitud, incluyendo su larga cola. Su dieta se compone principalmente de frutas, nueces, semillas y flores, y juega un papel importante en la dispersión de semillas en su ecosistema. Estos loros son muy sociales y suelen vivir en parejas o pequeños grupos, comunicándose entre sí mediante una variedad de sonidos fuertes y agudos. Además de su belleza y comportamiento fascinante, el guacamayo rojo enfrenta amenazas significativas debido a la pérdida de hábitat y el comercio ilegal de mascotas. Afortunadamente, existen esfuerzos de conservación dedicados a proteger a esta especie y su entorno natural, asegurando que las futuras generaciones puedan seguir disfrutando de la maravilla que representa el guacamayo rojo.Esta ave es muy inteligente y sociable. Vive en parejas o grupos y mantiene fuertes lazos con su compañero durante toda la vida. Su dieta se basa en frutas, semillas y nueces, que rompe fácilmente con su fuerte pico. Los guacamayos también ayudan a dispersar las semillas, favoreciendo el crecimiento de nuevos árboles en la selva.</p>'
    mensaje += '<p>El guacamayo rojo es un símbolo de la biodiversidad y la riqueza de las selvas tropicales. Sin embargo, su supervivencia está amenazada por la deforestación y el comercio ilegal de mascotas. Desafortunadamente, existen programas de conservación que trabajan para proteger a estas aves y su hábitat, asegurando que las futuras generaciones puedan seguir admirando la belleza y el encanto del guacamayo rojo.in embargo, enfrenta amenazas por la deforestación y el tráfico ilegal de aves exóticas. Gracias a su belleza, carisma e importancia ecológica, es considerado un tesoro natural que debemos proteger para mantener el equilibrio de los bosques tropicales.</p>'
    mensaje += '<img src="static/rojo.jpeg"  alt="Guacamayo Rojo" width="300">'
    mensaje += '<h3>🦅 6. Águila Real</h3>'
    mensaje += '<p>El águila real (Aquila chrysaetos) es una de las aves rapaces más majestuosas y poderosas del mundo. Con una envergadura que puede superar los dos metros, esta impresionante ave es conocida por su aguda visión, su vuelo elegante y su capacidad para cazar presas de considerable tamaño. Habita en una amplia variedad de ecosistemas, desde montañas y desiertos hasta bosques y praderas, y se encuentra en América del Norte, Europa, Asia y partes del norte de África.</p>'
    mensaje += '<p>El águila real es un depredador ápice, lo que significa que está en la cima de la cadena alimentaria. Su dieta incluye mamíferos medianos como conejos, liebres y marmotas, así como aves y reptiles. Utiliza su aguda visión para localizar a sus presas desde grandes alturas, y luego se lanza en picado con una velocidad impresionante para capturarlas con sus poderosas garras. Además de su destreza en la caza, el águila real es conocida por su longevidad y su fuerte vínculo con su pareja, con la que suele aparearse de por vida.</p>'
    mensaje += '<p>El águila real desempeña un papel crucial en el mantenimiento del equilibrio ecológico de su hábitat, controlando las poblaciones de sus presas y promoviendo la biodiversidad. A lo largo de la historia, esta ave ha sido un símbolo de poder, libertad y nobleza en muchas culturas alrededor del mundo. Sin embargo, enfrenta amenazas debido a la pérdida de hábitat, la caza furtiva y el envenenamiento. Afortunadamente, existen esfuerzos de conservación dedicados a proteger al águila real y su entorno natural, asegurando que futuras generaciones puedan seguir admirando a esta magnífica criatura en vuelo.</p>'
    mensaje += '<img src="static/agi.jpeg"  alt="Águila Real" width="300">'
    mensaje += '<h4> Hasta aqui llego esta seccion espero te haya gustado!!</h4>'
    return mensaje



@app.route('/carros')
def carros():
    mensaje = '<h1>Carros Exóticos</h1>'
    mensaje += '<h3>🏁 El nacimiento de los vehículos</h3>'
    mensaje += '<p>El origen de los vehículos se remonta al siglo XIX, cuando el ser humano buscaba nuevas formas de transporte más rápidas y cómodas que los carruajes tirados por caballos. El primer paso fue la invención del motor de combustión interna, que permitió transformar la energía del combustible en movimiento.</p>'
    mensaje += '<p>En 1886, el alemán Karl Benz construyó el primer automóvil de la historia, llamado Benz Patent-Motorwagen. Este vehículo tenía tres ruedas y funcionaba con gasolina. Poco después, inventores como Gottlieb Daimler y Henry Ford mejoraron el diseño, incorporando motores más potentes y sistemas de producción en masa, lo que hizo que los autos fueran más accesibles para la población.</p>'
    mensaje += '<p>A lo largo del siglo XX, los automóviles evolucionaron rápidamente, volviéndose más veloces, seguros y cómodos,los vehículos evolucionaron para incluir características como la dirección asistida, los frenos hidráulicos y la suspensión independiente, mejorando la seguridad y el confort. Hoy en día, los autos no solo son medios de transporte, sino también símbolos de estatus y estilo de vida, con diseños innovadores y tecnologías avanzadas como la electrificación y la conducción autónoma.</p>'
    mensaje += '<p>Surgieron marcas legendarias como Ford, Chevrolet, Mercedes-Benz, Volkswagen y Rolls-Royce, que dejaron una huella importante en la historia del transporte. Los vehículos antiguos no solo representan un medio de transporte, sino también una obra de ingeniería y arte que marcó el inicio de la modernidad.</p>'
    
    
    
    
    
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