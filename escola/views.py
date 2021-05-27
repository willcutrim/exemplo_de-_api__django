from rest_framework import viewsets
from escola.models import Aluno
from escola.serializer import AlunoSerializer
from django.shortcuts import render
import requests

class AlunosViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all() #listando todos os dados daa class Aluno
    serializer_class = AlunoSerializer #Nosso formulário
"""
    def __init__(self):
        self.pegar = Aluno.objects.all()
        print(self.pegar)

"""

def pegar(request):
    listar = requests.get("http://127.0.0.1:8000/alunos/?format=json")
    teste = listar.json()
    text_input = request.GET.get('text')
    lista_vazia = []
    """
    for item in teste:
        lista_vazia.append((
            item['id'],
            item['nome'],
            item['rg']
        ))
    """
    
    print(text_input)
    id = teste[1]['id']
    nome = teste[1]['nome']
    rg = teste[1]['rg']
    
    #print(f'status= {listar.json()}') 
    return render(request, 'listar.html', {'id': id, 'nome': nome, 'rg': rg})   