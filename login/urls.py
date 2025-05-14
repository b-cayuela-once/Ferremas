from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
# PAGINA BASE DELEGADA DE URLS.PY PAGINA WEB.
    path('', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('cargar_comunas/', views.cargar_comunas, name='cargar_comunas'),
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),  # Redirige a login después de cerrar sesión
]