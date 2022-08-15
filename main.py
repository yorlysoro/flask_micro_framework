from flask import (Flask, request, make_response,
                   redirect, render_template)
from markupsafe import escape

app = Flask(__name__)

todos = ["Comprar Cafe",
         "Enviar Solicitud de compra",
         "Entregar video a productor"]


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
    response.set_cookie('user_ip', user_ip)
    return response


@app.route("/hello")
def hello():
    user_ip = escape(request.cookies.get('user_ip'))
    context = {
        'user_ip': user_ip,
        'todos': todos
    }
    #raise Exception('Error 500')
    return render_template('hello.html', **context)
