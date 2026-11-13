from django import forms
from .models import Filme


class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['titulo', 'diretor', 'genero', 'ano', 'assistido']
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Ex.: Interestelar'}),
            'diretor': forms.TextInput(attrs={'placeholder': 'Ex.: Christopher Nolan'}),
            'genero': forms.TextInput(attrs={'placeholder': 'Ex.: Ficção científica'}),
            'ano': forms.NumberInput(attrs={'min': 1888, 'max': 2100}),
        }
