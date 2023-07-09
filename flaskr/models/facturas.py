from flaskr.models import db, usuarios, clientes

class Facturas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, nullable=False)    
    id_cliente = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    id_vendedor = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
