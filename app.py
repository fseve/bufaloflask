import os
from flask import Flask, render_template, request
from forms.forms import *
import datetime as dt

app = Flask(__name__)
app.url_map.strict_slashes = False
app.secret_key = os.urandom(24)


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if (form.validate_on_submit() and request.method == 'POST'):
        correo = form.correo.data
        password = form.password.data
        return f"Bienvenido: {correo}" + " Password: " + password
    return render_template('login.html', form=form)

@app.route('/usuarios/crear', methods=['GET', 'POST'])
def crearUsuarios():
    form = CrearUsuarioForm()
    if (form.validate_on_submit() and request.method == 'POST'):
        correo = form.correo.data
        password = form.password.data
        nombres = form.nombres.data
        apellidos = form.apellidos.data
        edad = form.edad.data
        genero = form.genero.data
        cargo = form.cargo.data
        fechaIngreso = form.fechaIngreso.data
        tipoContrato = form.tipoContrato.data
        fechaTerminoContrato = form.fechaTerminoContrato.data
        dependencia = form.dependencia.data
        salario = form.salario.data
        rol = form.rol.data
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

@app.route('/usuarios/ver', methods=['GET'])
def verUsuarios():
    form = VerUsuarioForm()
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
    return render_template('ver-usuario.html', form=form)

@app.route('/usuarios/retroalimentacion', methods=['GET', 'POST'])
def generarRetroalimentacion():
    form = GenerarRetroalimentacionUsuarioForm()
    form.id.data = 183
    form.correo.data = 'johndoe@mail.com'
    form.nombres.data = 'John'
    form.apellidos.data = 'Doe'
    form.puntaje.data = 85
    form.comentarios.data = 'Ha realizado un desempeño sobresaliente.'
    return render_template('generar-retroalimentacion-usuario.html', form=form)

@app.route('/usuarios/perfil', methods=['GET'])
def perfilUsuario():
    form = PerfilUsuarioForm()
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
    form.puntaje.data = 85
    form.comentarios.data = 'Ha realizado un desempeño sobresaliente.'
    return render_template('perfil-usuario.html', form=form)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
