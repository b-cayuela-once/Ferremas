from django.urls import path
from . import views

urlpatterns = [
# PAGINA BASE DELEGADA DE URLS.PY PAGINA WEB.
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('cargar_comunas/', views.cargar_comunas, name='cargar_comunas'),
]