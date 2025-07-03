from django.shortcuts import render, get_object_or_404, redirect
from .models import Mensaje
from .forms import MensajeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def inbox_view(request):
    mensajes = Mensaje.objects.filter(destinatario=request.user).order_by('-fecha_envio')
    return render(request, 'mensajes/inbox.html', {'mensajes': mensajes})

@login_required
def mensaje_detalle_view(request, pk):
    mensaje = get_object_or_404(Mensaje, pk=pk)
    if mensaje.destinatario != request.user:
        return redirect('inbox')
    mensaje.leido = True
    mensaje.save()
    return render(request, 'mensajes/detalle.html', {'mensaje': mensaje})

@login_required
def nuevo_mensaje_view(request):
    if request.method == "POST":
        form = MensajeForm(request.POST)
        if form.is_valid():
            nuevo = form.save(commit=False)
            nuevo.remitente = request.user
            nuevo.save()
            return redirect('inbox')
    else:
        form = MensajeForm()
    return render(request, 'mensajes/nuevo.html', {'form': form})
