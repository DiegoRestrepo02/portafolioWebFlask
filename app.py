from http import cookies
from urllib import response
from flask import Flask, flash, make_response, redirect, render_template, request
from flask_mail import Mail, Message 

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'pruebaenviocorreos13@gmail.com'
app.config['MAIL_PASSWORD'] = '1000884059Diego'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app) 

@app.route("/")
def redirecionarIndex():
    return redirect("/index")

@app.route("/enConstruccion")
def enConstruccion():
    usuarioIp = request.cookies.get("usuarioIpInformacion")
    context = {
        "usuarioIp": usuarioIp
    }

    return render_template("enConstruccion.html", **context)

@app.route("/index")
def index():
    usuarioIpInformacion = request.remote_addr
    response = make_response(redirect("/informacion"))
    response.set_cookie('usuarioIpInformacion', usuarioIpInformacion)
    return response

@app.route("/informacion")
def informacion():
    usuarioIp = request.cookies.get("usuarioIpInformacion")
    context = {
        "usuarioIp": usuarioIp
    }

    return render_template("informacion.html", **context)

@app.route("/contacto")
def contacto():
    usuarioIp = request.cookies.get("usuarioIpInformacion")
    context = {
        "usuarioIp": usuarioIp
    }

    return render_template("contacto.html", **context)

@app.route("/enviarMensajeContacto", methods=['POST'])
def enviarMensajeContacto():
    try:
        search_term = request.form

        msg = Message( 
                    'Hola! Contacto Portafolio', 
                    sender ='pruebaenviocorreos13@gmail.com', 
                    recipients = [search_term['correo'], "losnoob29@gmail.com"] 
                ) 
        msg.body = 'Hola Diego, soy ' + search_term['nombre'] + " mi correo es " + search_term['correo'] + ' y me gustaria: ' + search_term['mensaje']
        mail.send(msg) 
        return '¡Mensaje enviado con exito!.'
    except:
        return 'ERROR:\nNo se logro enviar el mensaje.'

app.run(debug=True)
