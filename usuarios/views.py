from django.http import HttpResponse

def listar_usuarios(request):
    return HttpResponse("Lista de usuários da biblioteca")
