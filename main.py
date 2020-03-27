from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

todos = ['Comprar café', 'Enviar solicitud', 'Entregar video']


@app.route('/')
def index():
    user_ip = request.remote_addr  # IP del usuario

    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)

    return response


@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip': user_ip,
        'todos': todos,
    }

    return render_template('hello.html', **context)
