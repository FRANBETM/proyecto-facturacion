from flask import Flask

def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/2455248_facturacion'
    app.config['SQLALCHEMY_DATABASE_MODIFICATIONS'] = False
    return app

