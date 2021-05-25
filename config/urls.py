from escola import urls
from django.contrib import admin
from django.urls import path, include
import rest_framework
from escola.views import AlunosViewSet
from rest_framework import routers
from django import urls

router = routers.DefaultRouter()
router.register(r'alunos', AlunosViewSet)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('pegar/', include('escola.urls'))
]
