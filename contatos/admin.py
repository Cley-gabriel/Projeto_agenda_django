from django.contrib import admin
from .models import Contato, Categoria

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'sobrenome', 'telefone', 'email', 'data_criacao', 'categoria', 'mostrar')
    list_display_links = ('id', 'nome', 'sobrenome')
    list_per_page = 10
    search_fields = ('nome', 'sobrenome')
    list_editable = ('telefone', 'mostrar')

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)