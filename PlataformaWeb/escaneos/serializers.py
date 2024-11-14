# En serializers.py
from rest_framework import serializers
from .models import Caja

class CajaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caja
        fields = ['caja', 'sello1', 'sello2', 'codigo', 'cantidad']
