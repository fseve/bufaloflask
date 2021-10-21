from flask import render_template, Blueprint, jsonify, request, redirect, flash
from db import *
from forms.forms import CargosForm
from utils.utils import validarLogin, validarAutorizacion

cargos_api = Blueprint('cargos_api', __name__)
nombreTabla = 'cargos'

@cargos_api.route('/cargos', methods=['GET'])
@cargos_api.route('/cargos/listar', methods=['GET'])
@validarLogin
@validarAutorizacion
def listarCargos():
    return render_template('/cargos/cargos-listar.html')

@cargos_api.route('/cargos/obtener', methods=['GET'])
@validarLogin
@validarAutorizacion
def obtenerCargos():
    try:
        db = get_db()
        sql = f'SELECT * FROM {nombreTabla}'
        cursorObj = db.cursor()
        cursorObj.execute(sql)
        datos = cursorObj.fetchall()

        cargos = [{'id': x[0], 'descripcion': x[1]} for x in datos]

        return jsonify(
            cargos
        )
    except Error:
        cargos = []
        return jsonify(
            cargos
        )

@cargos_api.route('/cargos/crear', methods=['GET', 'POST'])
@validarLogin
@validarAutorizacion
def crearCargos():
    try:
        form = CargosForm()
        if (form.validate_on_submit() and request.method == 'POST'):
            descripcion = form.descripcion.data

            sql = f'INSERT INTO {nombreTabla} (descripcion) VALUES (?)'

            db = get_db()
            db.execute(sql, [descripcion])
            db.commit()

            flash('Registro creado correctamente')
            return redirect('/cargos/listar')
        return render_template('cargos/cargos-crear.html', form=form)
    except Error:
        return redirect('/cargos/listar')

@cargos_api.route('/cargos/editar/<int:id>', methods=['GET', 'POST'])
@validarLogin
@validarAutorizacion
def editarCargos(id):
    try:
        form = CargosForm()
        if (request.method == 'GET'):
            db = get_db()
            sql = f'SELECT * FROM {nombreTabla} WHERE id = ?'

            cursorObj = db.cursor()
            cursorObj.execute(sql, [id])
            datos = cursorObj.fetchall()

            if (len(datos) > 0):
                form.id.data = datos[0][0]
                form.descripcion.data = datos[0][1]
                return render_template('cargos/cargos-editar.html', form=form)
            else:
                return redirect('/cargos/listar')
        elif (form.validate_on_submit() and request.method == 'POST'):
            descripcion = form.descripcion.data
            sql = f'UPDATE {nombreTabla} SET descripcion = ? WHERE id = ?'

            db = get_db()
            db.execute(sql, [descripcion, id])
            db.commit()
            flash('Registro actualizado correctamente')
            return redirect('/cargos/listar')
    except Error:
        return redirect('/cargos/listar')

@cargos_api.route('/cargos/eliminar', methods=['POST'])
@validarLogin
@validarAutorizacion
def eliminarCargos():
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
