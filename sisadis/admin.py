from django.contrib import admin
from .models import Aluno, Turma, Ocorrencia

# Register your models here.
admin.site.register(Aluno)
admin.site.register(Turma)
admin.site.register(Ocorrencia)