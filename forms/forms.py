from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SelectField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField, DateField
from wtforms.widgets.core import TextArea
from wtforms.widgets.html5 import NumberInput

class LoginForm(FlaskForm):
	correo = EmailField('Correo electrónico', validators=[DataRequired(message="Este campo es requerido")])
	password = PasswordField('Contraseña', validators=[DataRequired(message="Este campo es requerido")])

class CrearUsuarioForm(FlaskForm):
	correo = EmailField('Correo electrónico', validators=[DataRequired(message="Este campo es requerido")])
	password = PasswordField('Contraseña', validators=[DataRequired(message="Este campo es requerido")])
	nombres = StringField('Nombres', validators=[DataRequired(message="Este campo es requerido")])
	apellidos = StringField('Apellidos', validators=[DataRequired(message="Este campo es requerido")])
	edad = IntegerField('Edad', widget=NumberInput(min=18, max=200, step=1), validators=[DataRequired(message="Este campo es requerido")])
	genero = SelectField('Género', validate_choice=False, choices = [], validators=[DataRequired(message="Este campo es requerido")])
	cargo = SelectField('Cargo', validate_choice=False, choices = [], validators=[DataRequired(message="Este campo es requerido")])
	fechaIngreso = DateField('Fecha de ingreso', validators=[DataRequired(message="Este campo es requerido")])
	tipoContrato = SelectField('Tipo de contrato', validate_choice=False, choices = [], validators=[DataRequired(message="Este campo es requerido")])
	fechaTerminoContrato = DateField('Fecha término contrato', validators=[DataRequired(message="Este campo es requerido")])
	dependencia = SelectField('Dependencia', validate_choice=False, choices = [], validators=[DataRequired(message="Este campo es requerido")])
	salario = IntegerField('Salario', widget=NumberInput(min=0, step=1), validators=[DataRequired(message="Este campo es requerido")])
	rol = SelectField('Rol', validate_choice=False, choices = [], validators=[DataRequired(message="Este campo es requerido")])

class EditarUsuarioForm(FlaskForm):
	id = StringField('ID', render_kw={'readonly': True}, validators=[DataRequired(message="Este campo es requerido")])
	correo = EmailField('Correo electrónico', validators=[DataRequired(message="Este campo es requerido")])
	nombres = StringField('Nombres', validators=[DataRequired(message="Este campo es requerido")])
	apellidos = StringField('Apellidos', validators=[DataRequired(message="Este campo es requerido")])
	edad = IntegerField('Edad', widget=NumberInput(min=18, max=200, step=1), validators=[DataRequired(message="Este campo es requerido")])
	genero = SelectField('Género', validate_choice=False, choices = [], validators=[DataRequired(message="Este campo es requerido")])
	cargo = SelectField('Cargo', validate_choice=False, choices = [], validators=[DataRequired(message="Este campo es requerido")])
	fechaIngreso = DateField('Fecha de ingreso', validators=[DataRequired(message="Este campo es requerido")])
	tipoContrato = SelectField('Tipo de contrato', validate_choice=False, choices = [], validators=[DataRequired(message="Este campo es requerido")])
	fechaTerminoContrato = DateField('Fecha término contrato', validators=[DataRequired(message="Este campo es requerido")])
	dependencia = SelectField('Dependencia', validate_choice=False, choices = [], validators=[DataRequired(message="Este campo es requerido")])
	salario = IntegerField('Salario', widget=NumberInput(min=0, step=1), validators=[DataRequired(message="Este campo es requerido")])
	rol = SelectField('Rol', validate_choice=False, choices = [], validators=[DataRequired(message="Este campo es requerido")])

class VerUsuarioForm(FlaskForm):
	id = StringField('ID', render_kw={'readonly': True})
	correo = EmailField('Correo electrónico', render_kw={'readonly': True})
	nombres = StringField('Nombres', render_kw={'readonly': True})
	apellidos = StringField('Apellidos', render_kw={'readonly': True})
	edad = IntegerField('Edad', render_kw={'readonly': True})
	genero = StringField('Género', render_kw={'readonly': True})
	cargo = StringField('Cargo', render_kw={'readonly': True})
	fechaIngreso = DateField('Fecha de ingreso', render_kw={'readonly': True})
	tipoContrato = StringField('Tipo de contrato', render_kw={'readonly': True})
	fechaTerminoContrato = DateField('Fecha término contrato', render_kw={'readonly': True})
	dependencia = StringField('Dependencia', render_kw={'readonly': True})
	salario = IntegerField('Salario', render_kw={'readonly': True})
	rol = StringField('Rol', render_kw={'readonly': True})

class GenerarRetroalimentacionUsuarioForm(FlaskForm):
	id = StringField('ID', render_kw={'readonly': True}, validators=[DataRequired(message="Este campo es requerido")])
	correo = EmailField('Correo electrónico', render_kw={'readonly': True}, validators=[DataRequired(message="Este campo es requerido")])
	nombres = StringField('Nombres', render_kw={'readonly': True}, validators=[DataRequired(message="Este campo es requerido")])
	apellidos = StringField('Apellidos', render_kw={'readonly': True}, validators=[DataRequired(message="Este campo es requerido")])
	puntaje = IntegerField('Puntaje', widget=NumberInput(min=0, max=100, step=1), validators=[DataRequired(message="Este campo es requerido")])
	comentarios = StringField('Comentarios', widget=TextArea(), validators=[DataRequired(message="Este campo es requerido")])

class PerfilUsuarioForm(FlaskForm):
	id = StringField('ID', render_kw={'readonly': True})
	correo = EmailField('Correo electrónico', render_kw={'readonly': True})
	nombres = StringField('Nombres', render_kw={'readonly': True})
	apellidos = StringField('Apellidos', render_kw={'readonly': True})
	edad = IntegerField('Edad', render_kw={'readonly': True})
	genero = StringField('Género', render_kw={'readonly': True})
	cargo = StringField('Cargo', render_kw={'readonly': True})
	fechaIngreso = DateField('Fecha de ingreso', render_kw={'readonly': True})
	tipoContrato = StringField('Tipo de contrato', render_kw={'readonly': True})
	fechaTerminoContrato = DateField('Fecha término contrato', render_kw={'readonly': True})
	dependencia = StringField('Dependencia', render_kw={'readonly': True})
	salario = IntegerField('Salario', render_kw={'readonly': True})
	rol = StringField('Rol', render_kw={'readonly': True})
	puntaje = StringField('Puntaje', render_kw={'readonly': True})
	comentarios = StringField('Comentarios', render_kw={'readonly': True}, widget=TextArea())

# Formularios para géneros
class GenerosForm(FlaskForm):
	id = StringField('ID', render_kw={'readonly': True})
	descripcion = StringField('Descripción', validators=[DataRequired(message="Este campo es requerido")])
# END Formularios para géneros

# Formularios para cargos
class CargosForm(FlaskForm):
	id = StringField('ID', render_kw={'readonly': True})
	descripcion = StringField('Descripción', validators=[DataRequired(message="Este campo es requerido")])
# END Formularios para cargos

# Formularios para tiposContratos
class TiposContratosForm(FlaskForm):
	id = StringField('ID', render_kw={'readonly': True})
	descripcion = StringField('Descripción', validators=[DataRequired(message="Este campo es requerido")])
# END Formularios para tiposContratos

# Formularios para dependencias
class DependenciasForm(FlaskForm):
	id = StringField('ID', render_kw={'readonly': True})
	descripcion = StringField('Descripción', validators=[DataRequired(message="Este campo es requerido")])
# END Formularios para dependencias
