from django.contrib import admin
# SE IMPORTAN REGION, COMUNA Y TIPOUSUARIO DE MODELS.PY.
from .models import Region, Comuna, TipoUsuario

admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(TipoUsuario)
