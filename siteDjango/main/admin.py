from django.contrib import admin
# Register your models here.
from .models import Produto,Pedido,ItemPedido,User, ProdutoImagem
from django.utils.html import format_html



class ProdutoImagemInline(admin.TabularInline):
    model = ProdutoImagem
    extra = 2  # Define o número de imagens adicionais que podem ser adicionadas por produto
    fields = ['imagem']
    verbose_name = 'Imagem do Produto'
    verbose_name_plural = 'Imagens do Produto'
    
    def preview(self, obj):
        if obj.imagem:
            return format_html('<img src="{}" width="100" height="100" style="border-radius: 5px;" />', obj.imagem.url)
        return "Nenhuma imagem disponível"
        
    preview.short_description = "Preview"

class ProdutoAdmin(admin.ModelAdmin):
    inlines = [ProdutoImagemInline]
    list_display = ('nome', 'preco', 'estoque')
    
    
admin.site.register(Pedido)
admin.site.register(ItemPedido)
admin.site.register(User)
admin.site.register(Produto, ProdutoAdmin)