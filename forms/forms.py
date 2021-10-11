from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField, SelectField, FileField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField

class LoginForm(FlaskForm):
    correo = EmailField('Correo electrónico', validators=[DataRequired(message="Este campo es requerido")])
    password = PasswordField('Contraseña', validators=[DataRequired(message="Este campo es requerido")])
