from django.contrib import admin
# SE IMPORTAN REGION, COMUNA Y TIPOUSUARIO DE MODELS.PY.
from .models import Region, Comuna, TipoUsuario, Usuario

admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(TipoUsuario)
admin.site.register(Usuario)
