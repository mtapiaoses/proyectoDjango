from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from app1.models import PerfilDeUsuario



def perfil_usuario(request):
    usuarios = PerfilDeUsuario.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})
from django.shortcuts import render


def ingresar_datos_view(request, user_id):

        usuario = PerfilDeUsuario.objects.get(user_id=user_id)
        context = {'usuario' : usuario}
        # Realiza cualquier operación con el usuario encontrado
        return render(request, 'perfil_usuario.html', context)

def home(request):
    return render(request,'base.html')