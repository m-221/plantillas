
@app.route('/formulario', methods=("GET", "POST"))
def registro():
    error = None
    if request.method == "POST":
        nombrecompleto = request.form["nombre"]
        emailHelp = request.form["exampleInputEmail1"]
        password =request.form ["exampleInputPassword1"]
        fecha = request.form ["dia"]
        fecha = request.form ["mes"]
        fecha = request.form ["año"]
        genero = request.form ["hombre"]
        genero = request.form ["mujer"]
        genero = request.form ["personalizado"]

        if password != request.form["exampleInputPassword2"]:
            error = "lacontraseña no coincide"
        if error != None:
            flash(error)
            return render_template('formulario.html')
        else:
            (f"!registro exitoso! : {nombrecompleto}!")
            return render_template('formulario.html')