from django.test import TestCase
from django.urls import reverse
from .models import Filme


class FilmesTestes(TestCase):
    def criar_filme(self):
        return Filme.objects.create(
            titulo='Interestelar', diretor='Christopher Nolan',
            genero='Ficção científica', ano=2014,
        )

    def test_cadastrar(self):
        resposta = self.client.post(reverse('inicio'), {
            'titulo': 'Matrix', 'diretor': 'Lana Wachowski',
            'genero': 'Ação', 'ano': 1999,
        })
        self.assertEqual(resposta.status_code, 302)
        self.assertTrue(Filme.objects.filter(titulo='Matrix').exists())

    def test_listar(self):
        self.criar_filme()
        resposta = self.client.get(reverse('inicio'))
        self.assertContains(resposta, 'Interestelar')

    def test_editar(self):
        filme = self.criar_filme()
        resposta = self.client.post(reverse('editar', args=[filme.pk]), {
            'titulo': 'Interestelar 2', 'diretor': 'Christopher Nolan',
            'genero': 'Ficção científica', 'ano': 2014, 'assistido': 'on',
        })
        filme.refresh_from_db()
        self.assertEqual(resposta.status_code, 302)
        self.assertEqual(filme.titulo, 'Interestelar 2')
        self.assertTrue(filme.assistido)

    def test_excluir_somente_por_post(self):
        filme = self.criar_filme()
        endereco = reverse('excluir', args=[filme.pk])
        self.client.get(endereco)
        self.assertTrue(Filme.objects.filter(pk=filme.pk).exists())
        self.client.post(endereco)
        self.assertFalse(Filme.objects.filter(pk=filme.pk).exists())

    def test_busca_local(self):
        self.criar_filme()
        Filme.objects.create(titulo='Titanic', diretor='James Cameron', genero='Drama', ano=1997)
        resposta = self.client.get(reverse('inicio'), {'busca': 'Inter'})
        self.assertContains(resposta, 'Interestelar')
        self.assertNotContains(resposta, 'Titanic')
