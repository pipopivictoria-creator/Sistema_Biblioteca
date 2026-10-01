from django.shortcuts import render
from .models import emprestimo

def lista_emprestimos(request):
    emprestimos = emprestimo.objects.all()
    return render(request, 'emprestimos/lista.html', {
        'emprestimos': emprestimos
    })
