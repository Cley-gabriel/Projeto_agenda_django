from urllib import request
from django.shortcuts import render
from .models import Contato

# Create your views here.
def index(request):
    contatos = Contato.objects.all()
    return render (request, 'contatos/index.html', {
        'contatos': contatos
    })

def ver_contato(resquest, contato_id):
    contato = Contato.objects.get(id=contato_id)
    return render (resquest, 'contatos/ver_contato.html', {
        'contato': contato
    })