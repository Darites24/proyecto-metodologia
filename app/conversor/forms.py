from django import forms

class ConversionForm(forms.Form):
    moneda_base = forms.CharField(max_length=3)
    moneda_destino = forms.CharField(max_length=3)
    cantidad = forms.DecimalField(max_digits=30, decimal_places=6)