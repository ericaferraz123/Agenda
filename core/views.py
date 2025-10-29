from django.shortcuts import render, redirect
from .forms import CompromissoForm
from .models import Compromisso  # Supondo que tenha criado esse modelo

def index(request):
    if request.method == 'POST':
        form = CompromissoForm(request.POST)
        if form.is_valid():
            Compromisso.objects.create(
                titulo=form.cleaned_data['nome'],
                data_inicio=form.cleaned_data['horario'],
                data_fim=form.cleaned_data['horario']  # Ajuste conforme sua lógica
            )
            return redirect('index')  # Redireciona após salvar
    else:
        form = CompromissoForm()
    return render(request, 'core/index.html', {'form': form})
