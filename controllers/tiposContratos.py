from flask import render_template, Blueprint, jsonify, request, redirect, flash
from db import *
from forms.forms import TiposContratosForm
from utils.utils import validarLogin, validarAutorizacion

tiposContratos_api = Blueprint('tiposContratos_api', __name__)
nombreTabla = 'tiposContratos'

@tiposContratos_api.route('/tiposcontratos', methods=['GET'])
@tiposContratos_api.route('/tiposcontratos/listar', methods=['GET'])
@validarLogin
@validarAutorizacion
def listarTiposContratos():
    return render_template('/tiposcontratos/tiposcontratos-listar.html')

@tiposContratos_api.route('/tiposcontratos/obtener', methods=['GET'])
@validarLogin
@validarAutorizacion
def obtenerTiposContratos():
    try:
        db = get_db()
        sql = f'SELECT * FROM {nombreTabla}'
        cursorObj = db.cursor()
        cursorObj.execute(sql)
        datos = cursorObj.fetchall()

        tiposContratos = [{'id': x[0], 'descripcion': x[1]} for x in datos]

        return jsonify(
            tiposContratos
        )
    except Error:
        tiposContratos = []
        return jsonify(
            tiposContratos
        )

@tiposContratos_api.route('/tiposcontratos/crear', methods=['GET', 'POST'])
@validarLogin
@validarAutorizacion
def crearTiposContratos():
    try:
        form = TiposContratosForm()
        if (form.validate_on_submit() and request.method == 'POST'):
            descripcion = form.descripcion.data

            sql = f'INSERT INTO {nombreTabla} (descripcion) VALUES (?)'

            db = get_db()
            db.execute(sql, [descripcion])
            db.commit()

            flash('Registro creado correctamente')
            return redirect('/tiposcontratos/listar')
        return render_template('tiposcontratos/tiposcontratos-crear.html', form=form)
    except Error:
        return redirect('/tiposcontratos/listar')

@tiposContratos_api.route('/tiposcontratos/editar/<int:id>', methods=['GET', 'POST'])
@validarLogin
@validarAutorizacion
def editarTiposContratos(id):
    try:
        form = TiposContratosForm()
        if (request.method == 'GET'):
            db = get_db()
            sql = f'SELECT * FROM {nombreTabla} WHERE id = ?'

            cursorObj = db.cursor()
            cursorObj.execute(sql, [id])
            datos = cursorObj.fetchall()

            if (len(datos) > 0):
                form.id.data = datos[0][0]
                form.descripcion.data = datos[0][1]
                return render_template('tiposcontratos/tiposcontratos-editar.html', form=form)
            else:
                return redirect('/tiposcontratos/listar')
        elif (form.validate_on_submit() and request.method == 'POST'):
            descripcion = form.descripcion.data
            sql = f'UPDATE {nombreTabla} SET descripcion = ? WHERE id = ?'

            db = get_db()
            db.execute(sql, [descripcion, id])
            db.commit()
            flash('Registro actualizado correctamente')
            return redirect('/tiposcontratos/listar')
    except Error:
        return redirect('/tiposcontratos/listar')

@tiposContratos_api.route('/tiposcontratos/eliminar', methods=['POST'])
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
    except Error:
        return 'False'
