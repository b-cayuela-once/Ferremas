from django.db import models

# REGION 
class Region(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
# COMUNA
class Comuna(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

# TIPO DE USUARIO.   
class TipoUsuario(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre
# USUARIO.    
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    comuna = models.ForeignKey(Comuna, on_delete=models.SET_NULL, null=True)
    direccion = models.CharField(max_length=255)
    correo = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Aquí puedes aplicar hashing si deseas.

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.correo}"
