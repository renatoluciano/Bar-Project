from django.contrib import admin
from menu.models    import ItemDeMenu

class ListandoItensDeMenu(admin.ModelAdmin):
    list_display       = ("id", "nome", "preço", "publicado",)
    list_display_links = ("id", "nome")
    search_fields      = ("nome",)
    list_filter        = ('categoria',)
    list_editable      = ("publicado",)
    list_per_page      = 8

admin.site.register(ItemDeMenu, ListandoItensDeMenu)
