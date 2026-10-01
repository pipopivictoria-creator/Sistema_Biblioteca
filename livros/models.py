from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    data_publicacao = models.DateField()
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
