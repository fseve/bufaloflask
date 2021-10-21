from flask import render_template, Blueprint, jsonify, request, redirect, flash
from db import *
from forms.forms import DependenciasForm
from utils.utils import validarLogin, validarAutorizacion

dependencias_api = Blueprint('dependencias_api', __name__)
nombreTabla = 'dependencias'

@dependencias_api.route('/dependencias', methods=['GET'])
@dependencias_api.route('/dependencias/listar', methods=['GET'])
@validarLogin
@validarAutorizacion
def listarDependencias(mensaje = ''):
    return render_template('/dependencias/dependencias-listar.html', mensaje = mensaje)

@dependencias_api.route('/dependencias/obtener', methods=['GET'])
@validarLogin
@validarAutorizacion
def obtenerDependencias():
    try:
        db = get_db()
        sql = f'SELECT * FROM {nombreTabla}'
        cursorObj = db.cursor()
        cursorObj.execute(sql)
        datos = cursorObj.fetchall()

        dependencias = [{'id': x[0], 'descripcion': x[1]} for x in datos]

        return jsonify(
            dependencias
        )
    except Error:
        dependencias = []
        return jsonify(
            dependencias
        )

@dependencias_api.route('/dependencias/crear', methods=['GET', 'POST'])
@validarLogin
@validarAutorizacion
def crearDependencias():
    try:
        form = DependenciasForm()
        if (form.validate_on_submit() and request.method == 'POST'):
            descripcion = form.descripcion.data

            sql = f'INSERT INTO {nombreTabla} (descripcion) VALUES (?)'

            db = get_db()
            db.execute(sql, [descripcion])
            db.commit()

            flash('Registro creado correctamente')
            return redirect('/dependencias/listar')
        return render_template('dependencias/dependencias-crear.html', form=form)
    except Error:
        return redirect('/dependencias/listar')

@dependencias_api.route('/dependencias/editar/<int:id>', methods=['GET', 'POST'])
@validarLogin
@validarAutorizacion
def editarDependencias(id):
    try:
        form = DependenciasForm()
        if (request.method == 'GET'):
            db = get_db()
            sql = f'SELECT * FROM {nombreTabla} WHERE id = ?'

            cursorObj = db.cursor()
            cursorObj.execute(sql, [id])
            datos = cursorObj.fetchall()

            if (len(datos) > 0):
                form.id.data = datos[0][0]
                form.descripcion.data = datos[0][1]
                return render_template('dependencias/dependencias-editar.html', form=form)
            else:
                return redirect('/dependencias/listar')
        elif (form.validate_on_submit() and request.method == 'POST'):
            descripcion = form.descripcion.data
            sql = f'UPDATE {nombreTabla} SET descripcion = ? WHERE id = ?'

            db = get_db()
            db.execute(sql, [descripcion, id])
            db.commit()
            flash('Registro actualizado correctamente')
            return redirect('/dependencias/listar')
    except Error:
        return redirect('/dependencias/listar')

@dependencias_api.route('/dependencias/eliminar', methods=['POST'])
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
