from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Usuario', 
                           validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Contraseña', 
                             validators=[DataRequired(), Length(min=6, max=30)])
    submit = SubmitField('Registrarse')

class LoginForm(FlaskForm):
    username = StringField('Usuario', 
                           validators=[DataRequired()])
    password = PasswordField('Contraseña', 
                             validators=[DataRequired()])
    submit = SubmitField('Iniciar Sesión')
