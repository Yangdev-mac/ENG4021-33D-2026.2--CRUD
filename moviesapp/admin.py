from django.contrib import admin
from .models import Filme


@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'diretor', 'ano', 'assistido']
    search_fields = ['titulo', 'diretor']
