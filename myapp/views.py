from django.shortcuts import render, get_object_or_404
from .models import Propiedad
from .forms import MensajeContactoForm
from django.contrib import messages
from django.shortcuts import redirect

def home(request):
    propiedades = Propiedad.objects.all()
    return render(request, 'myapp/index.html', {'propiedades': propiedades})

def about(request):
    return render(request, 'myapp/about.html')

def propiedades_lista(request):
    propiedades = Propiedad.objects.all()
    return render(request, 'myapp/propiedades_lista.html', {'propiedades': propiedades})

def propiedad_detalle(request, id):
    propiedad = get_object_or_404(Propiedad, id=id)
    return render(request, 'myapp/propiedad_detalle.html', {'propiedad': propiedad})

def propiedades_lista(request):
    zona = request.GET.get('zona', '')  # Obtener zona del filtro
    propiedades = Propiedad.objects.all()

    if zona:
        propiedades = propiedades.filter(titulo__icontains=zona)

    # Obtener zonas únicas desde los títulos de propiedades
    zonas_unicas = set()
    for propiedad in Propiedad.objects.all():
        titulo = propiedad.titulo.lower()
        for z in ["caballito", "almagro", "belgrano", "recoleta", "palermo", "boedo"]:
            if z in titulo:
                zonas_unicas.add(z.capitalize())

    zonas = sorted(list(zonas_unicas))

    return render(request, 'myapp/propiedades_lista.html', {
        'propiedades': propiedades,
        'zonas': zonas,
        'zona_seleccionada': zona
    })

def contacto(request):
    if request.method == 'POST':
        form = MensajeContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu mensaje ha sido enviado correctamente.')
            return redirect('contacto')
    else:
        form = MensajeContactoForm()
    return render(request, 'myapp/contacto.html', {'form': form})