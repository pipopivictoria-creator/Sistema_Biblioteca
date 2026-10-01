from django.http import HttpResponse

def lista_livros(request):
    return HttpResponse("Lista de livros da biblioteca")

