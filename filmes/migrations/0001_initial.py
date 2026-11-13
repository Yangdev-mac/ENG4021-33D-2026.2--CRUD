from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=120, verbose_name='Título')),
                ('diretor', models.CharField(max_length=100, verbose_name='Diretor')),
                ('genero', models.CharField(max_length=60, verbose_name='Gênero')),
                ('ano', models.PositiveIntegerField(verbose_name='Ano de lançamento')),
                ('assistido', models.BooleanField(default=False, verbose_name='Já assisti')),
            ],
        ),
    ]
