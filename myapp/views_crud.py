from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Propiedad
from .forms import PropiedadForm

@login_required
def crear_propiedad(request):
    if request.method == "POST":
        form = PropiedadForm(request.POST, request.FILES)
        if form.is_valid():
            propiedad = form.save(commit=False)
            propiedad.duenio = request.user
            propiedad.save()
            return redirect('propiedades_lista')
    else:
        form = PropiedadForm()
    return render(request, 'myapp/crear_propiedad.html', {'form': form})

@login_required
def editar_propiedad(request, pk):
    propiedad = get_object_or_404(Propiedad, pk=pk, duenio=request.user)
    if request.method == "POST":
        form = PropiedadForm(request.POST, request.FILES, instance=propiedad)
        if form.is_valid():
            form.save()
            return redirect('propiedades_lista')
    else:
        form = PropiedadForm(instance=propiedad)
    return render(request, 'myapp/editar_propiedad.html', {'form': form})

@login_required
def eliminar_propiedad(request, pk):
    propiedad = get_object_or_404(Propiedad, pk=pk, duenio=request.user)
    if request.method == "POST":
        propiedad.delete()
        return redirect('propiedades_lista')
    return render(request, 'myapp/eliminar_propiedad.html', {'propiedad': propiedad})