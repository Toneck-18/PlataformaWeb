# escaneos/urls.py
from django.urls import path
from . import views  # Importamos las vistas desde el archivo views.py

urlpatterns = [
    path('api/escaneo/', views.recibir_escaneo, name='recibir_escaneo'),  # Ruta para la API de escaneo
]
