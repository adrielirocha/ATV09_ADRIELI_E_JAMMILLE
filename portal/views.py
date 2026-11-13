# portal/views.py
from django.shortcuts import render, get_object_or_404
from .models import Conteudo

def index(request):
    conteudo = Conteudo.objects.filter(slug='inicio', ativo=True).first()
    return render(request, 'portal/index.html', {'conteudo': conteudo})

def exibir_conteudo(request, slug):
    
    conteudo = get_object_or_404(Conteudo, slug=slug, ativo=True)
    return render(request, 'portal/conteudo.html', {'conteudo': conteudo})
