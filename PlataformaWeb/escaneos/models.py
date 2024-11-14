from django.db import models

class Caja(models.Model):
    caja = models.CharField(max_length=50)
    sello1 = models.CharField(max_length=20)
    sello2 = models.CharField(max_length=20)
    codigo = models.CharField(max_length=50)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"Caja {self.caja} - {self.codigo}"
