from django.contrib import admin

# Register your models here.

from .models import Produto,Pedido,ItemPedido,User


admin.site.register(Produto)
admin.site.register(Pedido)
admin.site.register(ItemPedido)
admin.site.register(User)
