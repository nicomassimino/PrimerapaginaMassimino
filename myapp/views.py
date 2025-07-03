from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Propiedad
from .forms import PropiedadForm

class ListaPropiedadesView(ListView):
    model = Propiedad
    template_name = "myapp/propiedades/lista.html"
    context_object_name = "propiedades"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not context['propiedades']:
            context['mensaje'] = "No hay propiedades aún."
        return context

class DetallePropiedadView(DetailView):
    model = Propiedad
    template_name = "myapp/propiedades/detalle.html"
    context_object_name = "propiedad"

class CrearPropiedadView(LoginRequiredMixin, CreateView):
    model = Propiedad
    form_class = PropiedadForm
    template_name = "myapp/propiedades/crear.html"
    success_url = reverse_lazy("propiedades_lista")

class EditarPropiedadView(LoginRequiredMixin, UpdateView):
    model = Propiedad
    form_class = PropiedadForm
    template_name = "myapp/propiedades/editar.html"
    success_url = reverse_lazy("propiedades_lista")

class EliminarPropiedadView(LoginRequiredMixin, DeleteView):
    model = Propiedad
    template_name = "myapp/propiedades/eliminar.html"
    success_url = reverse_lazy("propiedades_lista")
