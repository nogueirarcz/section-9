from django.contrib import admin
from .models import Categoria, Contato

class CategoriaAdmin():

    pass


class ContatoAdmin(admin.ModelAdmin):

    list_display = ('nome', 'sobrenome', 'telefone', 'email', 'categoria')

    list_display_links = ('nome',)

#    list_filter = ('nome', 'sobrenome', 'categoria')

    list_per_page = 10

    search_fields = ('nome', 'sobrenome', 'telefone', 'email')


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
