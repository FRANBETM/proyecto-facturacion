from flask_controller import FlaskController
from flaskr.app import app
from flask import render_template, session, request, redirect, url_for, flash
from flaskr.models import db, usuarios

class LoginController:
    @app.route("/", methods=['POST', 'GET'])
    def login():
        if request.method == 'POST':
            if 'email' in request.form and 'contrasena' in request.form:
                email = request.form['email']
                contrasena = request.form['contrasena']
                return render_template('index.html', titulo='Home')
            else:
                    flash('Correo o contraseña incorrectos', 'error')
                    return redirect(url_for('login'))
        
        return render_template('login.html', titulo='Login')

   