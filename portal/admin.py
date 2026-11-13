from django.contrib import admin
from .models import Conteudo, Menu


@admin.register(Conteudo)
class ConteudoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'ativo')
    prepopulated_fields = {'slug': ('titulo',)}


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo_destino', 'conteudo', 'url_externa', 'ordem', 'ativo')
    list_editable = ('ordem', 'ativo')
