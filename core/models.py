from django.db import models

class Agenda(models.Model):
    nome = models.CharField(max_length=100)
    horario = models.DateTimeField()

    def __str__(self):
        return f"{self.nome} em {self.horario.strftime('%d/%m/%Y %H:%M')}"
