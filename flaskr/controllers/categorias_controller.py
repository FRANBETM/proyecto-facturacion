
from hashlib import new
from flask_controller import FlaskController
from flaskr.app import app
from flask import render_template, session
from flaskr.models import db, categorias, productos, facturas, facturas_productos
from flask import request, redirect, url_for, flash

class CategoriasController(FlaskController):   
    @app.route("/categorias")
    def categorias():       
        result_categorias = categorias.obtener_categorias()
        return render_template('categorias.html', titulo='Gestión de Categorias', lista_categorias=result_categorias)
    
    @app.route("/crear_categoria", methods=['GET','POST'])
    def crear_categoria():
        if request.method == 'POST':
            nombre_categoria = request.form.get('categoria')
            if not nombre_categoria:
                flash('La categoría es un campo obligatorio')   
            else:          
                categoria = categorias.Categorias(nombre_categoria)
                categorias.crear_categoria(categoria=categoria)
                return redirect(url_for('categorias'))
        return render_template('crear_categoria.html', titulo='Nueva Categoría')
    
    @app.route("/editar_categoria/<int:id>", methods=['GET'])
    def editar_categoria(id=0):         
        categoria = categorias.obtener_categoria(id)    
        return render_template('editar_categoria.html', categoria=categoria, titulo="Editar Categoria")
    
    @app.route("/actualizar_categoria", methods=['POST'])
    def actualizar_categoria():        
        id_categoria = request.form.get('id')
        nombre_categoria = request.form.get('categoria')
        if not nombre_categoria:
            flash('La categoría es un campo obligatorio')   
        else:          
            categoria = categorias.Categorias(nombre_categoria)
            categoria.id = id_categoria
            categorias.actualizar_categoria(categoria=categoria)
            return redirect(url_for('categorias'))
    
    @app.route("/eliminar_categoria/<int:id>")
    def eliminar_categoria(id):
        categorias.eliminar_categoria(id=id)
        return redirect(url_for('categorias'))
    