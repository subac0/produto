from django.urls import path
from .views import listar_produtos, adicionar_produto, atualizar_produto, detalhes_produto, excluir_produto
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', listar_produtos, name='listar_produtos'),  # Página inicial de produtos
    path('adicionar/', adicionar_produto, name='adicionar_produto'), 
    path('editar/<int:pk>/', atualizar_produto, name='atualizar_produto'), 
    path('detalhes/<int:pk>/', detalhes_produto, name='detalhes_produto'), 
    path('excluir/<int:pk>/', excluir_produto, name='excluir_produto'),
]
