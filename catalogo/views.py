from django.shortcuts import render, get_object_or_404, redirect
from .models import Vinilo, Artista
from .forms import PedidoForm
from .models import Pedido

def inicio(request):
    vinilos = Vinilo.objects.filter(en_catalogo=True)
    artistas = Artista.objects.all()

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

def detalle_vinilo(request, id):
    vinilo = get_object_or_404(Vinilo, id=id, en_catalogo=True)
    
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.vinilo = vinilo
            pedido.save()
            return redirect('ticket_pedido', uuid=pedido.codigo)
    else:
        form = PedidoForm()

    return render(request, 'catalogo/detalle.html', {'vinilo': vinilo, 'form': form})

def ticket_pedido(request, uuid):
    pedido = get_object_or_404(Pedido, codigo=uuid)
    total = pedido.cantidad * pedido.vinilo.precio
    total_clp = f"${total:,}".replace(',', '.')
    
    return render(request, 'catalogo/ticket.html', {
        'pedido': pedido, 
        'total_clp': total_clp
    })
