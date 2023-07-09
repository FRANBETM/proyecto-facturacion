from enum import unique
import flaskr
from flaskr.models import db, categorias
from flaskr.models import *

class Productos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(128), unique=True, nullable=False)
    valor_unitario = db.Column(db.Float(10,8))
    unidad_medida = db.Column(db.String(3), nullable=False)
    cantidad_stock = db.Column(db.Float(10,8))
    categoria = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
    
    def __init__(self,descripcion, valor_unitario,unidad_medida,cantidad_stock,categoria):
        self.descripcion=descripcion
        self.valor_unitario=valor_unitario
        self.unidad_medida=unidad_medida
        self.cantidad_stock=cantidad_stock
        self.categoria=categoria
   
def obtener_productos():
    conexion = obtener_conexion()
    productos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT T1.id, descripcion, valor_unitario, unidad_medida, cantidad_stock, T2.id as id_categoria , T2.categoria as categoria FROM productos AS T1 INNER JOIN categorias AS T2 ON T1.categoria = T2.id")
        productos = cursor.fetchall()
    conexion.close()
    return productos

def obtener_producto(id):
    conexion = obtener_conexion()
    productos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, descripcion, valor_unitario, unidad_medida, cantidad_stock, categoria FROM productos WHERE id = {}".format(id))
        productos = cursor.fetchall()
    conexion.close()
    return productos

def crear_producto(producto):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        consulta = "INSERT INTO productos (descripcion, valor_unitario, unidad_medida, cantidad_stock, categoria) VALUES('{}',{},'{}',{},{})"\
            .format(producto.descripcion, producto.valor_unitario, producto.unidad_medida, producto.cantidad_stock, producto.categoria)
        cursor.execute(consulta)
        conexion.commit()
    conexion.close()

def eliminar_producto(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        consulta = "DELETE FROM productos WHERE id = {}".format(id)
        cursor.execute(consulta)
        conexion.commit()
    conexion.close()
    
    