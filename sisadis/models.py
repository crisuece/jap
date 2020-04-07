from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

class Aluno(models.Model):
    sige = models.CharField(max_length=15, primary_key=True)
    nome = models.CharField(max_length=255)
    turma = models.ForeignKey('Turma', on_delete=models.CASCADE)
    foto = models.ImageField()
    responsavel = models.CharField(max_length=20)
    fone_responsavel = models.CharField(max_length=13)
    observacoes = models.TextField()

    def __str__(self):
        return self.nome


class Turma(models.Model):
    nome = models.CharField(max_length=2)
    turno = models.CharField(max_length=5)
    sala = models.IntegerField()

    def __str__(self):
        return self.nome

class Ocorrencia(models.Model):
    aluno = models.ForeignKey('Aluno', on_delete=models.CASCADE)
    dt_ocorrencia = models.DateTimeField()
    dt_registro = models.DateTimeField()
    descricao = models.TextField()    
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.aluno
