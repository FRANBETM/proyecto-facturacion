from hashlib import new
from flask_controller import FlaskController
from flaskr.app import app
from flask import render_template, session, request, redirect, url_for, flash
from flaskr.models import db, usuarios

class usuariosController(FlaskController):
    @app.route("/usuarios")
    def usuarios():
        result_usuarios = usuarios.obtener_usuarios()
        return render_template('usuarios.html', titulo='Gestión de usuarios', lista_usuarios=result_usuarios)

    @app.route("/crear_usuario", methods=['GET','POST'])
    def crear_usuario():
        if request.method == 'POST':
            nombre_usuario = request.form.get('usuarios')
            if not nombre_usuario:
                flash('El usuario es un campo obligatorio')
            else:
                usuarios = usuarios(nombre_usuario=nombre_usuario)
                usuarios.crear_usuario(usuarios)
                return redirect(url_for('usuarios'))
        return render_template('crear_usuario.html', titulo='Nuevo usuario')

    @app.route("/editar_usuario/<int:id>", methods=['GET'])
    def editar_usuario(id=0):         
        usuario = usuarios.obtener_usuario(id)    
        return render_template('editar_usuario.html', usuario=usuario, titulo="Editar usuario")
    
    @app.route("/actualizar_usuario", methods=['POST'])
    def actualizar_usuario():
        id_usuario = request.form.get('id')
        nombre_usuario = request.form.get('usuario')
        if not nombre_usuario:
          flash('El usuario es un campo obligatorio')
        else:
            usuario = usuarios.obtener_usuario(id_usuario)
            usuario.nombre = nombre_usuario
            usuarios.actualizar_usuario(usuario=usuario)
            return redirect(url_for('usuarios'))
    
    # Si el flujo llega hasta aquí, significa que ocurrió un error
        flash('Ocurrió un error al actualizar el usuario', 'error')
        return redirect(url_for('usuarios'))
    
    @app.route("/eliminar_usuario/<int:id>")
    def eliminar_usuario(id):
        usuarios.eliminar_usuario(id=id)
        return redirect(url_for('usuarios'))
    