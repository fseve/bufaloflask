import os
from flask import Flask, render_template
from forms.forms import *

app = Flask(__name__)
app.url_map.strict_slashes = False
app.secret_key = os.urandom(24)


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if (form.validate_on_submit()):
        correo = form.correo.data
        return f"Bienvenido{correo}"
    return render_template('login.html', form=form)

@app.route('/usuarios/crear', methods=['GET', 'POST'])
def crearUsuarios():
    form = CrearUsuarioForm()
    return render_template('crear-usuario.html', form=form)
