from django.shortcuts import render, redirect
from .forms import FormAgenda
from .models import Agenda

def index(request):
    return render(request, 'core/index.html')

def agendar_compromisso(request):
    if request.method == 'POST':
        form = FormAgenda(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "core/sucesso.html")
    else:
        form = Agenda.objects.all()
        print(form)
    return render(request, "core/index.html", {"form":form})
