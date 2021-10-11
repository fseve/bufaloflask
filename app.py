import os
from flask import Flask, render_template
from forms.forms import *
import datetime as dt

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

@app.route('/usuarios/listar')
def listarUsuarios():
    return render_template('ver-listar-usuarios.html')

@app.route('/usuarios/editar', methods=['GET', 'POST'])
def editarUsuarios():
    form = EditarUsuarioForm()
    form.id.data = 183
    form.correo.data = 'johndoe@mail.com'
    form.nombres.data = 'John'
    form.apellidos.data = 'Doe'
    form.edad.data = 30
    form.genero.data = 'masculino'
    form.cargo.data = 'Gerente'
    form.fechaIngreso.data = dt.datetime(2021, 9, 20)
    form.tipoContrato.data = 'Contrato a término fijo'
    form.fechaTerminoContrato.data = dt.datetime(2021, 11, 30)
    form.dependencia.data = 'Talento Humano'
    form.salario.data = 1500000
    form.rol.data = 'usuarioFinal'
    return render_template('editar-usuario.html', form=form)
