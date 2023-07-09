from email.mime import image
from flask_sqlalchemy import SQLAlchemy
from flaskr.models import *
import pymysql

db = SQLAlchemy()

def obtener_conexion():
        return pymysql.connect(host='localhost',
                                    user='root',
                                    password='',
                                    db='2455248_facturacion')



