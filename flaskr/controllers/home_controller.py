from flask_controller import FlaskController
from flaskr.app import app
from flask import render_template

class HomeController(FlaskController):
    @app.route("/home")
    def index():
        return render_template('index.html', titulo='Home')