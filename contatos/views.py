from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Contato
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
# Create your views here.

def index(request):

    contatos = Contato.objects.order_by('-id').filter(
        mostrar = True
    )
    paginator = Paginator(contatos, 2)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render (request, 'contatos/busca.html', {
        'contatos': contatos
    })

def ver_contato(resquest, contato_id):
    # try:
        # contato = Contato.objects.get(id=contato_id)
        contato = get_object_or_404(Contato, id= contato_id)
        if not contato.mostrar:
            raise Http404

        return render (resquest, 'contatos/ver_contato.html', {
            'contato': contato
        })
    # except Contato.DoesNotExist as e:
    #     raise Http404("Essa pagina não existe")

def busca (request):
    termo = request.GET.get('termo')

    if termo is None or not termo:
        raise Http404

    campos = Concat('nome', Value (' '), 'sobrenome')

    contatos = Contato.objects.annotate(
        nome_completo = campos
    ).filter(
        Q(nome_completo__icontains = termo) | Q(telefone__icontains = termo)
    )
    paginator = Paginator(contatos, 2)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render (request, 'contatos/index.html', {
        'contatos': contatos
    })

    