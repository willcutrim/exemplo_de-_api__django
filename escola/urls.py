from django.urls.conf import path
from . import views
from django.urls import path


urlpatterns = [ 
    path('', views.AlunosViewSet, name='pegar'), 
    path('listar', views.pegar, name='listar')
]
