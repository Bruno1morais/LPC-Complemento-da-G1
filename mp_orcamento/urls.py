from django.urls import path
from .views import *

urlpatterns = [
    path('orcamentos/', orcamentos_lista, name='orcamentos-lista'),
    path('orcamentos/estatisticas/', orcamentos_estatisticas, name='orcamentos-estatisticas'),
    path('clientes/',orcamentos_clientes,name='orcamentos-clientes'),
    path('clientes/estatisticas/',orcamentos_clientes_estatisticas,name='clientes-estatisticas'),
]
