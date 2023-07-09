from . import db
from flaskr.models import *

class usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128), unique=True, nullable=False)
    tipo_documento = db.Column(db.String(2), nullable=False)
    numero_documento = db.Column(db.String(20), unique=True, nullable=False)
    direccion = db.Column(db.String(500), nullable=False)
    telefono = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    contrasena = db.Column(db.String(20), nullable=False)
    rol = db.Column(db.String(20), nullable=False)
    
    def __init__(self, usuarios):
        self.usuarios = usuarios
        
def obtener_usuarios():
    conexion = obtener_conexion()
    usuarios=[]
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, nombre, email, rol FROM usuarios")
        usuarios = cursor.fetchall()
    conexion.close()
    return usuarios

def obtener_usuario(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, nombre, email, rol FROM usuarios WHERE id = {}".format(id))
        rol = cursor.fetchone()
    conexion.close()
    return rol

def crear_usuario(self, usuarios):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        consulta = "INSERT INTO usuarios (usuario) VALUES('{}')".format(usuarios.usuarios)
        cursor.execute(consulta)
    conexion.commit()
    conexion.close()

def actualizar_usuario(usuario):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        consulta = "UPDATE usuarios SET usuario = '{}' WHERE id = {}"\
            .format(usuario.usuario, usuario.id)
        cursor.execute(consulta)
        conexion.commit()
    conexion.close()   

def eliminar_usuario(id):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            consulta = "DELETE FROM usuarios WHERE id = {}".format(id)
            cursor.execute(consulta)
            conexion.commit()
            conexion.close()
    except:
        conexion.close()
    
