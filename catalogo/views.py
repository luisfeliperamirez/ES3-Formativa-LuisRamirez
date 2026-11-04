from django.shortcuts import render, get_object_or_404, redirect
from .models import Vinilo, Artista

def inicio(request):
    # Solo mostrar los que están en catálogo
    vinilos = Vinilo.objects.filter(en_catalogo=True)
    artistas = Artista.objects.all()

    # Búsqueda y Filtro
    q_titulo = request.GET.get('q', '')
    q_artista = request.GET.get('artista', '')

    if q_titulo:
        vinilos = vinilos.filter(titulo__icontains=q_titulo)
    if q_artista:
        vinilos = vinilos.filter(artista_id=q_artista)

    return render(request, 'catalogo/inicio.html', {
        'vinilos': vinilos,
        'artistas': artistas,
    })
