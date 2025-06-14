from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('autor/', views.formulario_autor, name='form_autor'),
    path('categoria/', views.formulario_categoria, name='form_categoria'),
    path('post/', views.formulario_post, name='form_post'),
    path('buscar/', views.buscar_post, name='buscar_post'),
]
