from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):
    cantidad = forms.IntegerField(min_value=1, max_value=10, label="Cantidad de copias")
    
    class Meta:
        model = Pedido
        fields = ['comprador', 'correo', 'cantidad']
