from django.urls import path
from . import views
from .views import inbox_view, mensaje_detalle_view, nuevo_mensaje_view

app_name = 'mensajes'

urlpatterns = [
    path('', inbox_view, name='inbox'),
    path('nuevo/', nuevo_mensaje_view, name='nuevo'),
    path('<int:pk>/', mensaje_detalle_view, name='detalle'),
    path('', views.inbox, name='mensajes_inbox'),
    path('', views.inbox, name='inbox'),
]

