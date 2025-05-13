import json
import os
import django

# Configurar entorno Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'paginaweb.settings')  # Cambia si tu proyecto se llama distinto
django.setup()

from login.models import Region, Comuna, TipoUsuario

def cargar_regiones_y_comunas():
    with open('data/regiones_comunas.json', encoding='utf-8') as archivo:
        data = json.load(archivo)

        for item in data:
            region_nombre = item['region']
            region, _ = Region.objects.get_or_create(nombre=region_nombre)

            for comuna_nombre in item['comunas']:
                Comuna.objects.get_or_create(nombre=comuna_nombre, region=region)

    print("✅ Regiones y comunas cargadas correctamente.")

def cargar_tipos_usuario():
    with open('data/tipos_usuario.json', encoding='utf-8') as archivo:
        tipos = json.load(archivo)

        for tipo in tipos:
            TipoUsuario.objects.get_or_create(nombre=tipo['nombre'])

    print("✅ Tipos de usuario cargados correctamente.")


if __name__ == "__main__":
    cargar_regiones_y_comunas()
    cargar_tipos_usuario()
