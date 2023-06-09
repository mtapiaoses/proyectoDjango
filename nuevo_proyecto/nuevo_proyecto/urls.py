
from django.contrib import admin
from django.urls import path
from app1.views import  perfil_usuario, ingresar_datos_view,home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', perfil_usuario, name='usuarios'),
    path('ingresar-datos/<int:user_id>/', ingresar_datos_view, name='ingresar-datos')
  

     

]
