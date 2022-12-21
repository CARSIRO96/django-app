from os import name
from django.conf.urls import include
from django.urls.conf import path

from myApp import views

urlpatterns = [
    path('', views.formulario, name='formulario'),
    # path('home', views.home, name='home'),
    # path('formulario_respuesta', views.formulario, name='formulario_respuesta'),
]

