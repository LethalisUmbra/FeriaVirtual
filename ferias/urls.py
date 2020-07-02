from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
	path('create', views.CreateFeria, name='createFeria'),
	path('listado', views.ListarFerias, name='listarFerias'),
	path('eliminar/<int:id_feria>', views.DeleteFeria, name='deleteFeria'),
	path('modificar/<int:id_feria>', views.ModificarFeria, name='modificarFeria')
]