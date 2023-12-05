from django.shortcuts import render, get_object_or_404
from menu.models import ItemDeMenu


def index(request):
    itens_de_menu = ItemDeMenu.objects.order_by("-data_item").filter(publicado=True)
    return render(request, 'menu/index.html', { 'cards' : itens_de_menu} )

def imagem(request, itemdemenu_id):
    item_de_menu = get_object_or_404(ItemDeMenu, pk=itemdemenu_id)
    return render(request, 'menu/imagem.html', {"item_de_menu" : item_de_menu})

def buscar(request):
    itens_de_menu = ItemDeMenu.objects.order_by("-data_item").filter(publicado=True)
    
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            itens_de_menu = itens_de_menu.filter(nome__icontains=nome_a_buscar)

    return render(request, 'menu/buscar.html', { 'cards' : itens_de_menu})