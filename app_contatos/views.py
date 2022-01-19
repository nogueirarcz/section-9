from django.shortcuts import render
from .models import Contato


def index(request):

    contatos = Contato.objects.all()

    return render(request, 'app_contatos/index.html', {
        'contatos': contatos
    })
    
def ver_contato(request, contato_id):

    contato = Contato.objects.get(id=contato_id)

    return render(request, 'app_contatos/ver_contato.html',{
        'contato': contato
    })
