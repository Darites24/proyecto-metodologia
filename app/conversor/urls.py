from django.urls import path
from . import views

app_name = 'conversor'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('historial/', views.historial, name='historial'),
    path('api/codigos', views.codigos_api, name='codigos_api')
]
