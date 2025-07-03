from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('accounts/', include('accounts.urls')),
    path('mensajes/', include('mensajes.urls')),
    path('about/', TemplateView.as_view(template_name="about.html"), name="about"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
