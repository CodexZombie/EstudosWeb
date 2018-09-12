# ../connectedin/
# ../perfis/views.py

from django.shortcuts import render
from perfis.models import Perfil

def index(request):
    return render(request, 'index.html')


def exibir(request, perfil_id):

    perfil = Perfil.objects.get(id=perfil_id)

    return render(request, 'perfil.html', { "perfil" : perfil })
