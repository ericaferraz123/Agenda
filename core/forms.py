from django import forms
from .models import Compromisso

class CompromissoForm(forms.ModelForm):
    class Meta:
        model = Compromisso
        fields = ['titulo', 'descricao', 'data_inicio', 'data_fim']
