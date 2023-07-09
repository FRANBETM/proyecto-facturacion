from flaskr.models import db, pedidos

pedidos_productos = db.Table('pedidos_productos', \
    db.Column('id_pedido', db.Integer, db.ForeignKey('pedidos.id'), primary_key=True),\
    db.Column('id_producto', db.Integer, db.ForeignKey('productos.id'), primary_key=True),\
    db.Column('cantidad', db.Float(10,8)),\
    db.Column('valor_unitario', db.Float(10,8)))