from flask_wtf import FlaskForm
from wtforms.fields import StringField, BooleanField, PasswordField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email, Length, DataRequired


class LoginForm(FlaskForm):
    email = EmailField("Email")
    password = PasswordField("Senha", validators=[Length(3, 6, "O campo deve conter entre 3 á 6 caracteres.")])
    remenber = BooleanField("Permanecer Conectado")
    submit = SubmitField("Logar")


class RegisterForm(FlaskForm):
    name = StringField("Nome Complato", validators=[DataRequired("O campo é obrigatório")])
    email = EmailField("Email", validators=[ Email("E-mail invalido") ])
    password = PasswordField("Senha", validators=[Length(3, 6, "O campo deve conter entre 3 á 6 caracteres.")])
    submit = SubmitField("Cadastrar")