from django import forms
from .models import Propiedad
from .models import MensajeContacto

class PropiedadForm(forms.ModelForm):
    class Meta:
        model = Propiedad
        fields = ['titulo', 'descripcion', 'imagen']


class MensajeContactoForm(forms.ModelForm):
    class Meta:
        model = MensajeContacto
        fields = ['nombre', 'telefono', 'correo', 'comentario']
        widgets = {
            'comentario': forms.Textarea(attrs={'rows': 4}),
        }