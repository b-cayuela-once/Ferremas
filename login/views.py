from django.shortcuts import render
from django.http import JsonResponse
from .models import Comuna

#RENDERIZAR LOGIN.
def login(request):
    return render(request, 'login.html')

#RENDERIZAR SIGNUP.
def signup(request):
    return render(request, 'signup.html')

# CARGAR COMUNAS EN BASE AL TIPO DE REGIÓN.
def cargar_comunas(request):
    region_id = request.GET.get('region_id')
    comunas = Comuna.objects.filter(region_id=region_id).order_by('nombre')
    comuna_list = [{'id': c.id, 'nombre': c.nombre} for c in comunas]
    return JsonResponse(comuna_list, safe=False)
