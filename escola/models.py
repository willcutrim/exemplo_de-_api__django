from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    rg = models.IntegerField()
    
    def __str___(self):
        return self.nome