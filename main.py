from flask import (request, make_response,
                   redirect, render_template, session)
from flask_login import login_required, current_user
import unittest

from app import create_app
from app.firestore_service import get_todos


app = create_app()

todos = ["Comprar Cafe",
         "Enviar Solicitud de compra",
         "Entregar video a productor"]


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


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


@app.route("/hello", methods=['GET'])
@login_required
def hello():
    user_ip = session.get('user_ip')
    username = current_user.id

    context = {
        'user_ip': user_ip,
        'todos': get_todos(user_id=username),
        'username': username,
    }
    # raise Exception('Error 500')
    return render_template('hello.html', **context)
