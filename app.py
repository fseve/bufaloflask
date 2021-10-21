import os
from flask import Flask

from controllers.generos import generos_api
from controllers.cargos import cargos_api
from controllers.tiposContratos import tiposContratos_api
from controllers.dependencias import dependencias_api
from controllers.usuarios import usuarios_api
from controllers.login import login_api
from controllers.retroalimentacion import retroalimentacion_api
from controllers.dashboard import dashboard_api
from controllers.perfil import perfil_api

app = Flask(__name__)
app.url_map.strict_slashes = False
app.secret_key = os.urandom(24)

app.register_blueprint(generos_api)
app.register_blueprint(cargos_api)
app.register_blueprint(tiposContratos_api)
app.register_blueprint(dependencias_api)
app.register_blueprint(usuarios_api)
app.register_blueprint(login_api)
app.register_blueprint(retroalimentacion_api)
app.register_blueprint(dashboard_api)
app.register_blueprint(perfil_api)
