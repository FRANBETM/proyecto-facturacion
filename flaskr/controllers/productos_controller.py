
from hashlib import new
from flask_controller import FlaskController
from flaskr.app import app
from flask import render_template
from flaskr.models import db, categorias, productos, facturas, facturas_productos
from flask import request, redirect, url_for, flash

class ProductosController(FlaskController):   
    @app.route("/productos")
    def productos():
        resultProductos = productos.obtener_productos()
        return render_template('productos.html', titulo='Gestión de Productos', lista_productos=resultProductos)
    
    @app.route("/crear_producto", methods=['GET','POST'])
    def crear_producto():
        if request.method == 'POST':
            descripcion = request.form.get('descripcion')
            valor_unitario = request.form.get('valor_unitario')
            unidad_medida = request.form.get('unidad_medida')
            cantidad_stock = request.form.get('cantidad_stock')
            categoria = request.form.get('categoria')
            if not descripcion:
                flash('La descripción es un campo obligatorio') 
            elif not valor_unitario:
                flash('El valor unitario es un campo obligatorio')     
            elif not unidad_medida:
                flash('La unidad de medida es un campo obligatorio')    
            elif not cantidad_stock:
                flash('La cantidad en stock es un campo obligatorio')    
            elif not categoria:
                flash('La categoria es un campo obligatorio')  
            else:          
                producto = productos.Productos(descripcion,valor_unitario,unidad_medida,cantidad_stock,categoria)
                productos.crear_producto(producto=producto)
                return redirect(url_for('productos'))
        lista_categorias=[]    
        lista_categorias = categorias.obtener_categorias()
        return render_template('crear_producto.html', titulo='Nuevo Producto', categorias=lista_categorias)
    
    @app.route("/eliminar_producto/<int:id>/")
    def eliminar_producto(id):
        productos.eliminar_producto_producto(id=id)
        return redirect(url_for('productos'))
    
