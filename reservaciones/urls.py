from django.urls import path
from . import views

urlpatterns = [
    path('reservar/', views.reservar, name='reservar'),
    # Aquí puedes definir más URLs si lo necesitas
]

