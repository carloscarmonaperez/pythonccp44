import web
import model  


urls = (
    
    '/index', 'Index',
     '/agregar', 'Agregar',
     '/borrar', 'Borrar',
     '/editar', 'Editar',
     '/ver', 'Ver',
)
app = web.application(urls, globals())

render = web.template.render ('templates', base='master')

web.config.debug = False

     
class Index:        
   def GET(self):
    	products = model.get_products()
        return render.index(products)


        productos = model.get_productos()
        return render.index(productos)    
    
class Agregar(self):        
    def GET(self):
        return render insertar()
    def POST(self):
        form = web.input()  

imagen = web.input(imagen_producto={})

filedir = 'static/files'
filepath=imagen.imagen_productos.filename.replace('\\','/)
filename=filepatch.split('/')[-1]
#copiar archivos al servidor

fileserver = open(filedir + '/' + filename, 'w')
		fileserver.write(imagen.image_product.file.read())
		fileserver.close()

		image_producto = filename
		model.add_product(form['producto'],
			form['descripcion'],
			form['existencias'],
			form['precio_compra'],
			form['precio_venta'],
			imagen_producto
			)
		raise web.seeother('/')




model.insertar(
    form['producto'],
    form['producto'],form['existencias'],
    form['precio_compra'],form['precio_venta'],
    imagen_producto
    )

    raise web.seeother('/')
    return render.index()

class Borrar:        
       def GET(self, id_producto):
		data = model.get_product(int(id_producto))
		return render.delete(data)
	
	def POST(self, id_producto):
		form = web.input()
		model.delete_product(form.id_producto)
		raise web.seeother('/') 

class Editar:        
    def GET(self, id_producto):
		data = model.get_product(int(id_producto))
		return render.edit(data)

def POST(self, id_product):
		form = web.input()
		model.update_producto(form.id_producto, form.producto, form.descripcion, form.exitencias, form.precio_venta, form.precio_compra)
		raise web.seeother('/')


class Ver:        
      def GET(self, id_producto):
		data = model.get_product(int(id_producto))
		return render.see(data)

class Formulario:        
    def GET(self):  
        productos = model.get_productos()
        return render.formulario(productos)  

if __name__ == "__main__":
    app.run()
    
#UTIILIZAR POST ENVIAR DATOS DE UN FORMULARIO CON SEGURIDAD

#EN ARCRHIVOS METODO POST