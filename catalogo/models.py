import uuid
from django.db import models

class Artista(models.Model):
    nombre = models.CharField(max_length=100, unique=True) 

    def __str__(self):
        return self.nombre

class Album(models.Model):
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE) 
    titulo = models.CharField(max_length=150)
    caratula = models.ImageField(upload_to='caratulas/') 
    precio = models.IntegerField() 
    en_stock = models.BooleanField(default=True) 
    canciones = models.IntegerField(default=1) 
    lanzamiento = models.DateField() 

    def __str__(self):
        return self.titulo

class Compra(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE) 
    codigo = models.UUIDField(default=uuid.uuid4, editable=False, unique=True) 
    nombre_comprador = models.CharField(max_length=100)
    correo = models.EmailField()
    cantidad = models.IntegerField()
    fecha_compra = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.codigo} - {self.nombre_comprador}"