from django.urls import path
from . import views

urlpatterns = [
    # path(ruta y/o nombre en la ruta, vista, nombre)
    # path('', views.index, name='index'),
    path('', views.menu, name='menu'),
]