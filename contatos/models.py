from email.policy import default
from pickle import TRUE
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length = 100)

class Contato(models.Model):
    nome = models.CharField(max_length = 30)
    sobrenome = models.CharField(max_length = 70, blank = True)
    telefone = models.CharField(max_length = 12)
    email = models.CharField(max_length = 60, blank = True)
    data_criação = models.DateTimeField(default = timezone.now)
    descricao = models.TextField(blank = True)
    categoria = models.ForeignKey(Categoria, on_delete = models.DO_NOTHING)



