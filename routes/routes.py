from controllers.controller import *
from controllers.errors import *


routes = {
    #'':'','':as_view(),
    # rutas sin log in
    'reg_rut':'/registrarse','reg_cont': registerController.as_view('registrarse'),
    'log_rut':'/login','log_cont':loginController.as_view('login'),
    'con_rut':'/contacto','con_cont': contactController.as_view('contacto'),
    # rutas usuarios logeados
    'ind_rut':'/','ind_cont':indexController.as_view('index'),
    'pros_rut':'/productos','pros_cont': productosController.as_view('productos'),
    'pro_rut':'/producto/<string:name>','pro_cont': productController.as_view('producto'),
    'edituser_rut':'/edituser/<int:id>','edituser_cont': editarUsuarioController.as_view('editar usuario'),
    'deluser_rut':'/deluser/<string:username>','deluser_cont': eliminarUsuarioController.as_view('usuario eliminado'),
    'car_rut':'/carrito','car_cont': carController.as_view('carrito'),
    # rutas para admionistradores
    'creaPro_rut':'/crearproducto','creaPro_cont': crearProductoController.as_view('crearproducto'),
    'edipro_rut':'/ediproductos/<int:id_producto>','edipro_cont': editarProductoController.as_view('editar'),
    'delpro_rut':'/delproducto/<int:id_producto>','delpro_cont': eliminarProductoController.as_view('eliminado'),
    'regAd_rut':'/registrarAdmin','regAd_cont': registerADController.as_view('registrar Admin'),
    
    
    # pagina de error 404 
    'notFound_route': 404, 'not_found_cont':notFoundController.as_view('error')
}
