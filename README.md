# 🏠 Origami - Aplicación Web Inmobiliaria

Proyecto final individual desarrollado en Django para el Playground Final Project. Origami es una aplicación web estilo blog con temática inmobiliaria, donde los usuarios pueden ver, publicar y gestionar propiedades, registrarse, iniciar sesión, editar su perfil y contactarse entre ellos mediante un sistema de mensajería.

## 🚀 Funcionalidades Principales

- ✅ Home con propiedades destacadas
- ✅ Página "Sobre nosotros" (`/about/`)
- ✅ Listado de propiedades (`/propiedades/`)
- ✅ Filtro por zona (Caballito, Belgrano, etc.)
- ✅ Detalle de propiedad al hacer clic en "Ver más"
- ✅ Registro e inicio de sesión de usuarios
- ✅ Vista de perfil con edición y cambio de contraseña
- ✅ Envío de mensajes entre usuarios
- ✅ Formulario de contacto (Nombre, Teléfono, Email, Comentario)
- ✅ Manejo de imágenes y campos personalizados
- ✅ Herencia de templates (`base.html`)
- ✅ Panel de administración para todos los modelos
- ✅ Uso de CBVs, mixins y decoradores

---

## 🛠️ Tecnologías Utilizadas

- Python 3.13
- Django 5.2.4
- SQLite
- Bootstrap 5
- HTML5 + CSS3
- CKEditor (para campos enriquecidos)
- Pillow (para gestión de imágenes)

---

## 📁 Estructura del Proyecto

```bash
proyecto_python/
├── myapp/
├── accounts/
├── mensajes/
├── media/
├── static/
├── templates/
├── db.sqlite3 (excluido)
├── manage.py

## Cómo correr
1. Cloná el repo
2. `pip install -r requirements.txt`
3. `python manage.py migrate`
4. `python manage.py runserver`

> No incluye `db.sqlite3` ni la carpeta `media/`
