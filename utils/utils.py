from functools import wraps
from flask import redirect, session, request
from db import *

def validarLogin(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'id' not in session:
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated_function

def validarAutorizacion(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        idRol = int(session['idRol'])
        db = get_db()
        sql = f'SELECT om.descripcion, om.url, om.icono, om.mostrarMenu FROM opcionesMenu as om ' \
                + 'INNER JOIN roles as r ' \
                + 'ON om.idRol = r.id ' \
                + 'WHERE r.id = ?'
        cursorObj = db.cursor()

        cursorObj.execute(sql, [idRol])
        datos = cursorObj.fetchall()
        bandera = False
        url = request.path

        print('URL:'+url+':')

        if url != '/':
            datoUrl = url.split('/')
            print(datoUrl)
            if len(datoUrl) > 1 and len(datoUrl) < 2:
                url = '/' + datoUrl[1]
            elif len(datoUrl) > 2 and datoUrl[2] != '':
                url = '/' + datoUrl[1] + '/' + datoUrl[2]
            elif len(datoUrl) > 2:
                url = '/' + datoUrl[1]

        print(url)
        for item in datos:
            if (item[1] == url):
                bandera = True

        if bandera == False:
            session.clear()
            return redirect('/login')

        return f(*args, **kwargs)
    return decorated_function
