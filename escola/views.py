from rest_framework import viewsets
from escola.models import Aluno
from escola.serializer import AlunoSerializer
from django.shortcuts import HttpResponse, render


class AlunosViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    
    def __init__(self):
        self.pegar = Aluno.objects.all()
        print(self.pegar)

def pega_aluno(request):
    pegue = Aluno.objects.all()
    
    
    return render(request, 'index.html', {'pegue': pegue})