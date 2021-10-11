from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SelectField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField, DateField
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
	genero = SelectField('Género', choices = [('masculino', 'Masculino'), ('femenino', 'Femenino')])
	cargo = StringField('Cargo', validators=[DataRequired(message="Este campo es requerido")])
	fechaIngreso = DateField('Fecha de ingreso', validators=[DataRequired(message="Este campo es requerido")])
	tipoContrato = StringField('Tipo de contrato', validators=[DataRequired(message="Este campo es requerido")])
	fechaTerminoContrato = DateField('Fecha término contrato', validators=[DataRequired(message="Este campo es requerido")])
	dependencia = StringField('Dependencia', validators=[DataRequired(message="Este campo es requerido")])
	salario = IntegerField('Salario', widget=NumberInput(min=0, step=1), validators=[DataRequired(message="Este campo es requerido")])
	rol = SelectField('Rol', choices = [('usuarioFinal', 'Usuario final'), ('administrador', 'Administrador'), ('superAdministrador', 'SuperAdministrador')])

class EditarUsuarioForm(FlaskForm):
	id = StringField('ID', render_kw={'readonly': True}, validators=[DataRequired(message="Este campo es requerido")])
	correo = EmailField('Correo electrónico', validators=[DataRequired(message="Este campo es requerido")])
	nombres = StringField('Nombres', validators=[DataRequired(message="Este campo es requerido")])
	apellidos = StringField('Apellidos', validators=[DataRequired(message="Este campo es requerido")])
	edad = IntegerField('Edad', widget=NumberInput(min=18, max=200, step=1), validators=[DataRequired(message="Este campo es requerido")])
	genero = SelectField('Género', choices = [('masculino', 'Masculino'), ('femenino', 'Femenino')])
	cargo = StringField('Cargo', validators=[DataRequired(message="Este campo es requerido")])
	fechaIngreso = DateField('Fecha de ingreso', validators=[DataRequired(message="Este campo es requerido")])
	tipoContrato = StringField('Tipo de contrato', validators=[DataRequired(message="Este campo es requerido")])
	fechaTerminoContrato = DateField('Fecha término contrato', validators=[DataRequired(message="Este campo es requerido")])
	dependencia = StringField('Dependencia', validators=[DataRequired(message="Este campo es requerido")])
	salario = IntegerField('Salario', widget=NumberInput(min=0, step=1), validators=[DataRequired(message="Este campo es requerido")])
	rol = SelectField('Rol', choices = [('usuarioFinal', 'Usuario final'), ('administrador', 'Administrador'), ('superAdministrador', 'SuperAdministrador')])

class VerUsuarioForm(FlaskForm):
	id = StringField('ID', render_kw={'readonly': True}, validators=[DataRequired(message="Este campo es requerido")])
	correo = EmailField('Correo electrónico', render_kw={'readonly': True}, validators=[DataRequired(message="Este campo es requerido")])
	nombres = StringField('Nombres', render_kw={'readonly': True}, validators=[DataRequired(message="Este campo es requerido")])
	apellidos = StringField('Apellidos', render_kw={'readonly': True}, validators=[DataRequired(message="Este campo es requerido")])
	edad = IntegerField('Edad', render_kw={'readonly': True}, widget=NumberInput(min=18, max=200, step=1), validators=[DataRequired(message="Este campo es requerido")])
	genero = SelectField('Género', render_kw={'readonly': True}, choices = [('masculino', 'Masculino'), ('femenino', 'Femenino')])
	cargo = StringField('Cargo', render_kw={'readonly': True}, validators=[DataRequired(message="Este campo es requerido")])
	fechaIngreso = DateField('Fecha de ingreso', render_kw={'readonly': True}, validators=[DataRequired(message="Este campo es requerido")])
	tipoContrato = StringField('Tipo de contrato', render_kw={'readonly': True}, validators=[DataRequired(message="Este campo es requerido")])
	fechaTerminoContrato = DateField('Fecha término contrato', render_kw={'readonly': True}, validators=[DataRequired(message="Este campo es requerido")])
	dependencia = StringField('Dependencia', render_kw={'readonly': True}, validators=[DataRequired(message="Este campo es requerido")])
	salario = IntegerField('Salario', render_kw={'readonly': True}, widget=NumberInput(min=0, step=1), validators=[DataRequired(message="Este campo es requerido")])
	rol = SelectField('Rol', render_kw={'readonly': True}, choices = [('usuarioFinal', 'Usuario final'), ('administrador', 'Administrador'), ('superAdministrador', 'SuperAdministrador')])
