from django.contrib import admin
from .models import Artista, Vinilo, Pedido

@admin.register(Artista)
class ArtistaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(Vinilo)
class ViniloAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'artista', 'precio_clp', 'en_catalogo')
    list_filter = ('artista', 'en_catalogo')
    search_fields = ('titulo',)

    def precio_clp(self, obj):
        return f"${obj.precio:,}".replace(',', '.')
    precio_clp.short_description = 'Precio'

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'vinilo', 'comprador', 'cantidad', 'fecha_compra')
    list_filter = ('vinilo',)
