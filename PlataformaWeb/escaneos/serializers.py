# En serializers.py
from rest_framework import serializers
from .models import RegistroCaja

class RegistroCajaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroCaja
        fields = ['caja', 'sello1', 'sello2', 'codigo', 'cantidad']
