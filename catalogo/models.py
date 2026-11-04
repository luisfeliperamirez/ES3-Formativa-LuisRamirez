import uuid
from django.db import models

class Artista(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre del Artista")

    def __str__(self):
        return self.nombre

class Vinilo(models.Model):
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=150, verbose_name="Título del Álbum")
    anio = models.IntegerField(verbose_name="Año de Lanzamiento")
    caratula = models.ImageField(upload_to='caratulas/')
    precio = models.IntegerField(verbose_name="Precio (CLP)")
    en_catalogo = models.BooleanField(default=True, verbose_name="¿Está en catálogo?")

    def __str__(self):
        return f"{self.titulo} - {self.artista.nombre}"

class Pedido(models.Model):
    vinilo = models.ForeignKey(Vinilo, on_delete=models.CASCADE)
    comprador = models.CharField(max_length=100, verbose_name="Nombre del comprador")
    correo = models.EmailField()
    cantidad = models.IntegerField()
    fecha_compra = models.DateTimeField(auto_now_add=True)
    codigo = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return f"Pedido {self.codigo} - {self.comprador}"


