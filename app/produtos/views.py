from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from .models import Produto
from .forms import ProdutoForm, CadastroForm

# Create your views here.
@login_required
def listar_produtos(request):
    produtos = Produto.objects.filter(usuario=request.user)
    return render(request, 'listar_produtos.html', {'produtos' : produtos})

@login_required
def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.usuario = request.user
            produto.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm()

    return render(request, 'adicionar_produto.html', {'form': form})

@login_required
def atualizar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk, usuario=request.user)
    
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm(instance=produto)
    
    return render(request, 'atualizar_produto.html', {'form': form, 'produto': produto})

@login_required
def detalhes_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, 'detalhes_produto.html', {'produto': produto})

@login_required
def excluir_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method in ['POST', 'GET']:
        produto.delete()
        return redirect('listar_produtos')
    
def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('listar_produtos')
        else:
            messages.error(request, 'Usuário ou senha incorretos.')
            return render(request, 'login.html')
    else:
        return render(request,'login.html')
    
def custom_logout(request):
    logout(request)
    return redirect('login')

def custom_cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                messages.success(request, 'Cadastro realizado com sucesso.')
                return redirect(reverse('login')) 
            except Exception as e:
                messages.error(request, f'Erro ao cadastrar: {e}')
        else:
            messages.error(request, 'Por favor, corrija os erros no formulário.')
    else:
        form = CadastroForm()
    return render(request, 'signup.html', {'form': form})
