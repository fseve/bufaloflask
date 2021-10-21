from flask import render_template, Blueprint, redirect, request
from database.db import get_db
from utils.utils import validarLogin, validarAutorizacion

dashboard_api = Blueprint('dashboard_api', __name__)
nombreTabla = 'usuarios'

@dashboard_api.route('/', methods=['GET'])
@dashboard_api.route('/dashboard', methods=['GET'])
@validarLogin
@validarAutorizacion
def dashboard():
    try:

        if (request.method == 'GET'):
            db = get_db()

            sql = f'SELECT count(id) as cantidad from usuarios'
            cursorObj = db.cursor()
            cursorObj.execute(sql)
            datos = cursorObj.fetchall()

            cantidad = 0
            if (len(datos) > 0):
                cantidad = datos[0][0]

            sql = f'SELECT max(puntaje) as maxpuntaje from usuarios'
            cursorObj = db.cursor()
            cursorObj.execute(sql)
            datos = cursorObj.fetchall()

            maxPuntaje = 0
            if (len(datos) > 0):
                maxPuntaje = datos[0][0]

            sql = f'SELECT min(puntaje) as maxpuntaje from usuarios'
            cursorObj = db.cursor()
            cursorObj.execute(sql)
            datos = cursorObj.fetchall()

            minPuntaje = 0
            if (len(datos) > 0):
                minPuntaje = datos[0][0]

            return render_template('dashboard/dashboard.html', cantidad=cantidad, maxPuntaje=maxPuntaje, minPuntaje=minPuntaje)

        elif (request.method == 'POST'):
            return redirect('/')

    except Exception:
        return redirect('/')
