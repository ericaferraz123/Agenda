from django.urls import path
from core import views

urlpatterns = [
    path('', views.agendar_compromisso, name='index'),
    path('/sucesso', views.agendar_compromisso, name='sucesso')
]
