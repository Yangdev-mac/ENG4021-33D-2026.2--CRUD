# CineLog — CRUD de Filmes (Django)

Um projeto de catálogo de filmes feito com Django. Permite **cadastrar, listar, editar e excluir** filmes no banco SQLite. Também permite filtrar os filmes pelo nome e, opcionalmente, buscar títulos na OMDb.

## Como executar no Mac / Linux

Abra o terminal dentro da pasta do projeto e rode:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Acesse **http://127.0.0.1:8000/**.

## Como executar no Windows

No terminal (PowerShell), dentro da pasta do projeto:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Busca de filmes na OMDb (opcional)

O CRUD funciona sem API. Para usar a pesquisa externa, crie uma chave gratuita em https://www.omdbapi.com/apikey.aspx e defina a variável de ambiente antes de iniciar o servidor:

**Mac / Linux:**
```bash
export OMDB_API_KEY="sua_chave"
python manage.py runserver
```

**PowerShell:**
```powershell
$env:OMDB_API_KEY="sua_chave"
python manage.py runserver
```

Não envie uma chave real ao GitHub.

## O que cada arquivo faz

- `filmes/models.py`: define os dados de cada filme (título, diretor, gênero, ano e assistido).
- `filmes/forms.py`: formulário para cadastrar ou editar um filme.
- `filmes/views.py`: funções com as operações de CRUD e a busca opcional.
- `filmes/urls.py`: caminhos das páginas e ações.
- `filmes/templates/filmes/`: telas em HTML.
- `filmes/static/filmes/style.css`: aparência do site.
- `filmes/tests.py`: testes simples para criar, listar, editar, excluir e pesquisar.
- `cinecontrole/settings.py`: configurações do projeto e banco SQLite.

## O CRUD, explicado de forma fácil

1. **Create (Cadastrar)**: o formulário envia `POST`, Django valida e `formulario.save()` grava no banco.
2. **Read (Ler)**: `Filme.objects.all()` busca os filmes já cadastrados para exibir na tela.
3. **Update (Editar)**: selecionamos o filme pelo ID e usamos o mesmo formulário com `instance=filme` para salvar as mudanças.
4. **Delete (Excluir)**: ao confirmar a exclusão, `filme.delete()` remove o registro; o servidor exige um envio `POST`.

## Testar

```bash
python manage.py test
```

> Projeto acadêmico para execução local. A chave secreta padrão e o modo DEBUG devem ser alterados antes de publicar um servidor na internet.
