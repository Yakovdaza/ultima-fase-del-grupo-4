import os
from sqlite3.dbapi2 import connect
from flask.views import MethodView
from flask import render_template,request,redirect,flash,jsonify,session,g
from db import get_db
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename, send_from_directory

UPLOAD_FOLDER = '/static/img/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


class indexController(MethodView):
    def get(self):
        if "username" in session:
            print(g.rol)
            return render_template("index.html")
        else:
            return redirect("/login")
        
class contactController(MethodView):
    def get(self):
        return render_template("contacto.html")
    
class productosController(MethodView):
    def get(self):
        if "username" in session:
            db = get_db()
            producto = db.execute("SELECT* FROM producto")
            g.productos = producto.fetchall()
            return render_template("productos.html",productos= g.productos)
        else:
            return redirect("/")

class productController(MethodView):
    
    def get(self,name):
        if "username" in session:
            db = get_db()
            comentarios = db.execute("SELECT * FROM comentarios WHERE producto =?",(name,))
            producto = db.execute("SELECT* FROM producto WHERE nombre=?",(name,)).fetchone()
            g.producto = producto
            g.data = comentarios.fetchall()
            return render_template("producto.html", data= g.data,product= g.producto)
        else:
            return redirect ("/login")
    def post(self,name):
        try:
                userid = g.user[0]
                comentario = request.form["comentario"]
                calificacion=request.form["estrellas"]
                db= get_db()
                db.execute('INSERT INTO comentarios(idUsuario,comentario,producto,calificacion) VALUES(?,?,?,?)',(userid,comentario,name,calificacion))
                db.commit()
                return redirect(name)        
        except:
            flash("no se guardo el comentario","error")
            return redirect(name) 
class eliminarProductoController(MethodView):
    def post(self,id_producto):
        db= get_db()
        db.execute('DELETE FROM producto WHERE idProducto=?', (id_producto,))
        db.commit()
        return redirect("/productos")

class eliminarUsuarioController(MethodView):
    def post(self,name):
        db= get_db()
        db.execute('DELETE FROM ususario WHERE nombre=?', (name,))
        db.commit()
        return redirect("/registrarAdmin")
        
class editarUsuarioController(MethodView):
    def get(self,id):
        
        if g.rol==1:
            db= get_db()
            usuario= db.execute('SELECT * FROM usuario WHERE idUsuario=?',(id,)).fetchone()
            
            return render_template("editarUsuario.html",usuario=usuario)
        
        else:
            return redirect("/registarAdmin")
        
        
    def post(self,id):
        
        nombre = request.form["nombre"]
        correo = request.form["correo"]
        telefono = request.form["telefono"]
        date = request.form["fecha"]
        rol=request.form["tipoUsuario"]
        
        db= get_db()
        db.execute (
            'UPDATE usuario SET nombre=?,correo=?,telefono=?,fechaNacimiento=?,TipoUsuario=? WHERE idUsuario=?',(nombre,correo,telefono,date,rol,id)
            )
        db.commit()
        flash("producto creado","success")
        return redirect("/registrarAdmin") 
        
class editarProductoController(MethodView):
    def get(self,id_producto):
        db= get_db()
        edProduct=db.execute('SELECT* FROM producto WHERE idProducto=?', (id_producto,)).fetchone()
        db.commit()
        return render_template("editarProducto.html",producto=edProduct)
    
    def post(self,id_producto):
        
        id=id_producto
        if "file" not in request.files:
            flash("no hay archivo","error")
            return render_template("crearProducto.html")
        file = request.files["file"]
        nombre = request.form["nombre"]
        price= request.form["precio"]
        status=request.form["estado"]
        code =request.form["codigo"]
        descripcion = request.form["descripcion"]
        if file.filename=="":
            db= get_db()
            db.execute (
                'UPDATE producto SET idProducto=?,nombre=?,descripcion=? WHERE idProducto=? ',(id,nombre,descripcion,id)
                )
            db.commit()
            flash("producto creado","success")
            return redirect("/crearproducto") 
        if file.filename and allowed_file(file.filename):
            id=id_producto
            filename = secure_filename(file.filename)
            file.save(os.getcwd()+UPLOAD_FOLDER + filename)
            filename1 =".." +UPLOAD_FOLDER + filename
            db= get_db()
            db.execute (
                'UPDATE producto SET idProducto=?,nombre=?,descripcion=?,imagen=? precioVenta=? esatdo=? codigo=? WHERE idProducto=? ',(id,nombre,descripcion,filename1,price,status,code,id)
                )
            db.commit()
            flash("producto creado","success")
            return redirect("/crearproducto") 
    
    
class registerController(MethodView):
    
    def get(self):
        if "username" in session:
            return redirect("/")
        else:
            return render_template("registrarse.html")
    
    def post(self):
        
        try:
            nombre = request.form["nombre"]
            correo = request.form["correo"]
            telefono = request.form["telefono"]
            contraseña =request.form["contraseña"]
            date = request.form["date"]
            db= get_db()
            db.execute('INSERT INTO usuario(nombre,correo,telefono,contrasena,fechaNacimiento,TipoUsuario) VALUES(?,?,?,?,?,?)',(nombre,correo,telefono,generate_password_hash(contraseña),date,3))
            db.commit()
            flash("la informacion se ingresado con exito","success")
            return redirect("/")
        except:
            flash("un error ha ocurrido ","error")
            return render_template("registrarse.html")

class registerADController(MethodView):
    
    def get(self):
        
        if "username" in session:
            user = get_db().execute( 
            'SELECT * FROM usuario').fetchall()
            
            return render_template("crearUsuario.html",user=user)
        else:
            return redirect("/")

    def post(self):
        
        try:
            nombre = request.form["nombre"]
            correo = request.form["correo"]
            telefono = request.form["telefono"]
            contraseña =request.form["contraseña"]
            date = request.form["date"]
            db= get_db()
            db.execute('INSERT INTO usuario(nombre,correo,telefono,contrasena,fechaNacimiento,idTipoUsuario)',(nombre,correo,telefono,generate_password_hash(contraseña),date,1))
            db.commit()
            flash("la informacion se ingresado con exito","success")
            return redirect('/registrarAdmin')
        except:
            flash("un error ha ocurrido ","error")
            return redirect('/registrarAdmin')
        
class loginController(MethodView):
    def get(self):
        if "username" in session:
            return redirect("/")
        else:
            return render_template ("login.html")
    
    def post(self):
        try:
            correo = request.form["Email"]
            contraseña = request.form["password"]
            db= get_db()
            user = db.execute(
                "SELECT * FROM usuario WHERE correo=?",(correo,)
                ).fetchone()
            
            dbpass = user[4]
            valPassword = check_password_hash(dbpass,contraseña)
            
            #print(valPassword)
            #print(user[6])
            
            if user is None:
                flash("usuario o contraseña incorrectos ","error")
                return redirect("/login")
            else :
                if valPassword == True:
                    session["username"]= user[1]
                    return redirect("/")
        except:
            flash("un error ha ocurrido no try ","error")
            return redirect("/login")

class carController(MethodView):
    
    def get(self):
        if "username" in session:
            return render_template("carrito_de_compra.html")
        else:
            return render_template("login.html") 
    #def post(self)
    
def allowed_file(filename):
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
def ruta(filename):
    return send_from_directory(os.getcwd() + UPLOAD_FOLDER ,filename=filename , as_attachment=False)            

class crearProductoController(MethodView):
    def get(self):
        try:
            if g.rol == 1:
                return render_template("crearProducto.html")
        except:
            return redirect("/")
    def post(self):
        if g.rol == 1:
            try:    
                if "file" not in request.files:
                    flash("no hay archivo","error")
                    return render_template("crearProducto.html")
                file = request.files["file"]
                nombre = request.form["nombre"]
                descripcion = request.form["descripcion"]
                price= request.form["precio"]
                status=request.form["estado"]
                code =request.form["codigo"]
                if file.filename=="":
                    flash("no hay archivo correcto","error")
                    return render_template("crearProducto.html")
                if file.filename and allowed_file(file.filename):
                    
                    filename = secure_filename(file.filename)
                    file.save(os.getcwd()+UPLOAD_FOLDER + filename)
                    filename1 =".." +UPLOAD_FOLDER + filename
                    db= get_db()
                    db.execute (
                        'INSERT INTO producto(nombre,descripcion,imagen,precioVenta,estado,codigo) VALUES(?,?,?,?,?,?)',(nombre,descripcion,filename1,price,status,code)
                        )
                    db.commit()
                    flash("producto creado","success")
                    return redirect("/crearproducto") 
                else:
                    flash("problema en file","error" )
                    return redirect("/crearproducto")
                
            except:
                flash("no creado","error")
                return redirect("/crearproducto")