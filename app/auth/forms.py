from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class LoginForm(FlaskForm):
    email = StringField(
        "Email: ",
        validators=[DataRequired(),
                    Email("Некоректный email")])
    psw = PasswordField(
        "Password: ",
        validators=[DataRequired(),
                    Length(min=4, max=100,
                           message="Пароль должен быть от 4 до 100 символов")])
    remember = BooleanField("Remember? ", default=False)
    submit = SubmitField("Enter")


class RegisterForm(FlaskForm):
    name = StringField(
        "Name: ",
        validators=[DataRequired(),
                    Length(min=3, max=50,
                           message="Имя должно быть от 3 до 50 символов")])
    address = StringField(
        "Address: ",
        validators=[Length(max=200,
                           message="Длина адресса не более 200 символов")])
    email = StringField(
        "Email: ",
        validators=[DataRequired(),
                    Email("Некоректный email")])
    psw1 = PasswordField(
        "Password: ",
        validators=[DataRequired(),
                    Length(min=4, max=100,
                           message="Пароль должен быть от 4 до 100 символов")])
    psw2 = PasswordField(
        "Repeat password: ",
        validators=[DataRequired(),
                    EqualTo('psw1', message="Пароли не совпадают")])
    submit = SubmitField("Регистрация")
