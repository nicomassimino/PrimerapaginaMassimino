from django.urls import path
from .views import signup_view, login_view, logout_view, perfil_view, editar_perfil_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('signup/', signup_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('perfil/', perfil_view, name='perfil'),
    path('perfil/editar/', editar_perfil_view, name='editar_perfil'),
]
