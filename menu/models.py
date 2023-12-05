from django.db import models
from datetime  import datetime

class ItemDeMenu(models.Model):

    OPCOES_CATEGORIAS = [
        ("COMIDAS", "Comidas"),
        ("BEBIDAS", "Bebidas"),
    ]

    nome      = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(max_length=300, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIAS, default="")
    preço     = models.FloatField(null=False, blank=False)
    foto      = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicado = models.BooleanField(default=False)
    data_item = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.nome  
        