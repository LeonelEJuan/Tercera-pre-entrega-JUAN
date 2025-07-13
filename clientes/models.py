from django.db import models

class Cliente(models.Model):
    nombre_usuario = models.CharField(max_length=100)
    email = models.EmailField()
    edad = models.IntegerField()

class Perfil(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    bio = models.TextField()
    fecha_registro = models.DateField(auto_now_add=True)

class Suscripcion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50)
    activa = models.BooleanField(default=True)
