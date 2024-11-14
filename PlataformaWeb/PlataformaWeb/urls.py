# PlataformaWeb/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('escaneos.urls')),  # Incluye las URLs de la app escaneos
]
