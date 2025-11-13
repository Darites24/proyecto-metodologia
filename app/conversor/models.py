from django.db import models
from django.conf import settings

class Conversion(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    moneda_base = models.CharField(max_length=3)
    moneda_destino = models.CharField(max_length=3)
    cantidad = models.DecimalField(max_digits=30, decimal_places=6)
    resultado = models.DecimalField(max_digits=30, decimal_places=6)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} {self.cantidad} {self.moneda_base}->{self.moneda_destino}" 