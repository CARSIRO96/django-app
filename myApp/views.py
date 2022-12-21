from django.shortcuts import render, redirect
from django.contrib.auth import login
# from myApp.form import UserCreationForm
from django.urls import reverse

from rest_framework.decorators import api_view

# Create your views here.
def home(request):
    return render(
        request,
        'home.html',
        context={
            'prueba_invocar_variable_en_html': 1000, 
                }
    )

@api_view(['GET', 'POST'])
def formulario(request):
    if request.method == 'GET':
        return render(
            request, 
            'formulario.html'
        )
    if request.method == 'POST':
        data = request.data
        respuesta_al_form='FORMULARIO ENVIADO'
        error='Por favor, seleccione un Categoría'
        # if 'cat' in data['url']:
        #     error='Por favor, seleccione un Categoría'
        return render( request, 'formulario.html', 
                    context={
                        'urls': data['url'],
                        'data':data,
                        'respuesta':respuesta_al_form,
                        'error': error,
                        'tipo': str(type(data['url']))
                        })

            
        
    
    