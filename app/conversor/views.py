from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests
from django.conf import settings
from .models import Conversion
from .forms import ConversionForm
from django.http import JsonResponse
from django.core.cache import cache
from decimal import Decimal

CACHE_TTL = 24 * 3600

@login_required
def home(request):
    resultado = None
    form = ConversionForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        base = form.cleaned_data['moneda_base']
        destino = form.cleaned_data['moneda_destino']
        cantidad = form.cleaned_data['cantidad']

        try:
            url = f"https://v6.exchangerate-api.com/v6/{settings.API_KEY}/pair/{base}/{destino}/{cantidad}"
            resp = requests.get(url, timeout=5)
            resp.raise_for_status()
            data = resp.json()

            valor_conversion = data.get('conversion_result')
            if valor_conversion is None:
                rate = data.get('conversion_rate')
                if rate is None:
                    raise ValueError("Respuesta inválida de la API")
                valor_conversion = Decimal(str(rate)) * Decimal(str(cantidad))
            else:
                valor_conversion = Decimal(str(valor_conversion))

            Conversion.objects.create(
                usuario=request.user,
                moneda_base=base,
                moneda_destino=destino,
                cantidad=cantidad,
                resultado=valor_conversion
            )
            resultado = valor_conversion

        except (requests.RequestException, ValueError) as e:
            form.add_error(None, f"Error al convertir: {e}")

    return render(request, 'conversor/home.html', {"form": form, "resultado": resultado})



@login_required
def historial(request):
    conversiones = Conversion.objects.filter(usuario=request.user).order_by('-fecha')
    return render(request, "conversor/historial.html", {"conversiones": conversiones})

@login_required
def codigos_api(request):
    codigos = cache.get('supported_codes')
    if not codigos:
        url = f"https://v6.exchangerate-api.com/v6/{settings.API_KEY}/codes"
        try:
            res = requests.get(url, timeout=5)
            res.raise_for_status()
            codigos = res.json().get('supported_codes', [])
            cache.set('supported_codes', codigos, CACHE_TTL)
        except requests.RequestException:
            codigos = []
    return JsonResponse({"supported_codes": codigos})