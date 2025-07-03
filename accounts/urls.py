from django.urls import path
from .views import signup_view, login_view, logout_view, perfil_view, editar_perfil_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('perfil/', perfil_view, name='perfil'),
    path('editar/', editar_perfil_view, name='editar_perfil'),
    path('cambiar-password/', auth_views.PasswordChangeView.as_view(template_name='accounts/cambiar_password.html'), name='password_change'),
    path('password-ok/', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_ok.html'), name='password_change_done'),
]
