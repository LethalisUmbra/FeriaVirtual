from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from api.api import UserAPI
from . import views

#imports para debug
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('ferias/',include('ferias.urls')),
    path('productos/',include('productos.urls')),
    path('login', views.login, name='login'),
    path('logout', LogoutView.as_view(template_name='login.html'), name='logout'),
    path('api/', include('api.urls'), name='api'),
    path('api/1.0/create_user/', UserAPI.as_view(), name="api_create_user"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)