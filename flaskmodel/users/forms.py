from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20),])
    email = StringField('Email', validators=[DataRequired(), Email(),])
    password = PasswordField('Senha', validators=[DataRequired(), ])
    check_password = PasswordField('Verificação de Senha', validators=[DataRequired(), EqualTo('password')])
    submit_button = SubmitField('Cadastrar')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(),])
    password = PasswordField('Senha', validators=[DataRequired(), ])
    submit_button = SubmitField('Entrar')
