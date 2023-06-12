from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from primera_app.forms import FormularioUsuario
from primera_app.models import PerfilUsuario


def usuario_listar(request):
    usuario_listar = PerfilUsuario.objects.all()
    return render (request, 'usuario_individual.html', {'usuario_listar':usuario_listar})

def usuario_indiv(request, user_id):
    usuario = PerfilUsuario.objects.get(user_id=user_id)
    context = {'usuario': usuario}
    return render (request, 'usuarios.html', context)


def registro_usuarios(request):
    if request.method=='POST':
        print(request.POST['nombre_usuario'])
        print(request.POST['nombre'])
        print(request.POST['apellido'])
        print(request.POST['email'])
        print(request.POST['clave'])
        print(request.POST['telefono'])

        usuario = User(
            username=request.POST['nombre_usuario'],
            first_name=request.POST['nombre'],
            last_name=request.POST['apellido'],
            email=request.POST['email'])
        usuario.save() 

        perfil = PerfilUsuario(
            edad = request.POST['edad'],
            telefono = request.POST['telefono'],
            direccion = request.POST['direccion'],
            ciudad = request.POST['ciudad'],
            user = usuario
        )

       
        perfil.save()



        return redirect(f'/usuarios/')
        
    else:
        usuarios_formulario = FormularioUsuario()
        context = {'formulario': usuarios_formulario}
        return render(request,'crear_usuario.html',context)


