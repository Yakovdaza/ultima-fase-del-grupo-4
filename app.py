from flask import Flask,g
from db import close_db
from routes.routes import *
from flask import current_app
import os


app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY="development"
    
)
IS_DEV = app.env == 'development'
UPLOAD_FOLDER = '/static/img/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 

#rutas de la aplicacion
# rutas sin log in
app.add_url_rule(routes["reg_rut"], view_func=routes["reg_cont"])
app.add_url_rule(routes["log_rut"], view_func=routes["log_cont"])
app.add_url_rule(routes["con_rut"], view_func=routes["con_cont"])
# rutas usuarios logeados
app.add_url_rule(routes["ind_rut"], view_func=routes["ind_cont"])
app.add_url_rule(routes["pros_rut"], view_func=routes["pros_cont"])
app.add_url_rule(routes["edituser_rut"], view_func=routes["edituser_cont"])
app.add_url_rule(routes["deluser_rut"], view_func=routes["deluser_cont"])
app.add_url_rule(routes["pro_rut"], view_func=routes["pro_cont"])
app.add_url_rule(routes["car_rut"], view_func=routes["car_cont"])
# rutas para admionistradores
app.add_url_rule(routes["creaPro_rut"], view_func=routes["creaPro_cont"])
app.add_url_rule(routes["edipro_rut"], view_func=routes["edipro_cont"])
app.add_url_rule(routes["delpro_rut"], view_func=routes["delpro_cont"])
app.add_url_rule(routes["regAd_rut"], view_func=routes["regAd_cont"])

#ruta del 404
app.register_error_handler(routes['notFound_route'],routes['not_found_cont'])


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

@app.route('/set_cookie')
def cookie_insertion():
    redirect_to_index = redirect('/')
    response = current_app.make_response(redirect_to_index )  
    response.set_cookie('cookie_name',value='values')
    return response

@app.before_request
def load_logged_in_user():
    username = session.get('username') #get es para devolver valores de un diccionario
    #print('entro a app.before_request')
    if username is None:
        g.user = None
        #print('g.user : ',g.user)
    else: #trae una tupla
        g.user = get_db().execute( 
            'SELECT * FROM usuario WHERE nombre= ?',(username,)
        ).fetchone()
        g.rol = g.user[7]
        db = get_db()
        g.productos2 = db.execute("SELECT * FROM producto").fetchall()

if  __name__ == "__main__":
    app.run(debug=True)
    assert os.path.exists('.env')  # for other environment variables...
    os.environ['FLASK_ENV'] = 'development'  # HARD CODE since default is production
   