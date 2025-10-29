from django import forms
from .models import Agenda

class FormAgenda(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = ['nome', 'horario']
        widgets = {"horario": forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y/%m/%d %H:%M' )}