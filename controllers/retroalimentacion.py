from flask import render_template, Blueprint, request, redirect, flash
from database.db import get_db
from forms.forms import GenerarRetroalimentacionUsuarioForm
from utils.utils import validarLogin, validarAutorizacion

retroalimentacion_api = Blueprint('retroalimentacion_api', __name__)
nombreTabla = 'usuarios'

@retroalimentacion_api.route('/usuarios/retroalimentacion/<int:id>', methods=['GET', 'POST'])
@validarLogin
@validarAutorizacion
def generarRetroalimentacion(id):
    try:
        form = GenerarRetroalimentacionUsuarioForm()
        if (request.method == 'GET'):

            db = get_db()
            sql = f'SELECT u.id, u.correo, u.nombres, u.apellidos, u.puntaje, u.comentarios ' \
                + 'FROM usuarios as u ' \
                + 'WHERE u.id = ?'

            cursorObj = db.cursor()
            cursorObj.execute(sql, [id])
            datos = cursorObj.fetchall()

            if (len(datos) > 0):
                form.id.data = datos[0][0]
                form.correo.data = datos[0][1]
                form.nombres.data = datos[0][2]
                form.apellidos.data = datos[0][3]
                form.puntaje.data = datos[0][4]
                form.comentarios.data = datos[0][5]
                return render_template('retroalimentacion/generar-retroalimentacion-usuario.html', form=form)
            else:
                return redirect('/usuarios/listar')
        elif (form.validate_on_submit() and request.method == 'POST'):
            id = form.id.data
            puntaje = form.puntaje.data
            comentarios = form.comentarios.data

            sql = f'UPDATE {nombreTabla} SET puntaje = ?, comentarios = ? ' \
                + 'WHERE id = ?'

            db = get_db()
            db.execute(sql, (puntaje, comentarios, id))
            db.commit()
            flash('Retroalimentación almacenada correctamente')
            return redirect('/usuarios/listar')
    except Error:
        return redirect('/usuarios/listar')
