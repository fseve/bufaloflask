from flask import render_template, Blueprint, request, redirect, flash, session, jsonify
from werkzeug.security import check_password_hash
from database.db import get_db
from forms.forms import LoginForm
from utils.utils import validarLogin, validarAutorizacion

login_api = Blueprint('login_api', __name__)
nombreTabla = 'usuarios'

@login_api.route('/login', methods=['GET', 'POST'])
def login():
    try:
        if 'id' not in session:
            form = LoginForm()
            if (form.validate_on_submit() and request.method == 'POST'):
                correo = form.correo.data
                password = form.password.data

                db = get_db()
                sql = f'SELECT u.id, u.correo, u.password, u.nombres, u.apellidos, u.idRol, r.descripcion, r.urlInicio as rol FROM usuarios as u ' \
                        + 'INNER JOIN roles as r ' \
                        + 'on r.id = u.idRol ' \
                        + 'WHERE correo = ?'

                cursorObj = db.cursor()
                cursorObj.execute(sql, [correo])
                datos = cursorObj.fetchall()

                if len(datos) > 0:
                    passwordHash = datos[0][2]
                    if check_password_hash(passwordHash, password):
                        session.clear()
                        session['id'] = datos[0][0]
                        session['correo'] = datos[0][1]
                        session['nombres'] = datos[0][3]
                        session['apellidos'] = datos[0][4]
                        session['idRol'] = datos[0][5]
                        session['rol'] = datos[0][6]
                        return redirect(datos[0][7])
                    else:
                        session.clear()
                        flash('Correo electrónico o contraseña incorrectos')
                        return redirect('/login')
                else:
                        session.clear()
                        flash('Correo electrónico o contraseña incorrectos')
                        return redirect('/login')
            return render_template('login/login.html', form=form)
        else:
            return redirect('/')
    except Error:
        session.clear()
        return redirect('/login')

@login_api.route('/logout', methods=['GET'])
@validarLogin
@validarAutorizacion
def logout():
    session.clear()
    return redirect('/login')

@login_api.route('/menu', methods=['GET'])
@validarLogin
@validarAutorizacion
def obtenerOpcionesMenu():
    try:
        idRol = int(session['idRol'])
        db = get_db()
        sql = f'SELECT om.descripcion, om.url, om.icono, om.mostrarMenu FROM opcionesMenu as om ' \
                + 'INNER JOIN roles as r ' \
                + 'ON om.idRol = r.id ' \
                + 'WHERE r.id = ?'
        cursorObj = db.cursor()

        cursorObj.execute(sql, [idRol])
        datos = cursorObj.fetchall()

        opcionesMenu = [
            {
                'descripcion': x[0],
                'url': x[1],
                'icono': x[2],
                'mostrarMenu': x[3]
            }
            for x in datos
        ]

        return jsonify(
            opcionesMenu
        )
    except Error:
        opcionesMenu = []
        return jsonify(
            opcionesMenu
        )
