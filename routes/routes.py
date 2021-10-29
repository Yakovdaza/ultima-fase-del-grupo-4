from controllers.controller import *
from controllers.errors import *


routes = {
    #'':'','':as_view(),
    'ind_rut':'/','ind_cont':indexController.as_view('index'),
    'log_rut':'/login','log_cont':loginController.as_view('login'),
    'reg_rut':'/registrarse','reg_cont': registerController.as_view('registrarse'),
    'regAd_rut':'/registrarAdmin','regAd_cont': registerADController.as_view('registrar Admin'),
    'con_rut':'/contacto','con_cont': contactController.as_view('contacto'),
    'pro_rut':'/producto/<string:name>','pro_cont': productController.as_view('producto'),
    'pros_rut':'/productos','pros_cont': productosController.as_view('productos'),
    'edipro_rut':'/ediproductos/<int:id_producto>','edipro_cont': editarProductoController.as_view('editar'),
    'delpro_rut':'/delproductos/<int:id_producto>','delpro_cont': eliminarProductoController.as_view('eliminado'),
    'car_rut':'/carrito','car_cont': carController.as_view('carrito'),
    'creaPro_rut':'/crearproducto','creaPro_cont': crearProductoController.as_view('crearproducto'),
    
    
    # pagina de error 404 
    'notFound_route': 404, 'not_found_cont':notFoundController.as_view('error')
}
