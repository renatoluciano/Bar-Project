from django.urls import path
from menu.views  import index, imagem, buscar

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:itemdemenu_id>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
]