
from flaskr.models import db, categorias, productos, facturas, facturas_productos, proveedores, pedidos, pedidos_productos
from flaskr import create_app
from flask_controller import FlaskControllerRegister

app = create_app('default')
app.secret_key = 'super secret key'
app_context = app.app_context()
app_context.push()
register = FlaskControllerRegister(app)

register.register_package('flaskr.controllers')

db.init_app(app)
db.create_all()





