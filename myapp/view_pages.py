from django.views.generic import ListView, DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Propiedad

class PageListView(ListView):
    model = Propiedad
    template_name = 'myapp/pages_list.html'
    context_object_name = 'propiedades'

class PageDetailView(DetailView):
    model = Propiedad
    template_name = 'myapp/pages_detail.html'
    context_object_name = 'propiedad'