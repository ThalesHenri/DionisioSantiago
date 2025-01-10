
from django.shortcuts import render, get_object_or_404,redirect
from django.conf import settings
from .models import Produto
from .forms import ProdutoForm,UserForm,CompraForm
from .emailSender import EmailSender

# Create your views here.

def homePage(request):
    produtos = Produto.objects.all()
    
    context = {
        'produtos': produtos
    }
    return render(request, 'index.html',context=context)


def comprarProduto(request,produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    
    if request.method == 'POST':
        form = form = CompraForm(request.POST)
        if form.is_valid():
            #capturar os dados do formulario
            quantidade = form.cleaned_data['quantidade']
            observacoes = form.cleaned_data['observacoes']
            
            #calcula o preco total
            preco_total = quantidade * produto.preco
            
            #certifica se tem estoque suficiente
            if quantidade > produto.estoque:
                
                return redirect('main:comprarProduto',produto_id=produto_id)
            
            #diminui a quantidade do estoque
            produto.estoque -= quantidade
            produto.save()
            
            #detalhes do pedido
            detalhes_pedido = f"""
            Produto: {produto.nome}
            nome: {form.cleaned_data['nome']}
            email: {form.cleaned_data['email']}
            telefone: {form.cleaned_data['telefone']}
            Endereço: {form.cleaned_data['endereco']}
            Quantidade: {quantidade}
            Observaçôes: {observacoes}
            Preco total: {preco_total:.2f}
            """
            
            #enviar email
            try:
                emailSender = EmailSender()
                emailSender.startserver()
                emailSender.sendMensage(subject=f"Pedido de {produto.nome}",message=detalhes_pedido)
                emailSender.server.quit()
                print('email enviado com sucesso')
                return redirect('main:homePage')
            except:
                return redirect('main:homePage')
            
    else:
        form = CompraForm()
    
    context = {
        'form': form,
        'produto': produto
    }
    
    return render(request, 'comprarProduto.html', context)