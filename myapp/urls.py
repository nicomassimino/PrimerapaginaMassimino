from django.urls import path, include
from . import views
from .views_crud import crear_propiedad, editar_propiedad, eliminar_propiedad
from .views import contacto

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('propiedades/', views.propiedades_lista, name='propiedades_lista'),
    path('propiedades/<int:id>/', views.propiedad_detalle, name='propiedad_detalle'),
    path('crear/', crear_propiedad, name='crear_propiedad'),
    path('editar/<int:pk>/', editar_propiedad, name='editar_propiedad'),
    path('eliminar/<int:pk>/', eliminar_propiedad, name='eliminar_propiedad'),
    path('mensajes/', include('mensajes.urls')),
    path('contacto/', contacto, name='contacto'),
]

