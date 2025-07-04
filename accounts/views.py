from .forms import UserRegisterForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, PerfilForm
from .models import Perfil

def signup_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('propiedades_lista')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('propiedades_lista')
        else:
            messages.error(request, "Credenciales incorrectas. Intenta de nuevo.")
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def perfil_view(request):
    perfil = request.user.perfil
    return render(request, 'accounts/perfil.html', {'perfil': perfil})


@login_required
def editar_perfil_view(request):
    perfil = request.user.perfil
    if request.method == "POST":
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil actualizado correctamente.")
            return redirect('perfil')
        else:
            messages.error(request, "Revisa los errores en el formulario.")
    else:
        form = PerfilForm(instance=perfil)
    return render(request, 'accounts/editar_perfil.html', {'form': form})


@login_required
def perfil_view(request):
    return render(request, 'accounts/perfil.html', {'user': request.user})


def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/registro.html', {'form': form})