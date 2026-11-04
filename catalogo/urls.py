from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('vinilo/<int:id>/', views.detalle_vinilo, name='detalle_vinilo'),
    path('ticket/<uuid:uuid>/', views.ticket_pedido, name='ticket_pedido'),
]
