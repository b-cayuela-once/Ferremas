from django.urls import path
from . import views

urlpatterns = [
# PAGINA BASE DELEGADA DE URLS.PY PAGINA WEB.
    path('', views.index, name='index'),
]