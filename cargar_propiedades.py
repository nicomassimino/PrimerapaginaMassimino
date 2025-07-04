import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_python.settings')
django.setup()

from django.core.files import File
from myapp.models import Propiedad

ruta = os.getcwd()

datos = [
    {
        "titulo": "Departamento moderno en Palermo",
        "descripcion": "Excelente unidad de 2 ambientes con balcón y vista abierta.",
        "precio": 120000,
        "metros_cuadrados": 45,
        "nombre_archivo": "palermo.jpg"
    },
    {
        "titulo": "Casa con patio en Caballito",
        "descripcion": "Casa antigua reciclada con 3 dormitorios y gran patio.",
        "precio": 220000,
        "metros_cuadrados": 120,
        "nombre_archivo": "caballito.jpg"
    },
    {
        "titulo": "PH en Almagro con terraza",
        "descripcion": "PH al frente con terraza privada, ideal para familia.",
        "precio": 180000,
        "metros_cuadrados": 90,
        "nombre_archivo": "almagro.jpg"
    },
    {
        "titulo": "Monoambiente en Recoleta",
        "descripcion": "Ambiente amplio con cocina integrada, excelente zona.",
        "precio": 95000,
        "metros_cuadrados": 30,
        "nombre_archivo": "recoleta.jpg"
    }
]

Propiedad.objects.all().delete()

for dato in datos:
    propiedad = Propiedad(
        titulo=dato["titulo"],
        descripcion=dato["descripcion"],
        precio=dato["precio"],
        metros_cuadrados=dato["metros_cuadrados"]
    )
    with open(os.path.join(ruta, dato["nombre_archivo"]), 'rb') as img_file:
        propiedad.imagen.save(dato["nombre_archivo"], File(img_file), save=True)

print("✔️ Propiedades cargadas correctamente.")
