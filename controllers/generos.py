from flask import render_template, Blueprint, jsonify, request, redirect, flash
from db import *
from forms.forms import GenerosForm
from utils.utils import validarLogin, validarAutorizacion

generos_api = Blueprint('generos_api', __name__)
nombreTabla = 'generos'

@generos_api.route('/generos', methods=['GET'])
@generos_api.route('/generos/listar', methods=['GET'])
@validarLogin
@validarAutorizacion
def listarGeneros():
    return render_template('/generos/generos-listar.html')

@generos_api.route('/generos/obtener', methods=['GET'])
@validarLogin
@validarAutorizacion
def obtenerGeneros():
    try:
        db = get_db()
        sql = f'SELECT * FROM {nombreTabla}'
        cursorObj = db.cursor()
        cursorObj.execute(sql)
        datos = cursorObj.fetchall()

        generos = [{'id': x[0], 'descripcion': x[1]} for x in datos]

        return jsonify(
            generos
        )
    except Error:
        generos = []
        return jsonify(
            generos
        )

@generos_api.route('/generos/crear', methods=['GET', 'POST'])
@validarLogin
@validarAutorizacion
def crearGeneros():
    try:
        form = GenerosForm()
        if (form.validate_on_submit() and request.method == 'POST'):
            descripcion = form.descripcion.data

            sql = f'INSERT INTO {nombreTabla} (descripcion) VALUES (?)'

            db = get_db()
            db.execute(sql, [descripcion])
            db.commit()

            flash('Registro creado correctamente')
            return redirect('/generos/listar')
        return render_template('generos/generos-crear.html', form=form)
    except Error:
        return redirect('/generos/listar')

@generos_api.route('/generos/editar/<int:id>', methods=['GET', 'POST'])
@validarLogin
@validarAutorizacion
def editarGeneros(id):
    try:
        form = GenerosForm()
        if (request.method == 'GET'):
            db = get_db()
            sql = f'SELECT * FROM {nombreTabla} WHERE id = ?'

            cursorObj = db.cursor()
            cursorObj.execute(sql, [id])
            datos = cursorObj.fetchall()

            if (len(datos) > 0):
                form.id.data = datos[0][0]
                form.descripcion.data = datos[0][1]
                return render_template('generos/generos-editar.html', form=form)
            else:
                return redirect('/generos/listar')
        elif (form.validate_on_submit() and request.method == 'POST'):
            descripcion = form.descripcion.data
            sql = f'UPDATE {nombreTabla} SET descripcion = ? WHERE id = ?'

            db = get_db()
            db.execute(sql, [descripcion, id])
            db.commit()
            flash('Registro actualizado correctamente')
            return redirect('/generos/listar')
    except Error:
        return redirect('/generos/listar')

@generos_api.route('/generos/eliminar', methods=['POST'])
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
