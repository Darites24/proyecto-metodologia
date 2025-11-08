from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls', namespace='usuarios')),
    path('', RedirectView.as_view(pattern_name='usuarios:login', permanent=False)),
    path('conversor/', include('conversor.urls', namespace='conversor'))
]
