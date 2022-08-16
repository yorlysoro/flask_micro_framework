from flask import (Flask, request, make_response,
                   redirect, render_template, session)
from markupsafe import escape
from flask_bootstrap import Bootstrap5
from pathlib import Path
from dotenv import load_dotenv
import os
from flask_wtf import FlaskForm
from wtforms.fields import (StringField, PasswordField,
                            SubmitField)
from wtforms.validators import DataRequired

BASE_DIR = Path(__file__).resolve()
dotenv_path = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)
Bootstrap5(app)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

todos = ["Comprar Cafe",
         "Enviar Solicitud de compra",
         "Entregar video a productor"]


class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Enviar')


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)


@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    # response.set_cookie('user_ip', user_ip)
    session['user_ip'] = user_ip
    return response


@app.route("/hello")
def hello():
    user_ip = session.get('user_ip')
    login_form = LoginForm()
    context = {
        'user_ip': user_ip,
        'todos': todos,
        'login_form': login_form,
    }
    # raise Exception('Error 500')
    return render_template('hello.html', **context)
