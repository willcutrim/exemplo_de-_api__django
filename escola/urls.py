from django.urls.conf import path
from . import views
from django.urls import path

urlpatterns = [ 
    path('', views.pega_aluno, name='pegar')
]
