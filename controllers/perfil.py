from flask import render_template, Blueprint, redirect, request, session
from database.db import get_db
import datetime as dt
from forms.forms import PerfilUsuarioForm
from utils.utils import validarLogin, validarAutorizacion

perfil_api = Blueprint('perfil_api', __name__)

@perfil_api.route('/usuarios/perfil', methods=['GET'])
@validarLogin
@validarAutorizacion
def perfilUsuario():
    try:
        form = PerfilUsuarioForm()
        if (request.method == 'GET'):
            id = int(session['id'])
            db = get_db()
            sql = f'SELECT u.id, u.correo, u.nombres, u.apellidos, u.edad, u.idGenero, g.descripcion as genero, u.idCargo, c.descripcion as cargo, ' \
                + 'u.fechaIngreso, u.idTipoContrato, tc.descripcion as tipoContrato, u.fechaTerminoContrato, u.idDependencia, d.descripcion as dependencia, ' \
                + 'u.salario, u.idRol, r.descripcion as rol, u.puntaje, u.comentarios FROM usuarios as u ' \
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
                form.puntaje.data = datos[0][18]
                form.comentarios.data = datos[0][19]
                return render_template('perfil/perfil-usuario.html', form=form)
            else:
                return redirect('/usuarios/listar')
        elif (request.method == 'POST'):
            return redirect('/usuarios/listar')
    except Exception:
        return redirect('/usuarios/listar')
