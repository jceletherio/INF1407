from django.db import models
from django.db.models.fields import URLField

# Create your models here.

class Mylist(models.Model):
    nome = models.CharField(max_length=150)
    myprefeito = models.IntegerField()

    def __str__(self):
        return self.nome

class Estado(models.Model):
    nome = models.CharField(max_length=200)
    UF = models.CharField(max_length=2)

    def __str__(self):
        return self.nome

class Municipio(models.Model):
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Prefeito(models.Model):
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    sigla = models.IntegerField()
    partido = models.CharField(max_length=20)
    plano = models.CharField(max_length=400)

    def __str__(self):
        return self.nome