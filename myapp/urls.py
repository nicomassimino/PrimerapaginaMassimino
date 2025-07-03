from .views import dashboard
from django.urls import path
from .views import (
    ListaPropiedadesView,
    DetallePropiedadView,
    CrearPropiedadView,
    EditarPropiedadView,
    EliminarPropiedadView
)

urlpatterns = [
    path('', ListaPropiedadesView.as_view(), name='propiedades_lista'),
    path('<int:pk>/', DetallePropiedadView.as_view(), name='propiedad_detalle'),
    path('crear/', CrearPropiedadView.as_view(), name='propiedad_crear'),
    path('editar/<int:pk>/', EditarPropiedadView.as_view(), name='propiedad_editar'),
    path('eliminar/<int:pk>/', EliminarPropiedadView.as_view(), name='propiedad_eliminar'),
    path('dashboard/', dashboard, name='dashboard'),
]
