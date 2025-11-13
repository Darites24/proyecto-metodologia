from django.contrib import admin
from .models import Conversion

@admin.register(Conversion)
class ConversionAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'moneda_base', 'moneda_destino', 'cantidad', 'resultado', 'fecha')
    list_filter = ('moneda_base', 'moneda_destino', 'fecha')

