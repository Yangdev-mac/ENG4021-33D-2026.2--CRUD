from django.db import models


class Filme(models.Model):
    titulo = models.CharField('Título', max_length=120)
    diretor = models.CharField('Diretor', max_length=100)
    genero = models.CharField('Gênero', max_length=60)
    ano = models.PositiveIntegerField('Ano de lançamento')
    assistido = models.BooleanField('Já assisti', default=False)

    def __str__(self):
        return self.titulo
