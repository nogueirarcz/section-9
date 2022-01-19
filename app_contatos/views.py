from django.shortcuts import render
from .models import Contato


def index(request):

    contatos = Contato.objects.all()

    return render(request, 'app_contatos/index.html', {
        'contatos': contatos
    })
    