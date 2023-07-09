from flaskr.models import db
from flaskr.models import *

class Categorias(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(128), unique=True, nullable=False)
    
    def __init__(self, categoria):
        self.categoria=categoria
    
def obtener_categorias():
    conexion = obtener_conexion()
    categorias = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, categoria FROM categorias")
        categorias = cursor.fetchall()
    conexion.close()
    return categorias

def obtener_categoria(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, categoria FROM categorias WHERE id = {}".format(id))
        categoria = cursor.fetchone()
    conexion.close()
    return categoria

def crear_categoria(categoria):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        consulta = "INSERT INTO categorias (categoria) VALUES('{}')"\
            .format(categoria.categoria)
        cursor.execute(consulta)
        conexion.commit()
    conexion.close()

def actualizar_categoria(categoria):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        consulta = "UPDATE categorias SET categoria = '{}' WHERE id = {}"\
            .format(categoria.categoria, categoria.id)
        cursor.execute(consulta)
        conexion.commit()
    conexion.close()   

def eliminar_categoria(id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            consulta = "DELETE FROM categorias WHERE id = {}".format(id)
            cursor.execute(consulta)
            conexion.commit()
            conexion.close()
    except:
        conexion.close()
    
    