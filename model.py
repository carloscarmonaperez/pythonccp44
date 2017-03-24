import web
# database heroku        
db_host='edo4plet5mhv93s3.cbetxkdyhwsb.us-east-1.rds.amazonaws.com';
db_name='zna0zlhsq9z8gu8g';
db_user'l2p55lasihlxw5hk';
db_pw="aagizcum2em36gxo";

#conexion con datos anteriores
db = web.database(
    dbn= 'mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
)


#Borrar
def borrar(id):
	db.delete('products', where='id_producto=$id', vars=locals())

#Registrar

def registrar(producto, descripcion, exitencias, precio_venta, precio_compra, image):
    db.insert('productos',
    	producto=producto, 
    	description=description, 
    	exitencias=stock,
    	cost_price=cost_price,
    	sale_price=sale_price,
    	imagen_producto=image)

#Actualizar
def actualizar(id, producto, descripcion, exitencias, precio_compra, precio_venta):
	    db.update('productos',
	    	where="id_producto=$id", 
	    	vars=locals(), 
	    	producto=producto, 
	    	descripcion=descripcion, 
	    	exitencias=exitencias, 
	    	precio_compra=precio_compra, 
	    	precio_venta=precio_venta)

# obtencion de datos
def get_productos():
	try:
		return db.select('productos')
	except Exception, e:
		return e

def get_product(id):
	try:
		return db.select('productos', where='id_producto=$id', vars=locals())[0]
	except Exception, e:
		return e


 