from django.contrib import admin
from .models import Artista, Album, Compra

admin.site.register(Artista)

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'artista', 'precio_clp', 'en_stock') 
    list_filter = ('artista', 'en_stock') 
    search_fields = ('titulo',) 

    def precio_clp(self, obj):
        return f"${obj.precio:,}".replace(',', '.') 
    precio_clp.short_description = 'Precio'

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'album', 'nombre_comprador', 'cantidad', 'fecha_compra') 
    list_filter = ('album',) 