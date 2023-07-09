from flaskr.models import db, facturas

facturas_productos = db.Table('facturas_productos', \
    db.Column('id_factura', db.Integer, db.ForeignKey('facturas.id'), primary_key=True),\
    db.Column('id_producto', db.Integer, db.ForeignKey('productos.id'), primary_key=True),\
    db.Column('cantidad', db.Float(10,8)),\
    db.Column('valor_unitario', db.Float(10,8)))