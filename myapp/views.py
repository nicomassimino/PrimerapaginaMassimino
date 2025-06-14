from django.shortcuts import render
from .forms import AutorForm, CategoriaForm, PostForm, BusquedaPostForm
from .models import Post

def index(request):
    return render(request, 'myapp/index.html')

def formulario_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AutorForm()
    return render(request, 'myapp/formulario.html', {'form': form, 'titulo': 'Formulario Autor'})

def formulario_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CategoriaForm()
    return render(request, 'myapp/formulario.html', {'form': form, 'titulo': 'Formulario Categoría'})

def formulario_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()
    return render(request, 'myapp/formulario.html', {'form': form, 'titulo': 'Formulario Post'})

def buscar_post(request):
    resultado = None
    if request.method == 'POST':
        form = BusquedaPostForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            resultado = Post.objects.filter(titulo__icontains=titulo)
    else:
        form = BusquedaPostForm()
    return render(request, 'myapp/buscar.html', {'form': form, 'resultado': resultado})
