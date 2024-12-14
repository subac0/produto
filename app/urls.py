from django.contrib import admin
from django.urls import path, include
from produtos.views import listar_produtos, custom_login, custom_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produtos/', include('produtos.urls')), 
    path('', listar_produtos, name='listar_produtos'), 
    path('login/', custom_login, name='login'),  
    path('logout/', custom_logout, name='logout'),  
]
