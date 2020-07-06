from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
	path('create', views.CreateProducto, name='createProducto'),
	path('listado', views.ListarProductosComprar, name='listarProductosComprar'),
	path('listado/ver', views.ListarProductosPropios, name='listarProductosPropios'),
	path('eliminar/<int:id_producto>', views.DeleteProducto, name='deleteProducto'),
	path('modificar/<int:id_producto>', views.ModificarProducto, name='modificarProducto'),
	path('comprar/<int:id_producto>', views.ComprarProducto, name='comprarProducto')
]