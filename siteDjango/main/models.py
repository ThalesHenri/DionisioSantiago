from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Email")
    is_admin = models.BooleanField(default=False, verbose_name="Is Admin")
    is_staff = models.BooleanField(default=False, verbose_name="Is Staff")

    # Add related_name to avoid clashes
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",  # Custom related_name
        blank=True,
        verbose_name="Groups"
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_set",  # Custom related_name
        blank=True,
        verbose_name="User Permissions"
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    
    
class Produto(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome do Produto")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")
    estoque = models.PositiveIntegerField(verbose_name="Quantidade em Estoque")
    foto = models.ImageField(upload_to='produtos/', blank=True, null=True, verbose_name="Foto do Produto")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

class Pedido(models.Model):
    STATUS_CHOICES = [
        ('criado', 'Criado'),
        ('preparando', 'Preparando'),
        ('pronto', 'Pronto'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pedidos", verbose_name="Usuário")
    produtos = models.ManyToManyField(Produto, through="ItemPedido", verbose_name="Produtos")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='criado', verbose_name="Status")
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    def __str__(self):
        return f"Pedido #{self.id} - {self.usuario.email}"

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="itens", verbose_name="Pedido")
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name="item_pedido", verbose_name="Produto")
    quantidade = models.PositiveIntegerField(verbose_name="Quantidade")
    preco_total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço Total")

    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome} - Pedido #{self.pedido.id}"

    class Meta:
        verbose_name = "Item do Pedido"
        verbose_name_plural = "Itens do Pedido"
