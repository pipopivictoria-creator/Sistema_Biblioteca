from django.db import models

class emprestimo(models.Model):
    livro = models.ForeignKey('livros.Livro', on_delete=models.CASCADE)
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
    data_emprestimo = models.DateTimeField(auto_now_add=True)
    data_devolucao = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.livro.titulo} - {self.usuario.nome}"