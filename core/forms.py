from django import forms

class CompromissoForm(forms.Form):
    nome = forms.CharField(label='Compromisso', max_length=200)
    horario = forms.DateTimeField(label='Horário')
