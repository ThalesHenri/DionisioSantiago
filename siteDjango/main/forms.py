from django import forms
from .models import User, Produto, Pedido, ItemPedido

class UserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'}),
        label="Senha",
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_admin', 'is_staff']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome de Usuário'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'is_admin': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_staff': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'estoque',]
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Produto'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Preço'}),
            'estoque': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade em Estoque'}),
        }
        

class CompraForm(forms.Form):
    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome de Usuário'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    telefone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone'}))
    quantidade = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade'}))
    endereco = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Endereço'}))
    observacoes = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Observações'}))
    

class ContatoForm(forms.Form):
    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu Nome'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Seu Email'}))
    mensagem = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Sua Mensagem'}))

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['usuario', 'produtos', 'status']
        widgets = {
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'produtos': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

class ItemPedidoForm(forms.ModelForm):
    class Meta:
        model = ItemPedido
        fields = ['pedido', 'produto', 'quantidade', 'preco_total']
        widgets = {
            'pedido': forms.Select(attrs={'class': 'form-control'}),
            'produto': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade'}),
            'preco_total': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Preço Total'}),
        }
