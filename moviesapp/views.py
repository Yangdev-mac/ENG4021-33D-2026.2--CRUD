import os
import requests
from django.shortcuts import get_object_or_404, redirect, render
from .forms import FilmeForm
from .models import Filme


def inicio(request):
    # CREATE: salva um novo filme enviado pelo formulário.
    formulario = FilmeForm(request.POST or None)
    if request.method == 'POST' and formulario.is_valid():
        formulario.save()
        return redirect('inicio')

    # READ: mostra os filmes cadastrados, com filtro por título.
    busca = request.GET.get('busca', '').strip()
    filmes = Filme.objects.all().order_by('-id')
    if busca:
        filmes = filmes.filter(titulo__icontains=busca)

    # Busca externa opcional na OMDb (não interfere no CRUD).
    termo = request.GET.get('omdb', '').strip()
    encontrados = []
    aviso = ''
    if termo:
        chave = os.getenv('OMDB_API_KEY', '')
        if not chave:
            aviso = 'Para buscar na OMDb, configure sua chave OMDB_API_KEY.'
        else:
            try:
                resposta = requests.get(
                    'https://www.omdbapi.com/',
                    params={'apikey': chave, 's': termo, 'type': 'movie'},
                    timeout=8,
                )
                resposta.raise_for_status()
                dados = resposta.json()
                if dados.get('Response') == 'True':
                    encontrados = dados.get('Search', [])[:8]
                else:
                    aviso = 'Nenhum resultado encontrado na OMDb.'
            except (requests.RequestException, ValueError):
                aviso = 'Não foi possível consultar a OMDb agora.'

    contexto = {
        'formulario': formulario,
        'filmes': filmes,
        'busca': busca,
        'total': Filme.objects.count(),
        'assistidos': Filme.objects.filter(assistido=True).count(),
        'termo': termo,
        'encontrados': encontrados,
        'aviso': aviso,
    }
    return render(request, 'index.html', contexto)


def editar(request, pk):
    # UPDATE: abre um filme existente e salva as alterações.
    filme = get_object_or_404(Filme, pk=pk)
    formulario = FilmeForm(request.POST or None, instance=filme)
    if request.method == 'POST' and formulario.is_valid():
        formulario.save()
        return redirect('inicio')
    return render(request, 'edit_movie.html', {'formulario': formulario, 'filme': filme})


def excluir(request, pk):
    # DELETE: só exclui quando o botão envia um POST.
    if request.method == 'POST':
        filme = get_object_or_404(Filme, pk=pk)
        filme.delete()
    return redirect('inicio')
