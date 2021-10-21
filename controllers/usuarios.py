from flask import render_template, Blueprint, jsonify, request, redirect, flash, session
from werkzeug.security import generate_password_hash
from database.db import get_db
import datetime as dt
from forms.forms import CrearUsuarioForm, EditarUsuarioForm, VerUsuarioForm
from utils.utils import validarLogin, validarAutorizacion

usuarios_api = Blueprint('usuarios_api', __name__)
nombreTabla = 'usuarios'

@usuarios_api.route('/usuarios', methods=['GET'])
@usuarios_api.route('/usuarios/listar', methods=['GET'])
@validarLogin
@validarAutorizacion
def listarUsuarios():
    return render_template('/usuarios/ver-listar-usuarios.html')

@usuarios_api.route('/usuarios/obtener', methods=['GET'])
@validarLogin
@validarAutorizacion
def obtenerUsuarios():
    try:
        db = get_db()
        sql = f'SELECT u.id, u.correo, u.nombres, u.apellidos, u.edad, u.idGenero, g.descripcion as genero, u.idCargo, c.descripcion as cargo, ' \
            + 'u.fechaIngreso, u.idTipoContrato, tc.descripcion as tipoContrato, u.fechaTerminoContrato, u.idDependencia, d.descripcion as dependencia, ' \
            + 'u.salario, u.idRol, r.descripcion as rol FROM usuarios as u ' \
            + 'INNER JOIN cargos as c ' \
            + 'on c.id = u.idCargo ' \
            + 'INNER JOIN dependencias as d ' \
            + 'on d.id = u.idDependencia ' \
            + 'INNER JOIN generos as g ' \
            + 'on g.id = u.idGenero ' \
            + 'INNER JOIN tiposContratos as tc ' \
            + 'on tc.id = u.idTipoContrato ' \
            + 'INNER JOIN roles as r ' \
            + 'on r.id = u.idRol '

        cursorObj = db.cursor()
        cursorObj.execute(sql)
        datos = cursorObj.fetchall()

        usuarios = [
            {
                'id': x[0],
                'correo': x[1],
                'nombres': x[2],
                'apellidos': x[3],
                'edad': x[4],
                'genero': x[6],
                'cargo': x[8],
                'fechaIngreso': x[9],
                'tipoContrato': x[11],
                'fechaTerminoContrato': x[12],
                'dependencia': x[14],
                'salario': x[15],
                'rol': x[17]
            }
            for x in datos
        ]

        return jsonify(
            usuarios
        )
    except Exception:
        usuarios = []
        return jsonify(
            usuarios
        )

@usuarios_api.route('/usuarios/ver/<int:id>', methods=['GET'])
@validarLogin
@validarAutorizacion
def verUsuarios(id):
    try:
        form = VerUsuarioForm()
        if (request.method == 'GET'):
            db = get_db()
            sql = f'SELECT u.id, u.correo, u.nombres, u.apellidos, u.edad, u.idGenero, g.descripcion as genero, u.idCargo, c.descripcion as cargo, ' \
                + 'u.fechaIngreso, u.idTipoContrato, tc.descripcion as tipoContrato, u.fechaTerminoContrato, u.idDependencia, d.descripcion as dependencia, ' \
                + 'u.salario, u.idRol, r.descripcion as rol FROM usuarios as u ' \
                + 'INNER JOIN cargos as c ' \
                + 'on c.id = u.idCargo ' \
                + 'INNER JOIN dependencias as d ' \
                + 'on d.id = u.idDependencia ' \
                + 'INNER JOIN generos as g ' \
                + 'on g.id = u.idGenero ' \
                + 'INNER JOIN tiposContratos as tc ' \
                + 'on tc.id = u.idTipoContrato ' \
                + 'INNER JOIN roles as r ' \
                + 'on r.id = u.idRol ' \
                + 'WHERE u.id = ?'

            cursorObj = db.cursor()
            cursorObj.execute(sql, [id])
            datos = cursorObj.fetchall()

            if (len(datos) > 0):
                form.id.data = datos[0][0]
                form.correo.data = datos[0][1]
                form.nombres.data = datos[0][2]
                form.apellidos.data = datos[0][3]
                form.edad.data = datos[0][4]
                form.genero.data = datos[0][6]
                form.cargo.data = datos[0][8]
                fechaIngreso = datos[0][9].split('-')
                form.fechaIngreso.data = dt.datetime(int(fechaIngreso[0]), int(fechaIngreso[1]), int(fechaIngreso[2]))
                form.tipoContrato.data = datos[0][11]
                fechaTerminoContrato = datos[0][12].split('-')
                form.fechaTerminoContrato.data = dt.datetime(int(fechaTerminoContrato[0]), int(fechaTerminoContrato[1]), int(fechaTerminoContrato[2]))
                form.dependencia.data = datos[0][14]
                form.salario.data = int(datos[0][15])
                form.rol.data = datos[0][17]
                return render_template('usuarios/ver-usuario.html', form=form)
            else:
                return redirect('/usuarios/listar')
        elif (request.method == 'POST'):
            return redirect('/usuarios/listar')
    except Exception:
        return redirect('/usuarios/listar')

@usuarios_api.route('/usuarios/crear', methods=['GET', 'POST'])
@validarLogin
@validarAutorizacion
def crearUsuarios():
    try:
        form = CrearUsuarioForm()
        generos = obtenerDatosSelectField('generos')
        form.genero.choices = [(x[0], x[1]) for x in generos]

        cargos = obtenerDatosSelectField('cargos')
        form.cargo.choices = [(x[0], x[1]) for x in cargos]

        tiposcontratos = obtenerDatosSelectField('tiposContratos')
        form.tipoContrato.choices = [(x[0], x[1]) for x in tiposcontratos]

        dependencias = obtenerDatosSelectField('dependencias')
        form.dependencia.choices = [(x[0], x[1]) for x in dependencias]

        roles = obtenerRoles()

        form.rol.choices = [(x[0], x[1]) for x in roles]

        if (form.validate_on_submit() and request.method == 'POST'):
            correo = form.correo.data
            password = generate_password_hash(form.password.data)
            nombres = form.nombres.data
            apellidos = form.apellidos.data
            edad = int(form.edad.data)
            genero = int(form.genero.data)
            cargo = int(form.cargo.data)
            fechaIngreso = form.fechaIngreso.data
            tipoContrato = int(form.tipoContrato.data)
            fechaTerminoContrato = form.fechaTerminoContrato.data
            dependencia = int(form.dependencia.data)
            salario = form.salario.data
            rol = int(form.rol.data)

            sql = f'SELECT id, correo FROM {nombreTabla} WHERE correo = ?'

            db = get_db()
            cursorObj = db.cursor()
            cursorObj.execute(sql, [correo])
            datos = cursorObj.fetchall()

            if (len(datos) > 0):
                flash(f'El correo electrónico {datos[0][1]} ya existe en la base de datos')
                return render_template('/usuarios/crear-usuario.html', form=form)

            sql = 'INSERT INTO usuarios (correo, password, nombres, apellidos, edad, idGenero, idCargo, fechaIngreso, idTipoContrato, fechaTerminoContrato, idDependencia, salario, idRol) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'

            db = get_db()
            db.execute(sql, (correo, password, nombres, apellidos, edad, genero, cargo, fechaIngreso, tipoContrato, fechaTerminoContrato, dependencia, salario, rol))
            db.commit()

            flash('Registro creado correctamente')
            return redirect('/usuarios/listar')

        return render_template('/usuarios/crear-usuario.html', form=form)
    except Exception:
        return redirect('/usuarios/listar')

@usuarios_api.route('/usuarios/editar/<int:id>', methods=['GET', 'POST'])
@validarLogin
@validarAutorizacion
def editarUsuarios(id):
    try:
        form = EditarUsuarioForm()
        if (request.method == 'GET'):
            db = get_db()
            sql = f'SELECT u.id, u.correo, u.nombres, u.apellidos, u.edad, u.idGenero, g.descripcion as genero, u.idCargo, c.descripcion as cargo, ' \
                + 'u.fechaIngreso, u.idTipoContrato, tc.descripcion as tipoContrato, u.fechaTerminoContrato, u.idDependencia, d.descripcion as dependencia, ' \
                + 'u.salario, u.idRol, r.descripcion as rol FROM usuarios as u ' \
                + 'INNER JOIN cargos as c ' \
                + 'on c.id = u.idCargo ' \
                + 'INNER JOIN dependencias as d ' \
                + 'on d.id = u.idDependencia ' \
                + 'INNER JOIN generos as g ' \
                + 'on g.id = u.idGenero ' \
                + 'INNER JOIN tiposContratos as tc ' \
                + 'on tc.id = u.idTipoContrato ' \
                + 'INNER JOIN roles as r ' \
                + 'on r.id = u.idRol ' \
                + 'WHERE u.id = ?'

            cursorObj = db.cursor()
            cursorObj.execute(sql, [id])
            datos = cursorObj.fetchall()

            if (len(datos) > 0):
                form.id.data = datos[0][0]
                form.correo.data = datos[0][1]
                form.nombres.data = datos[0][2]
                form.apellidos.data = datos[0][3]
                form.edad.data = datos[0][4]

                generos = obtenerDatosSelectField('generos')
                form.genero.choices = [(x[0], x[1]) for x in generos]
                form.genero.data = str(datos[0][5])

                cargos = obtenerDatosSelectField('cargos')
                form.cargo.choices = [(x[0], x[1]) for x in cargos]
                form.cargo.data = str(datos[0][7])

                fechaIngreso = datos[0][9].split('-')
                form.fechaIngreso.data = dt.datetime(int(fechaIngreso[0]), int(fechaIngreso[1]), int(fechaIngreso[2]))

                tiposcontratos = obtenerDatosSelectField('tiposContratos')
                form.tipoContrato.choices = [(x[0], x[1]) for x in tiposcontratos]
                form.tipoContrato.data = str(datos[0][10])

                fechaTerminoContrato = datos[0][12].split('-')
                form.fechaTerminoContrato.data = dt.datetime(int(fechaTerminoContrato[0]), int(fechaTerminoContrato[1]), int(fechaTerminoContrato[2]))

                dependencias = obtenerDatosSelectField('dependencias')
                form.dependencia.choices = [(x[0], x[1]) for x in dependencias]
                form.dependencia.data = str(datos[0][13])

                form.salario.data = int(datos[0][15])

                roles = obtenerRoles()
                form.rol.choices = [(x[0], x[1]) for x in roles]
                form.rol.data = str(datos[0][16])
                return render_template('usuarios/editar-usuario.html', form=form)
            else:
                return redirect('/usuarios/listar')
        elif (form.validate_on_submit() and request.method == 'POST'):
            correo = form.correo.data
            nombres = form.nombres.data
            apellidos = form.apellidos.data
            edad = int(form.edad.data)
            genero = int(form.genero.data)
            cargo = int(form.cargo.data)
            fechaIngreso = form.fechaIngreso.data
            tipoContrato = int(form.tipoContrato.data)
            fechaTerminoContrato = form.fechaTerminoContrato.data
            dependencia = int(form.dependencia.data)
            salario = form.salario.data
            rol = int(form.rol.data)

            sql = f'SELECT id, correo FROM {nombreTabla} WHERE correo = ?'

            db = get_db()
            cursorObj = db.cursor()
            cursorObj.execute(sql, [correo])
            datos = cursorObj.fetchall()

            if (len(datos) > 0):
                if (int(datos[0][0]) != int(id)):
                    flash(f'El correo electrónico {datos[0][1]} ya existe en la base de datos')
                    return redirect(f'/usuarios/editar/{id}')

            sql = f'UPDATE {nombreTabla} SET correo = ?, nombres = ?, apellidos = ?, ' \
                + 'edad = ?, idGenero = ?, idCargo = ?, fechaIngreso = ?, ' \
                + 'idTipoContrato = ?, fechaTerminoContrato = ?, idDependencia = ?, salario = ?, idRol = ? ' \
                + 'WHERE id = ?'

            db = get_db()
            db.execute(sql, (correo, nombres, apellidos, edad, genero, cargo, fechaIngreso, tipoContrato, fechaTerminoContrato, dependencia, salario, rol, id))
            db.commit()
            flash('Registro actualizado correctamente')
            return redirect('/usuarios/listar')
        else:
            return redirect('/usuarios/listar')
    except Exception:
        return redirect('/usuarios/listar')

@usuarios_api.route('/usuarios/eliminar', methods=['POST'])
@validarLogin
@validarAutorizacion
def eliminarUsuarios():
    try:
        id = request.form['id']
        sql = f'DELETE FROM {nombreTabla} WHERE id = ?'
        db = get_db()
        result = db.execute(sql, [id]).rowcount
        db.commit()
        if result > 0:
            return 'True'
        return 'False'
    except Exception:
        return 'False'

def obtenerDatosSelectField(nombreTabla = ''):
    try:
        db = get_db()
        sql = f'SELECT * FROM {nombreTabla}'
        cursorObj = db.cursor()
        cursorObj.execute(sql)
        datos = cursorObj.fetchall()

        return datos
    except Exception:
        datos = []
        return datos

def obtenerRoles():
    try:

        idRol = int(session['idRol'])

        sql = ''
        if idRol == 3:
            sql = f'SELECT * FROM roles'
        elif idRol == 2:
            sql = f'SELECT * FROM roles WHERE id != 3'

        db = get_db()
        cursorObj = db.cursor()
        cursorObj.execute(sql)
        datos = cursorObj.fetchall()

        return datos
    except Exception:
        datos = []
        return datos
