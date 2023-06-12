from django import forms


class FormularioUsuario(forms.Form):
    nombre_usuario = forms.CharField(max_length=50, min_length=8,widget=forms.TextInput(attrs={'class':'form-control'}))
    nombre = forms.CharField(max_length=50, min_length=8,widget=forms.TextInput(attrs={'class':'form-control'}))
    apellido = forms.CharField(max_length=50, min_length=8,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(max_length=50, min_length=8,widget=forms.TextInput(attrs={'class':'form-control'}))            #type = password
    clave = forms.CharField(max_length=50, min_length=8,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    edad = forms.IntegerField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    telefono = forms.CharField(max_length=50, min_length=8,widget=forms.TextInput(attrs={'class':'form-control'})) 
    direccion = forms.CharField(max_length=50, min_length=8,widget=forms.TextInput(attrs={'class':'form-control'}))
    ciudad = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
