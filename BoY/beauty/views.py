from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages  
from .forms import CustomUserCreationForm 

# Create your views here.

def login_view(request):
    if request.method == 'GET':
        context = ''
        return render(request, 'beauty/login.html', {'context': context})
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            context = {'error': 'Credenciales erroneas'}
            return render(request, 'beauty/login.html', {'context': context})

    return render(request, 'beauty/login.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Validación adicional para confirmar que password1 y password2 coincidan
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password1 != password2:
                messages.error(request, 'Las contraseñas no coinciden.')
                return redirect('registro')  # Reemplaza 'registro' con el nombre de tu vista de registro

            # Continuar con el registro normal si las contraseñas coinciden
            user = form.save()

            # Autenticar al usuario después de registrarse
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user:
                auth_login(request, user)
                messages.success(request, f'¡Usuario {username} registrado correctamente!')
                return redirect('index')
            else:
                messages.error(request, 'Hubo un problema al iniciar sesión después del registro.')
                return redirect('login')
        else:
            messages.error(request, 'Hubo un problema con el formulario.')
            print(form.errors)  # Imprime los errores del formulario en la consola para depurar
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form,
    }
    return render(request, 'registration/registro.html', context)

def index(request):
    return render(request, 'beauty/index.html')

def nosotros(request):
    return render(request, 'beauty/nosotros.html')

def terminos(request):
    return render(request, 'beauty/terminosyCondiciones.html')

def privacidadpoliticas(request):
    return render(request, 'beauty/privacidad-politicas.html')

def blog(request):
    return render(request, 'beauty/blog.html')

def actitud(request):
    return render(request, 'beauty/blogs/actitud.html')

def cabello_afro(request):
    return render(request, 'beauty/blogs/cabelloAfro.html')

def cuidado_cabello(request):
    return render(request, 'beauty/blogs/cuidadoCabello.html')

def oficina(request):
    return render(request, 'beauty/blogs/oficina.html')

def primavera_verano(request):
    return render(request, 'beauty/blogs/primaveraVerano.html')

def skincare(request):
    return render(request, 'beauty/blogs/skinCare.html')

def resena(request):
    return render(request, 'beauty/reseña.html')
