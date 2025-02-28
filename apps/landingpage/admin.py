from django.contrib import admin
from .models import *


@admin.register(LandingPage)
class LandingPageAdmin(admin.ModelAdmin):
        list_display = ('nome', 'descricao', 'ativo', 
                        'principal_texto', 'image', 'aniversario', 
                        'endereco', 'complemento', 'bairro', 'cidade', 'cep', 'uf', 
                        'contato', 
                        'email', 
                        'facebook', 'x', 'instagram', 'linkedin', 
                        'missao_valor_titulo', 'missao_valor_complemento', 'missao_valor_item_1', 'missao_valor_item_2', 'missao_valor_item_3', 'missao_valor_item_4', 'missao_valor_item_5', 'missao_valor_item_6', 
                        'funcionamento_seg', 'funcionamento_ter', 'funcionamento_qua', 'funcionamento_qui', 'funcionamento_sex', 'funcionamento_sab', 'funcionamento_dom', 
                        'footer_descricao', 'ano')
        list_filter = ('nome',)
        search_fields = ('nome',)
        ordering = ('nome',)
        fieldsets = (
            (None, {
                'fields': ('nome', 'ativo',) 
            }),
            ('Conteúdo Principal', {
                'fields': ('principal_texto', 'image', 'aniversario',)
            }),
            ('Endereço', {
                'fields': ('endereco', 'complemento', 'bairro', 'cidade', 'cep', 'uf',)
            }),
            ('Contato', {
                'fields': ('contato', 'email',)
            }),
            ('Redes Sociais', {
                'fields': ('facebook', 'x','instagram', 'linkedin',)
            }),
            ('Missão e Valores', {
                'fields': ('missao_valor_titulo', 'missao_valor_complemento', 'missao_valor_item_1', 'missao_valor_item_2', 'missao_valor_item_3', 'missao_valor_item_4', 'missao_valor_item_5', 'missao_valor_item_6',)
            }),
            ('Funcionamento', {
                'fields': ('funcionamento_seg', 'funcionamento_ter', 'funcionamento_qua', 'funcionamento_qui', 'funcionamento_sex', 'funcionamento_sab', 'funcionamento_dom',)
            }),
            ('Footer', {
                'fields': ('footer_descricao', 'ano',)
            }),
        )

@admin.register(Programas)
class ProgramasPageAdmin(admin.ModelAdmin):
    pass

@admin.register(Oferecemos)
class OferecemosPageAdmin(admin.ModelAdmin):
    pass

@admin.register(Eventos)
class EventosPageAdmin(admin.ModelAdmin):
    pass

@admin.register(Colaboradores)
class ColaboradoresPageAdmin(admin.ModelAdmin):
    pass