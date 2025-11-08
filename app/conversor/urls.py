from django.urls import path
from . import views

app_name = 'conversor'

urlpatterns = [
    path('home/', views.home, name='home')
]
