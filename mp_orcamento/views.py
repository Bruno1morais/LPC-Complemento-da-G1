from django.shortcuts import render
from .models import *

# Create your views here.
def orcamentos_lista(request):
    orcamentos = Orcamento.objects.all()
    return render(request, 'mp_orcamento/orcamentos.html', {'orcamentos': orcamentos})


def orcamentos_estatisticas(request):
    maior_custo = 0
    menor_custo = 999999999999
    orcamento_maior_custo = None
    orcamento_menor_custo = None
    orcamentos = Orcamento.objects.all()
    somatorio_custo_total = 0
    for orcamento in orcamentos:
        somatorio = 0
        for peca in Peca.objects.filter(orcamento=orcamento):
            somatorio += peca.custo_de_producao_ajustado()
        orcamento.custo_total = somatorio * 1.25
        somatorio_custo_total += orcamento.custo_total
        if orcamento.custo_total >= maior_custo:
            orcamento_maior_custo = orcamento
            maior_custo = orcamento.custo_total
        if orcamento.custo_total <= menor_custo:
            orcamento_menor_custo = orcamento
            menor_custo = orcamento.custo_total
    quantidade = Orcamento.objects.count() 
    media_custo_total = somatorio_custo_total / quantidade
    return render(request, 'mp_orcamento/estatisticas.html', 
        {'quantidade': quantidade, 
        'orcamento_maior_custo': orcamento_maior_custo,
        'orcamento_menor_custo': orcamento_menor_custo,
        'media_custo_total': media_custo_total
        })


def orcamentos_clientes(request):
    clientes = Cliente.objects.all().first()
    orcamentos = Orcamento.objects.filter(cliente=clientes)
    return render (request,'mp_orcamento/clientes.html',
    {'clientes': clientes,
    'orcamentos': orcamentos
    })
        

def orcamentos_clientes_estatisticas(request):
    clientes = Cliente.objects.all()
    maior_custo = 0
    menor_custo = 999999999999
    orcamento_maior_custo = None
    orcamento_menor_custo = None
    nome_maior = None
    nome_menor = None
    for cliente in clientes:
        somatorio = 0
        for orcamento in Orcamento.objects.filter(cliente=cliente):
            somatorio += orcamento.custo_total()
        orcamento_total = somatorio
        if orcamento_total >= maior_custo:
            orcamento_maior_custo = orcamento_total
            nome_maior = cliente.nome
            maior_custo = orcamento_total
        if orcamento_total <= menor_custo:
            orcamento_menor_custo = orcamento_total
            nome_menor = cliente.nome
            menor_custo = orcamento_total
    quantidade = Cliente.objects.count()
    return render(request, 'mp_orcamento/clientes_estatisticas.html',
    {'quantidade': quantidade,
    'orcamento_maior_custo': orcamento_maior_custo,
    'orcamento_menor_custo': orcamento_menor_custo,
    'nome_maior': nome_maior,
    'nome_menor': nome_menor
    })

        
