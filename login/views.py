from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Region, Comuna, Usuario
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

#RENDERIZAR LOGIN.
def login(request):
    if request.method == 'POST':
        correo = request.POST.get('username')
        password = request.POST.get('password')

        try:
            usuario = Usuario.objects.get(correo=correo)  # Buscamos al usuario por correo
            if check_password(password, usuario.password):  # Verificamos la contraseña
                # Si la contraseña es correcta, redirigimos a una página de inicio o dashboard
                messages.success(request, 'Has iniciado sesión correctamente.')
                return redirect('/catalogo/')  # Redirige a la página de catalogo
            else:
                messages.error(request, 'Contraseña incorrecta.')
        except Usuario.DoesNotExist:
            messages.error(request, 'El usuario no existe.')

    return render(request, 'login.html')

# RENDERIZAR SIGNUP.
def signup(request):
    regiones = Region.objects.all()

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        region_id = request.POST.get('region')
        comuna_id = request.POST.get('comuna')
        direccion = request.POST.get('direccion')
        correo = request.POST.get('correo')
        password = request.POST.get('password')

        # Validación de usuario existente
        if Usuario.objects.filter(correo=correo).exists():
            messages.error(request, 'El correo ya está registrado.')
            return render(request, 'signup.html', {'regiones': regiones})

        region = Region.objects.get(id=region_id)
        comuna = Comuna.objects.get(id=comuna_id)

        usuario = Usuario.objects.create(
            nombre=nombre,
            apellido=apellido,
            region=region,
            comuna=comuna,
            direccion=direccion,
            correo=correo,
            password=make_password(password)  # <- ahora la contraseña está hasheada
        )

        messages.success(request, 'Usuario creado correctamente.')
        return redirect('login')

    return render(request, 'signup.html', {'regiones': regiones})


# CARGAR COMUNAS EN BASE AL TIPO DE REGIÓN.
def cargar_comunas(request):
    region_id = request.GET.get('region_id')
    comunas = Comuna.objects.filter(region_id=region_id).order_by('nombre')
    comuna_list = [{'id': c.id, 'nombre': c.nombre} for c in comunas]
    return JsonResponse(comuna_list, safe=False)
